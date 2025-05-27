from django.shortcuts import render
from django.http import JsonResponse

def students_view(request):

    # primeiro exemplo respostau em formato json
    students = {
        'id': 1,
        'name': 'Rathan',
        'class': 'Computer Science'
    }
    return JsonResponse(students)
