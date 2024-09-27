from django.urls import path
from .views import EmployeeAPIView, EmployeeUpdateAPIView, DepartmentAPIView, DepartmentUpdateAPIView

urlpatterns = [
    path('employees/', EmployeeAPIView.as_view(), name='employees'),
    path('employees/<int:id>/', EmployeeUpdateAPIView.as_view(), name="emp-update"),
    path('department/', DepartmentAPIView.as_view(), name='departments'),
    path('department/<int:id>/', DepartmentUpdateAPIView.as_view(), name="dep-update")
]
