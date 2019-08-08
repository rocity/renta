from django.shortcuts import render

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Listing, ListingImage
from .serializers import ListingSerializer, ListingImageSerializer
from .permissions import CanManageListing, CanManageListingImage


class ListingViewSet(ModelViewSet):
    """
    Listings Views
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, CanManageListing, )


class ListingImageViewSet(ModelViewSet):
    """
    ListingImage Views
    """

    queryset = ListingImage.objects.all()
    serializer_class = ListingImageSerializer
    permission_classes = (permissions.IsAuthenticated, CanManageListingImage, )
