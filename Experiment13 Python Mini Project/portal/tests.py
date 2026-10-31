from datetime import date
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Student, Attendance, Mark


class CampusModelTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            roll_no="SC-001", name="Test Student", department="Computer Science", semester=1
        )

    def test_mark_percentage_and_grade(self):
        mark = Mark(student=self.student, subject="Maths", exam="Midterm", score=Decimal("85"), max_score=Decimal("100"))
        mark.full_clean()
        mark.save()
        self.assertEqual(mark.percentage, Decimal("85.00"))
        self.assertEqual(mark.grade, "A")

    def test_attendance_duplicate_constraint(self):
        Attendance.objects.create(student=self.student, date=date(2026, 1, 1), status=Attendance.PRESENT)
        with self.assertRaises(Exception):
            Attendance.objects.create(student=self.student, date=date(2026, 1, 1), status=Attendance.ABSENT)


class CampusViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="admin", password="Strong-test-password-123")
        self.user.is_staff = True
        self.user.save()

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_loads_for_staff(self):
        self.client.login(username="admin", password="Strong-test-password-123")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
