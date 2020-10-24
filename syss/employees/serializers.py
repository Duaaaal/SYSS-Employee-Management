from rest_framework import serializers
from employees.models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Employee
        fields = ['owner', 'name', 'email', 'department']


class UserSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'employees']