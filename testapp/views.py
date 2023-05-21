from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.generics import get_object_or_404


class EmployeeViewSet(ViewSet):
    def list(self, request):
        emps = Employee.objects.all()
        serializer = EmployeeSerializers(emps, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        emps = Employee.objects.all()
        emp = get_object_or_404(emps, pk=pk)
        serializer = EmployeeSerializers(emp)
        return Response(serializer.data)
    def update(self, request, pk=None):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializers(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        msg = {'msg': "Resource deleted successfully"}
        return Response(msg, status=status.HTTP_200_OK)
