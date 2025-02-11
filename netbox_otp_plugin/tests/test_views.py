from utilities.testing import ViewTestCases
from netbox_otp_plugin.models import Device
from users.models import User


class MyDeviceTestCase(ViewTestCases.ListObjectsViewTestCase,
                       ViewTestCases.GetObjectViewTestCase):

    model = Device

    def _get_base_url(self):
        """
        Return the base format for a URL for the test's model. Override this to test for a model which belongs
        to a different app (e.g. testing Interfaces within the virtualization app).
        """
        return '{}:{}:{}_{{}}'.format('plugins', self.model._meta.app_label, self.model._meta.model_name)

    @classmethod
    def setUpTestData(cls):
        user_a = User(username='user_a')
        user_a.save()
        user_b = User(username='user_b')
        user_b.save()
        Device.objects.create(name='device-1', user=user_a)
        Device.objects.create(name='device-2', user=user_b)

    def test_export_objects(self):
        pass
