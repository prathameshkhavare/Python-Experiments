from django import forms
from django.core.exceptions import ValidationError
from .models import Student, Attendance, Mark


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault("class", "form-check-input")
            elif isinstance(widget, forms.Select):
                widget.attrs.setdefault("class", "form-select")
            else:
                widget.attrs.setdefault("class", "form-control")


class StudentForm(StyledModelForm):
    class Meta:
        model = Student
        fields = ["roll_no", "name", "department", "semester", "email", "phone", "is_active"]
        widgets = {"is_active": forms.CheckboxInput()}


class AttendanceForm(StyledModelForm):
    class Meta:
        model = Attendance
        fields = ["student", "date", "status", "note"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"}), "note": forms.TextInput(attrs={"placeholder": "Optional note"})}

    def clean(self):
        cleaned = super().clean()
        student, date = cleaned.get("student"), cleaned.get("date")
        if student and date:
            qs = Attendance.objects.filter(student=student, date=date)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise ValidationError("Attendance has already been recorded for this student on that date.")
        return cleaned


class MarkForm(StyledModelForm):
    class Meta:
        model = Mark
        fields = ["student", "subject", "exam", "score", "max_score"]
        widgets = {
            "subject": forms.TextInput(attrs={"placeholder": "e.g. Mathematics"}),
            "exam": forms.TextInput(attrs={"placeholder": "e.g. Midterm"}),
            "score": forms.NumberInput(attrs={"min": "0", "step": "0.01"}),
            "max_score": forms.NumberInput(attrs={"min": "0.01", "step": "0.01"}),
        }

    def clean(self):
        cleaned = super().clean()
        score, maximum = cleaned.get("score"), cleaned.get("max_score")
        if score is not None and maximum is not None and score > maximum:
            self.add_error("score", "Score cannot exceed maximum score.")
        student, subject, exam = cleaned.get("student"), cleaned.get("subject"), cleaned.get("exam")
        if student and subject and exam:
            qs = Mark.objects.filter(student=student, subject__iexact=subject, exam__iexact=exam)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise ValidationError("A mark record already exists for this student, subject and exam.")
        return cleaned
