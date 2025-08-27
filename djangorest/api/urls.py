from django.http import JsonResponse
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_list, name='students_list_api'),
    path('add-student/', views.add_student, name='add_student_api'),
]
