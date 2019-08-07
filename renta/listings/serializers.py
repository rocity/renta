from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Listing, ListingImage


class ListingImageSerializer(serializers.ModelSerializer):
    """
    ListingImage Serializer
    """

    class Meta:
        model = ListingImage
        fields = ('id', 'listing', 'image', )


class ListingSerializer(serializers.ModelSerializer):
    """
    Listing Serializer
    """
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                              queryset=get_user_model().objects.all())
    image_urls = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'price', 'billing_frequency', 'location',
                  'location_coordinates', 'user', 'image_urls', 'owner', 'is_owner', )

    def get_image_urls(self, obj):
        return ListingImageSerializer(instance=obj.listingimage_set.all(), many=True).data

    def get_owner(self, obj):
        return obj.user.get_full_name()

    def get_is_owner(self, obj):
        try:
            return self.context.get('request').user == obj.user
        except AttributeError:
            return False
