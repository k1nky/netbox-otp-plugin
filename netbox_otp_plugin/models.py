from base64 import b32encode
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.models import DeviceManager
from utilities.querysets import RestrictedQuerySet
from django.urls import reverse


class DeviceQuerySet(RestrictedQuerySet, DeviceManager):
    pass


class Device(TOTPDevice):

    class Meta:
        proxy = True
    objects = DeviceQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('plugins:netbox_otp_plugin:device', args=[self.pk])

    @property
    def base32_key(self):
        return b32encode(self.bin_key).decode()
