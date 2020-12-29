from django.urls import path

from .views import MyApi

urlpatterns = [
    path('', MyApi.as_view(), name="myapiviw")
]