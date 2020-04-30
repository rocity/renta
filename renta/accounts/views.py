from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

from .models import User
from .serializers import ProfileSerializer, SignUpSerializer
from .permissions import CanManageProfile, CanSignUp


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


class SignupView(APIView):
    """
    View to let users register to the app
    """

    permission_classes = [CanSignUp, ]

    @property
    def allowed_methods(self):
        return ['post', ]

    def post(self, *args, **kwargs):
        serializer = SignUpSerializer(data=self.request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
