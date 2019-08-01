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
    images = serializers.ListField(
        child=serializers.ImageField(use_url=True),
        write_only=True
    )

    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'price', 'billing_frequency', 'location',
                  'location_coordinates', 'user', 'images', 'image_urls', )

    def save(self, **kwargs):

        images = self.validated_data.pop('images', [])

        super(ListingSerializer, self).save(**kwargs)

        for image in images:
            ListingImage.objects.create(listing=self.instance, image=image)

    def get_image_urls(self, obj):
        return ListingImageSerializer(instance=obj.listingimage_set.all(), many=True).data
