from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ModelForm
from django.utils.translation import gettext, gettext_lazy as _
from django.urls import reverse_lazy

from accounts.models import User


class UserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"{}\">this form</a>."
        ),
    )

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        if password:
            password.help_text = password.help_text.format('../password/')
        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial.get('password')



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''
    form = UserChangeForm

    list_display = ('email', 'first_name', 'last_name', )
