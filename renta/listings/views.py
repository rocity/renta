from django.shortcuts import render

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Listing
from .serializers import ListingSerializer
from .permissions import CanManageListing


class ListingViewSet(ModelViewSet):
    """
    Listings Views
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, CanManageListing, )
