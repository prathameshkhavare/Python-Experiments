from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q


class Student(models.Model):
    roll_no = models.CharField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=150, db_index=True)
    department = models.CharField(max_length=100, db_index=True)
    semester = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["department", "semester"]),
            models.Index(fields=["is_active", "name"]),
        ]

    def __str__(self):
        return f"{self.roll_no} — {self.name}"


class Attendance(models.Model):
    PRESENT = "Present"
    ABSENT = "Absent"
    STATUS_CHOICES = [(PRESENT, "Present"), (ABSENT, "Absent")]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField(db_index=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PRESENT)
    note = models.CharField(max_length=250, blank=True)
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="attendance_recorded",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "student__name"]
        constraints = [
            models.UniqueConstraint(fields=["student", "date"], name="unique_student_attendance_per_day"),
            models.CheckConstraint(condition=Q(status__in=["Present", "Absent"]), name="attendance_status_valid"),
        ]
        indexes = [models.Index(fields=["date", "status"])]

    def __str__(self):
        return f"{self.student} · {self.date} · {self.status}"


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="marks")
    subject = models.CharField(max_length=100, db_index=True)
    exam = models.CharField(max_length=100, default="Final")
    score = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal("0"))])
    max_score = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal("100"), validators=[MinValueValidator(Decimal("0.01"))])
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="marks_recorded",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["student__name", "subject", "exam"]
        constraints = [
            models.UniqueConstraint(fields=["student", "subject", "exam"], name="unique_student_subject_exam"),
            models.CheckConstraint(condition=Q(score__gte=0), name="mark_score_nonnegative"),
            models.CheckConstraint(condition=Q(max_score__gt=0), name="mark_max_score_positive"),
        ]

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        if self.score is not None and self.max_score is not None and self.score > self.max_score:
            raise ValidationError({"score": "Score cannot exceed maximum score."})

    @property
    def percentage(self):
        if not self.max_score:
            return Decimal("0.00")
        return (self.score * Decimal("100") / self.max_score).quantize(Decimal("0.01"))

    @property
    def grade(self):
        pct = self.percentage
        if pct >= 90:
            return "A+"
        if pct >= 80:
            return "A"
        if pct >= 70:
            return "B"
        if pct >= 60:
            return "C"
        if pct >= 50:
            return "D"
        return "F"

    def __str__(self):
        return f"{self.student} · {self.subject} · {self.percentage}%"
