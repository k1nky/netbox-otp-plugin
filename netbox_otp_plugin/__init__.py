import importlib
from django.core.exceptions import ImproperlyConfigured

from netbox.plugins import PluginConfig
import netbox.settings as netbox_settings

if importlib.util.find_spec('django_otp') is None:
    raise ImproperlyConfigured(
        "netbox_otp_plugin is enabled but django_otp is not present. It can be "
        "installed by running 'pip install django_otp qrcode'."
    )


class OTPPluginConfig(PluginConfig):
    name = 'netbox_otp_plugin'
    verbose_name = 'OTP Login'
    description = 'OTP Login plugin'
    version = '1.3.3'
    author = 'Andrey Shalashov'
    author_email = 'avshalashov@yandex.ru'
    min_version = '4.0.0'
    max_version = '4.3.99'
    django_apps = [
        'django_otp',
        'django_otp.plugins.otp_totp',
        'qr_code'
    ]
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

        parsed_netbox_version = tuple(map(int, netbox_version.split('.')))
        # the AUTH_EXEMPT_PATHS setting has been removed since NetBox v4.1.0
        if parsed_netbox_version < (4, 1, 0):
            # the plugin login URL must be exempt from authentication
            auth_exempt_paths = netbox_settings.AUTH_EXEMPT_PATHS + (f'/{netbox_settings.BASE_PATH}plugins/otp',)
            setattr(netbox_settings, 'AUTH_EXEMPT_PATHS', auth_exempt_paths)


config = OTPPluginConfig
