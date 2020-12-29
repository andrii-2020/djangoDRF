from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .models import OfficeM
from .serializers import OfficeSerialiaer

# Create your views here.


class MyApi(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerialiaer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        filt = self.request.query_params.get('filter',  None)
        filt1 = self.request.query_params.get('startswith', None)
        qs = OfficeM.objects.all()
        if filt:
            qs = qs.filter(pk=filt)
        if filt1:
            qs = qs.filter(name__startswith=filt1)
        serializer = OfficeSerialiaer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        f = self.request.query_params.get('filter', None)
        qs = OfficeM.objects.get(pk=f)
        data = self.request.data
        serializer = OfficeSerialiaer(qs, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)