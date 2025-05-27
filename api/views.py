from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student


def students_view(request):

    # primeiro exemplo resposta em formato json
    students =Student.objects.all() # QuerySet nao é seriaizavel.
    students_list = list(students.values()) # Serialização Manual
    return JsonResponse(students_list, safe=False)
