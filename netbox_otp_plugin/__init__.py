import importlib
from django.core.exceptions import ImproperlyConfigured

from netbox.plugins import PluginConfig
import netbox.settings as netbox_settings

if importlib.util.find_spec('django_otp') is None:
    raise ImproperlyConfigured(
        f"netbox_otp_plugin is enabled but django_otp is not present. It can be "
        f"installed by running 'pip install django_otp qrcode'." 
    )

netbox_settings.INSTALLED_APPS.extend(['django_otp','django_otp.plugins.otp_totp'])
# the plugin login URL must be exempt from authentication
netbox_settings.AUTH_EXEMPT_PATHS = netbox_settings.AUTH_EXEMPT_PATHS + (f'/{netbox_settings.BASE_PATH}plugins/otp',)

class OTPPluginConfig(PluginConfig):
    name = 'netbox_otp_plugin'
    verbose_name = 'OTP Login'
    description = 'OTP Login plugin'
    version = '1.1.0'
    author = 'Andrey Shalashov'
    author_email = 'avshalashov@yandex.ru'
    base_url = 'otp'
    required_settings = []
    default_settings = {
        'otp_required': True,
        'issuer': 'Netbox'
    }
    middleware = [
        'django_otp.middleware.OTPMiddleware',
        'netbox_otp_plugin.middleware.RedirectToOTPMiddleware'
    ]

    @classmethod
    def validate(cls, user_config, netbox_version):
        super().validate(user_config, netbox_version)
        # django_otp provides OTP_TOTP_ISSUER. Set it here to avoid
        # making any changes in the original settings.py
        setattr(netbox_settings, 'OTP_TOTP_ISSUER', user_config.get('issuer'))


config = OTPPluginConfig