from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView,Response,status
from .models import Address,Student
from .serializers import AddressSerializer,StudentSerializer

# Create your views here.

class StudentView(APIView):

    def get(self, request, format=None):
        id=request.GET['standard']
        if id is not None:
            stu = Student.objects.filter(standard=id)
            stu_ser = StudentSerializer(stu, many=True)
            return Response (stu_ser.data)
        stu = Student.objects.all()
        stu_ser = StudentSerializer(stu, many=True)
        return Response (stu_ser.data)

    def post(self, request, format=None):
        stu_ser = StudentSerializer(data=request.data)
        if stu_ser.is_valid():
            stu_ser.save()
            return Response(stu_ser.data, status=status.HTTP_201_CREATED)
        return Response(stu_ser.errors, status=status.HTTP_400_BAD_REQUEST)



