from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.CampusLoginView.as_view(), name="login"),
    path("logout/", views.CampusLogoutView.as_view(), name="logout"),
    path("students/", views.students, name="students"),
    path("students/add/", views.student_add, name="student_add"),
    path("students/<int:pk>/edit/", views.student_edit, name="student_edit"),
    path("students/<int:pk>/delete/", views.student_delete, name="student_delete"),
    path("attendance/", views.attendance, name="attendance"),
    path("marks/", views.marks, name="marks"),
    path("reports/export/", views.export_csv, name="export"),
]
