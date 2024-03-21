from rest_framework import serializers
from api.models import Company, Employee
# create Serializers  
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"
    
# employee serializers
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"