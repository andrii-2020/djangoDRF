from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserS(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UpTOAdminS(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }