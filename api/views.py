from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student

from .serializers import StudentSerializer


@api_view(["GET"])
def students_view(request):
    if request.method == "GET":
        # recuperando todos os dados
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
