from django.urls import path

from .views import (
    ClassDetailView,
    ClassView,
    EmployeeDetailView,
    EmployeesView,
    student_detail_view,
    students_view,
)

urlpatterns = [
    path("students/", students_view),
    path("students/<int:pk>/", student_detail_view),
    path("employees/", EmployeesView.as_view()),
    path("employees/<int:pk>", EmployeeDetailView.as_view()),
    path("classes/", ClassView.as_view()),
    path("classes/<int:pk>/", ClassDetailView.as_view()),
]
