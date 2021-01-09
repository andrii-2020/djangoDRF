from django.urls import path
from .views import EmployeeListView, EmployeeDeleteUpdateView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('/<int:id>', EmployeeDeleteUpdateView.as_view(), name="employeesUpdate"),
]