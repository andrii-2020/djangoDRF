from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import UserS, UpTOAdminS
from user.permissions import IsSuperUser


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserS
    queryset = User.objects.all()


class CurrentUserView(RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserS

    def get_object(self):
        user = self.request.user
        return user


class UpUserToAdminView(UpdateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsSuperUser,)
    queryset = User.objects.all()
    serializer_class = UpTOAdminS

    def put(self, request, *args, **kwargs):
        user: User = self.get_object()
        print(user)
        user.is_staff = True
        user.save()
        return super().put(request, *args, **kwargs)