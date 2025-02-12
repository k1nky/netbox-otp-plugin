from utilities.testing import ViewTestCases
from netbox_otp_plugin.models import Device
from users.models import User
from users.models import ObjectPermission
from core.models import ObjectType
from django.test import override_settings
from utilities.testing.utils import post_data


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
            'user': users[0].pk
        }

    def test_export_objects(self):
        pass

    @override_settings(EXEMPT_VIEW_PERMISSIONS=['*'], EXEMPT_EXCLUDE_MODELS=[])
    def test_create_object_with_constrained_permission(self):

        # Assign constrained permission
        obj_perm = ObjectPermission(
            name='Test permission',
            constraints={'pk': 0},  # Dummy permission to deny all
            actions=['add']
        )
        obj_perm.save()
        obj_perm.users.add(self.user)
        obj_perm.object_types.add(ObjectType.objects.get_for_model(self.model))

        # Try GET with object-level permission
        self.assertHttpStatus(self.client.get(self._get_url('add')), 200)

        # Try to create an object (not permitted)
        initial_count = self._get_queryset().count()
        request = {
            'path': self._get_url('add'),
            'data': post_data(self.form_data),
        }
        self.assertHttpStatus(self.client.post(**request), 200)
        self.assertEqual(initial_count, self._get_queryset().count())  # Check that no object was created

        # Update the ObjectPermission to allow creation
        obj_perm.constraints = {'pk__gt': 0}
        obj_perm.save()

        # Try to create an object (permitted)
        request = {
            'path': self._get_url('add'),
            'data': post_data(self.form_data),
        }
        self.assertHttpStatus(self.client.post(**request), 302)
        # self.assertHttpStatus(self.client.post(**request), 200)
        self.assertEqual(initial_count + 1, self._get_queryset().count())
        instance = self._get_queryset().order_by('pk').last()
        self.assertInstanceEqual(instance, self.form_data, exclude=self.validation_excluded_fields)

