from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CampusViewSet,
    ClassDetailView,
    ClassView,
    EmployeeDetailView,
    EmployeesView,
    TeacherDetailView,
    TeacherView,
    student_detail_view,
    students_view,
)

router = DefaultRouter()
router.register("campus", CampusViewSet, basename="campus")


urlpatterns = [
    path("", include(router.urls)),
    path("students/", students_view),
    path("students/<int:pk>/", student_detail_view),
    path("employees/", EmployeesView.as_view()),
    path("employees/<int:pk>", EmployeeDetailView.as_view()),
    path("classes/", ClassView.as_view()),
    path("classes/<int:pk>", ClassDetailView.as_view()),
    path("teachers/", TeacherView.as_view()),
    path("teachers/<int:pk>/", TeacherDetailView.as_view()),
]
