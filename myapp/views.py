from django.db.models import F, Prefetch
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from user.permissions import IsAdmin

from .models import OfficeM
from .serializers import OfficeSerialiaer
from employee.serializer import EmployeeSerializer
from employee.models import EmployeeM


class MyApiList(ListCreateAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = OfficeSerialiaer

    def get_queryset(self):
        city = self.request.query_params.get('city')
        age = self.request.query_params.getlist('age')
        qs = OfficeM.objects.all()
        if city:
            qs = qs.filter(city__iexact=city)
        if age and len(age) == 2:
            objects_filter = EmployeeM.objects.filter(age__range=age, city__iexact=F('office__city'))
            qs = qs.prefetch_related(Prefetch('employees', objects_filter))
        return qs


class MyListDeleteUpdateView(DestroyAPIView, UpdateModelMixin):
    queryset = OfficeM.objects
    serializer_class = OfficeSerialiaer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class OfficeEmployeeView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        office_id = self.kwargs.get('pk')
        office = get_object_or_404(OfficeM, pk=office_id)
        serializer.save(office=office)
