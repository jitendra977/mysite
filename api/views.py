from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializers, EmployeeSerializers
from rest_framework.decorators import action 
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    
    @action(detail=True, methods=['get'])  # Explicitly specify methods=['get']
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializers(emps, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Company.DoesNotExist:
            return Response({'message': "Company does not exist!"})
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
