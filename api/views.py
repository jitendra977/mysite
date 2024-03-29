from django.shortcuts import redirect, render
import requests
from rest_framework import viewsets
from rest_framework.decorators import action 
from rest_framework.response import Response
from .models import Company, Employee
from .serializers import CompanySerializers, EmployeeSerializers
from django.http import JsonResponse

# show data use api 
def index_view(request):
    # Make an API request to fetch employees data
    api_url = 'http://127.0.0.1:8000/api/employees/'
    response = requests.get(api_url)
    if response.status_code == 200:
        employees_data = response.json()  # Convert response to JSON format
    else:
        employees_data = []  # If API request fails, initialize an empty list
    context = {'employees': employees_data}  # Pass only API data in context
    return render(request, 'api_index.html', context)

# delete item
def delete_emp(request, id):
    emp = Employee.objects.filter(id=id).first()
    if emp:
        emp.delete()
    return redirect('/api_home/')
    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    
    @action(detail=True, methods=['get'])  # Explicitly specify methods=['get']
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializers(emp, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Company.DoesNotExist:
            return Response({'message': "Company does not exist!"})
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


