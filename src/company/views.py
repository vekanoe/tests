from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from company.models import Employee, Department
from company.serializers import EmployeeSerializer, DepartmentSerializer
from company.filters import EmployeeFilter


class EmployeePageNumberPagination(PageNumberPagination):
    page_size = 4


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter
    pagination_class = EmployeePageNumberPagination
    permission_classes = [IsAdminUser]


class DepartmentListAPIView(ListAPIView):

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
