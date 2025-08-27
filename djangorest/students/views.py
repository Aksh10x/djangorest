from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def students_list(request):
    students=[
        {'name': 'John Doe', 'age': 20},
        {'name': 'Jane Smith', 'age': 22},
        {'name': 'Sam Brown', 'age': 19},
    ]
    return HttpResponse(students)
