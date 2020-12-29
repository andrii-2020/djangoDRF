from  rest_framework.serializers import ModelSerializer

from .models import OfficeM


class OfficeSerialiaer(ModelSerializer):
    class Meta:
        model = OfficeM
        fields = ('id', 'name', 'city')