from django_filters.rest_framework import FilterSet, CharFilter

from company.models import Employee


class EmployeeFilter(FilterSet):

    last_name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['department', 'last_name']
