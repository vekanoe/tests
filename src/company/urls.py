from django.urls import path, include
from rest_framework.routers import DefaultRouter

from company.views import EmployeeViewSet, DepartmentListAPIView

router = DefaultRouter()
router.register('employees', EmployeeViewSet)


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('departments/', DepartmentListAPIView.as_view())
] + router.urls
