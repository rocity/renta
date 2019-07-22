from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import User
from .serializers import ProfileSerializer
from .permissions import CanManageProfile


class ProfileViewSet(viewsets.ModelViewSet):
    """
    View to let users fetch and update their profile
    """

    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, CanManageProfile, )

    @action(detail=False, methods=['get', ], url_name='own')
    def own(self, request, *args, **kwargs):
        instance = get_object_or_404(User, id=request.user.id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
