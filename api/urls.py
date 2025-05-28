from django.urls import path

from .views import EmployeesView, student_detail_view, students_view

urlpatterns = [
    path("students/", students_view),
    path("students/<int:pk>/", student_detail_view),
    path("employees/", EmployeesView.as_view()),
]
