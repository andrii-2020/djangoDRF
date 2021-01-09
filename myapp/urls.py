from django.urls import path

from .views import  MyApiList, MyListDeleteUpdateView, OfficeEmployeeView

urlpatterns = [
    path('', MyApiList.as_view(), name="myapiviw"),
    path('/<int:id>', MyListDeleteUpdateView.as_view(), name="readUpdate"),
    path('/<int:pk>/employees', OfficeEmployeeView.as_view(), name="office_employee_create")
]