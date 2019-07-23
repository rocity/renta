from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    """
    Listing Serializer
    """

    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'price', 'billing_frequency', 'location',
                  'location_coordinates', 'user', )
