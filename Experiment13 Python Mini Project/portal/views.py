import csv
from datetime import date, timedelta
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.db.models import Avg, Count, Q, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .forms import StudentForm, AttendanceForm, MarkForm
from .models import Student, Attendance, Mark
from .permissions import can_edit_academics, can_manage_students, role_names


class CampusLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


class CampusLogoutView(LogoutView):
    next_page = reverse_lazy("login")


def _ensure_user(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("Please sign in to continue.")


def dashboard(request):
    _ensure_user(request)
    today = timezone.localdate()
    total_students = Student.objects.filter(is_active=True).count()
    total_attendance = Attendance.objects.count()
    present_count = Attendance.objects.filter(status=Attendance.PRESENT).count()
    attendance_percentage = round(present_count * 100 / total_attendance, 1) if total_attendance else 0
    average = Mark.objects.aggregate(avg=Avg("score"))["avg"]
    # Overall percentage uses the average per-record percentage, not raw scores with differing maxima.
    mark_rows = list(Mark.objects.only("score", "max_score"))
    overall_percentage = round(sum((float(m.percentage) for m in mark_rows), 0) / len(mark_rows), 1) if mark_rows else 0
    departments = list(
        Student.objects.filter(is_active=True).values("department").annotate(total=Count("id")).order_by("-total", "department")
    )
    recent_students = Student.objects.filter(is_active=True).order_by("-created_at")[:6]
    low_attendance = []
    for student in Student.objects.filter(is_active=True):
        stats = student.attendance_records.aggregate(total=Count("id"), present=Count("id", filter=Q(status=Attendance.PRESENT)))
        if stats["total"] >= 5:
            pct = round(stats["present"] * 100 / stats["total"], 1)
            if pct < 75:
                low_attendance.append({"student": student, "percentage": pct})
    low_attendance.sort(key=lambda item: item["percentage"])
    low_attendance = low_attendance[:10]

    start_date = today - timedelta(days=6)
    attendance_trend = []
    for offset in range(7):
        day = start_date + timedelta(days=offset)
        records = Attendance.objects.filter(date=day)
        total = records.count()
        present = records.filter(status=Attendance.PRESENT).count()
        attendance_trend.append({
            "date": day.strftime("%a"),
            "present": present,
            "absent": records.filter(status=Attendance.ABSENT).count(),
            "rate": round(present * 100 / total, 1) if total else 0,
        })

    context = {
        "total_students": total_students, "total_attendance": total_attendance,
        "attendance_percentage": attendance_percentage, "overall_percentage": overall_percentage,
        "departments": departments, "recent_students": recent_students,
        "low_attendance": low_attendance, "attendance_trend": attendance_trend,
        "role_names": sorted(role_names(request.user)),
    }
    return render(request, "dashboard.html", context)


def students(request):
    _ensure_user(request)
    query = request.GET.get("q", "").strip()
    qs = Student.objects.all()
    if query:
        qs = qs.filter(
            Q(name__icontains=query) | Q(roll_no__icontains=query) |
            Q(department__icontains=query) | Q(email__icontains=query)
        )
    department = request.GET.get("department", "").strip()
    if department:
        qs = qs.filter(department__iexact=department)
    context = {
        "students": qs, "query": query, "department": department,
        "departments_filter": Student.objects.order_by().values_list("department", flat=True).distinct(),
        "can_manage_students": can_manage_students(request.user),
    }
    return render(request, "students.html", context)


@require_http_methods(["GET", "POST"])
def student_add(request):
    _ensure_user(request)
    if not can_manage_students(request.user):
        raise PermissionDenied("Only administrators can add students.")
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student created successfully.")
        return redirect("students")
    return render(request, "student_form.html", {"form": form, "heading": "Add student"})


@require_http_methods(["GET", "POST"])
def student_edit(request, pk):
    _ensure_user(request)
    if not can_manage_students(request.user):
        raise PermissionDenied("Only administrators can edit student profiles.")
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student details updated.")
        return redirect("students")
    return render(request, "student_form.html", {"form": form, "heading": "Edit student", "student": student})


@require_http_methods(["GET", "POST"])
def student_delete(request, pk):
    _ensure_user(request)
    if not can_manage_students(request.user):
        raise PermissionDenied("Only administrators can delete students.")
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student and related records deleted.")
        return redirect("students")
    return render(request, "confirm_delete.html", {"student": student})


@require_http_methods(["GET", "POST"])
def attendance(request):
    _ensure_user(request)
    selected_date_raw = request.GET.get("date", "")
    selected_date = timezone.localdate()
    if selected_date_raw:
        try:
            selected_date = date.fromisoformat(selected_date_raw)
        except ValueError:
            messages.warning(request, "Invalid date. Showing today's attendance.")
    form = AttendanceForm(request.POST or None, initial={"date": timezone.localdate()})
    if request.method == "POST":
        if not can_edit_academics(request.user):
            raise PermissionDenied("Teacher or administrator access is required to record attendance.")
        if form.is_valid():
            record = form.save(commit=False)
            record.recorded_by = request.user
            record.save()
            messages.success(request, "Attendance saved.")
            return redirect(f"{reverse_lazy('attendance')}?date={record.date.isoformat()}")
    records = Attendance.objects.filter(date=selected_date).select_related("student", "recorded_by")
    return render(request, "attendance.html", {
        "form": form, "records": records, "selected_date": selected_date,
        "can_edit_academics": can_edit_academics(request.user),
    })


@require_http_methods(["GET", "POST"])
def marks(request):
    _ensure_user(request)
    form = MarkForm(request.POST or None)
    if request.method == "POST":
        if not can_edit_academics(request.user):
            raise PermissionDenied("Teacher or administrator access is required to record marks.")
        if form.is_valid():
            record = form.save(commit=False)
            record.recorded_by = request.user
            record.save()
            messages.success(request, "Marks saved successfully.")
            return redirect("marks")
    records = Mark.objects.select_related("student", "recorded_by").all()
    return render(request, "marks.html", {
        "form": form, "records": records,
        "can_edit_academics": can_edit_academics(request.user),
    })


def export_csv(request):
    _ensure_user(request)
    if not can_edit_academics(request.user):
        raise PermissionDenied("Teacher or administrator access is required to export reports.")
    report_type = request.GET.get("type", "students").lower()
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="smartcampus_{report_type}_{timezone.localdate().isoformat()}.csv"'
    response.write("\ufeff")
    writer = csv.writer(response)

    if report_type == "attendance":
        writer.writerow(["Roll No", "Student", "Department", "Date", "Status", "Note", "Recorded By"])
        for row in Attendance.objects.select_related("student", "recorded_by").order_by("-date", "student__name").iterator():
            writer.writerow([row.student.roll_no, row.student.name, row.student.department, row.date, row.status, row.note, row.recorded_by.username if row.recorded_by else ""])
    elif report_type == "marks":
        writer.writerow(["Roll No", "Student", "Department", "Subject", "Exam", "Score", "Maximum", "Percentage", "Grade"])
        for row in Mark.objects.select_related("student").order_by("student__name", "subject").iterator():
            writer.writerow([row.student.roll_no, row.student.name, row.student.department, row.subject, row.exam, row.score, row.max_score, row.percentage, row.grade])
    elif report_type == "students":
        writer.writerow(["Roll No", "Name", "Department", "Semester", "Email", "Phone", "Active"])
        for row in Student.objects.order_by("name").iterator():
            writer.writerow([row.roll_no, row.name, row.department, row.semester, row.email, row.phone, row.is_active])
    else:
        return HttpResponse("Unknown report type.", status=400)
    return response
