from django.core.management.base import BaseCommand, CommandError

from users.models import User

try:
    from netbox_otp_plugin.models import Device as TOTPDevice
    import qrcode
except ModuleNotFoundError:
    raise CommandError('django_otp or qrcode module does not exist')


class Command(BaseCommand):

    help = 'Add a TOTP device for specified user'

    def add_arguments(self, parser):
        parser.add_argument('user', type=str)

    def handle(self, *args, **options):
        username = options['user']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f"User {username} does not exist")
        device = TOTPDevice.objects.create(user=user, name=f'{username}-otp')
        qr = qrcode.QRCode()
        qr.add_data(device.config_url)
        qr.print_ascii()
        self.stdout.write(self.style.SUCCESS(f'Created: {str(device)} with key {device.base32_key}'))
