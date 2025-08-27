from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def students_list(request):
    if(request.method=='GET'):
        students=Student.objects.all()
        serialier=StudentSerializer(students,many=True)
        return Response(serialier.data, status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
def add_student(request):
    if(request.method=='POST'):
        serializer=StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
