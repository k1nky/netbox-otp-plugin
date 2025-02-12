from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django_otp.forms import OTPAuthenticationFormMixin
from django_otp import user_has_device

from netbox.forms import NetBoxModelForm
from netbox.plugins import get_plugin_config
from users.models import User
from utilities.forms.fields import DynamicModelChoiceField

from .models import Device


class OTPAuthenticationForm(OTPAuthenticationFormMixin, AuthenticationForm):
    otp_device = forms.CharField(
        required=False,
        widget=forms.Select
    )
    otp_token = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'off',
                'class': 'rounded'
            }
        ),
        label="OTP Token"
    )
    otp_challenge = forms.CharField(
        required=False
    )

    def clean(self):
        self.cleaned_data = super().clean()
        user = self.get_user()
        otp_required = get_plugin_config('netbox_otp_plugin', 'otp_required')
        if user_has_device(user) or otp_required:
            self.clean_otp(self.get_user())

        return self.cleaned_data


class OTPLoginForm(OTPAuthenticationForm):
    pass


class DeviceForm(NetBoxModelForm):
    user = DynamicModelChoiceField(
        label=_('User'),
        queryset=User.objects.all(),
        required=True
    )

    class Meta:
        model = Device
        fields = (
            'name',
            'digits',
            'user',
        )
