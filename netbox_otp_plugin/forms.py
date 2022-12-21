from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django_otp.forms import OTPAuthenticationFormMixin
from django_otp import user_has_device
from utilities.forms import BootstrapMixin

class OTPAuthenticationForm(OTPAuthenticationFormMixin, AuthenticationForm):
    otp_device = forms.CharField(required=False, widget=forms.Select)
    otp_token = forms.CharField(required=False, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    otp_challenge = forms.CharField(required=False)

    def clean(self):
        self.cleaned_data = super().clean()
        user = self.get_user()
        # use get_plugin_config better
        plugin_config = settings.PLUGINS_CONFIG['netbox_otp_plugin'] 
        otp_required = plugin_config.get('otp_required')
        if user_has_device(user) or otp_required:
            self.clean_otp(self.get_user())

        return self.cleaned_data

class OTPLoginForm(BootstrapMixin, OTPAuthenticationForm):
    pass
