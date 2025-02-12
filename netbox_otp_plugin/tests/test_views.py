from utilities.testing import ViewTestCases
from netbox_otp_plugin.models import Device
from users.models import User


class DeviceTestCase(ViewTestCases.ListObjectsViewTestCase,
                     ViewTestCases.GetObjectViewTestCase,
                     ViewTestCases.DeleteObjectViewTestCase,
                     ViewTestCases.CreateObjectViewTestCase):

    model = Device

    def _get_base_url(self):
        """
        Return the base format for a URL for the test's model. Override this to test for a model which belongs
        to a different app (e.g. testing Interfaces within the virtualization app).
        """
        return '{}:{}:{}_{{}}'.format('plugins', self.model._meta.app_label, self.model._meta.model_name)

    @classmethod
    def setUpTestData(cls):
        users = (
            User(username='user_a'),
            User(username='user_b'),
            User(username='user_c')
        )
        User.objects.bulk_create(users)
        devices = (
            Device(name='device-1', user=users[0]),
            Device(name='device-2', user=users[1])
        )
        Device.objects.bulk_create(devices)

        cls.form_data = {
            'name': 'device-3',
            'user': users[0].pk,
            'digits': 6,
        }

    def test_export_objects(self):
        pass
