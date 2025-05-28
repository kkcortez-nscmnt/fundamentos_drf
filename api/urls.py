from django.urls import path

from .views import EmployeeDetailView, EmployeesView, student_detail_view, students_view

urlpatterns = [
    path("students/", students_view),
    path("students/<int:pk>/", student_detail_view),
    path("employees/", EmployeesView.as_view()),
    path("employees/<int:pk>", EmployeeDetailView.as_view()),
]
