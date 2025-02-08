from base64 import b32encode
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.models import DeviceManager
from utilities.querysets import RestrictedQuerySet
from django.urls import reverse


class DeviceQuerySet(RestrictedQuerySet, DeviceManager):
    pass


class MyDeviceQuerySet(RestrictedQuerySet, DeviceManager):
    def restrict(self, user, action='view'):
        """
        Filter the QuerySet to return only objects on which the specified user has been granted the specified
        permission.

        :param user: User instance
        :param action: The action which must be permitted (e.g. "view" for "dcim.view_site"); default is 'view'
        """
        return self.devices_for_user(user)


class Device(TOTPDevice):

    class Meta:
        proxy = True
    objects = DeviceQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('plugins:netbox_otp_plugin:device', args=[self.pk])

    @property
    def base32_key(self):
        return b32encode(self.bin_key).decode()


class MyDevice(Device):
    """
    Proxy model for users to manage their own devices.
    """

    class Meta:
        proxy = True
    objects = MyDeviceQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('plugins:netbox_otp_plugin:mydevice', args=[self.pk])
