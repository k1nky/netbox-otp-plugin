import importlib
from django.core.exceptions import ImproperlyConfigured

from extras.plugins import PluginConfig
from netbox.settings import INSTALLED_APPS

if importlib.util.find_spec('django_otp') is None:
    raise ImproperlyConfigured(
        f"netbox_otp_plugin is enabled but django_otp is not present. It can be "
        f"installed by running 'pip install django_otp qrcode'." 
    )

INSTALLED_APPS.extend(['django_otp','django_otp.plugins.otp_totp'])

class OTPPluginConfig(PluginConfig):
    name = 'netbox_otp_plugin'
    verbose_name = 'OTP Login'
    description = 'OTP Login plugin'
    version = '1.0.3'
    author = 'Andrey Shalashov'
    author_email = 'avshalashov@yandex.ru'
    base_url = 'otp'
    required_settings = []
    default_settings = {
        'otp_required': True
    }
    middleware = [
        'django_otp.middleware.OTPMiddleware',
        'netbox_otp_plugin.middleware.RedirectToOTPMiddleware'
    ]

config = OTPPluginConfig