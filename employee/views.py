from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmployeeM
from .serializer import EmployeeSerializer


class EmployeeListView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        qs = EmployeeM.objects.all()
        data = EmployeeSerializer(qs, many=True).data
        return Response(data, status.HTTP_201_CREATED)


class EmployeeDeleteUpdateView(APIView):
    @staticmethod
    def delete(*args, **kwargs):
        id = kwargs.get('id')
        get_object_or_404(EmployeeM, pk=id).delete()
        return Response("ok", status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        data = self.request.data
        instance = get_object_or_404(EmployeeM, pk=id)
        serializer = EmployeeSerializer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
