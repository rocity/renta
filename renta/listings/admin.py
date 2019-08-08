from django.contrib import admin

from .models import ListingImage


# Register your models here.
@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    '''Admin View for ListingImage'''

    list_display = ('listing',)
