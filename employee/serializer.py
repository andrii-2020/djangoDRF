from rest_framework.serializers import ModelSerializer


from .models import EmployeeM


class  EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeM
        fields = '__all__'
        #exclude = ('office',)
        #extra_kwargs = {'office': {'read_only': True}}