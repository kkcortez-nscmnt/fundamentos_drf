from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    # primeiro exemplo insercao de dados na view utilizando lista.
    students = [
        {"id": 1, "name": "John Doe", "age": 25}
    ]
    return HttpResponse(students)
