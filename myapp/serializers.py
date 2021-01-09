from  rest_framework.serializers import ModelSerializer

from employee.serializer import EmployeeSerializer
from .models import OfficeM


class OfficeSerialiaer(ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = OfficeM
        fields = ('__all__')