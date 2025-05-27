from django.urls import path

from .views import student_detail_view, students_view

urlpatterns = [
    path("students/", students_view),
    path("students/<int:pk>/", student_detail_view),
]
