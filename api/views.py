from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student

from .serializers import StudentSerializer


@api_view(["GET", "POST"])
def students_view(request):
    if request.method == "GET":
        # recuperando todos recursos registrados em tabela no banco
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        # criando registro de recurso em tabela no banco
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def student_detail_view(request, pk):
    # recuperando um estudante especifico
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
