from rest_framework import status


from rest_framework.generics import  DestroyAPIView, ListAPIView
from rest_framework.mixins import UpdateModelMixin

from .models import EmployeeM
from .serializer import EmployeeSerializer


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = EmployeeM.objects.all()


class EmployeeDeleteUpdateView(DestroyAPIView, UpdateModelMixin):
    queryset = EmployeeM.objects
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
