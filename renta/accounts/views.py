from rest_framework import viewsets, permissions

from .models import User
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    View to let users fetch and update their profile
    """

    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )
