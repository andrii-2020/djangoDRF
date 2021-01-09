
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .models import OfficeM
from .serializers import OfficeSerialiaer
from employee.serializer import EmployeeSerializer
# Create your views here.


class MyApiList(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerialiaer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(*args, **kwargs):
        qs = OfficeM.objects.all()
        serializer = OfficeSerialiaer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyListDeleteUpdateView(APIView):
    @staticmethod
    def delete(*args, **kwargs):
        id = kwargs.get('id')
        get_object_or_404(OfficeM, pk=id).delete()
        return Response("ok", status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        data = self.request.data
        instance = get_object_or_404(OfficeM, pk=id)
        serializer = OfficeSerialiaer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class OfficeEmployeeView(APIView):
    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        data = self.request.data
        office = get_object_or_404(OfficeM, pk=pk)
        serializer = EmployeeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        #serializer.save(office_id=pk)
        serializer.save(office=office)
        return Response(serializer.data)
