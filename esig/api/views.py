from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from esig.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#class UserViewSet(viewsets.ModelViewSet):
 #   """
  #  API endpoint that allows users to be viewed or edited.
   # """
    #queryset = User.objects.all().order_by('-date_joined')
    #serializer_class = BookSerializer


