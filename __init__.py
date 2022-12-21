from extras.plugins import PluginConfig
from netbox.settings import INSTALLED_APPS


if importlib.util.find_spec('django_otp') is None:
    raise ImproperlyConfigured(
        f"netbox-otp-plugin is enabled but django_otp is not present. It can be "
        f"installed by running 'pip install django_otp qrcode'." 
    )
INSTALLED_APPS.extend(['django_otp','django_otp.plugins.otp_totp'])

class OTPLoginPluginConfig(PluginConfig):
    name = 'otp_login'
    verbose_name = 'OTP Login'
    description = 'OTP Login plugin'
    version = '0.0.1'
    author = 'Andrey Shalashov'
    author_email = 'avshalashov@yandex.ru'
    base_url = 'otp'
    required_settings = []
    default_settings = {
    }
    middleware = [
        'django_otp.middleware.OTPMiddleware',
        'otp_login.middleware.RedirectToOTPMiddleware'
    ]

config = OTPLoginPluginConfig