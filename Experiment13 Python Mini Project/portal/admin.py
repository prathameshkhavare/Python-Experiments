from django.contrib import admin
from .models import Student, Attendance, Mark


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("roll_no", "name", "department", "semester", "email", "is_active")
    list_filter = ("department", "semester", "is_active")
    search_fields = ("roll_no", "name", "email")
    ordering = ("name",)
    list_per_page = 30


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "status", "recorded_by")
    list_filter = ("date", "status")
    search_fields = ("student__roll_no", "student__name")
    date_hierarchy = "date"
    list_select_related = ("student", "recorded_by")


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "exam", "score", "max_score", "grade")
    list_filter = ("subject", "exam")
    search_fields = ("student__roll_no", "student__name", "subject")
    list_select_related = ("student", "recorded_by")
