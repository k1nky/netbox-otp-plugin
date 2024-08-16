from django_otp.plugins.otp_totp.models import TOTPDevice
# from netbox.models.features import ChangeLoggingMixin
from utilities.querysets import RestrictedQuerySet
from django.urls import reverse


class Device(TOTPDevice):
    class Meta:
        proxy = True
    objects = RestrictedQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('plugins:netbox_otp_plugin:device', args=[self.pk])
