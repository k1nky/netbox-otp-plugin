from django.core.management.base import BaseCommand, CommandError

from users.models import User

try:
    from django_otp.plugins.otp_totp.models import TOTPDevice
    from django_otp import user_has_device
except ModuleNotFoundError:
    raise CommandError('django_otp module does not exist')

class Command(BaseCommand):

    help = 'Reset a TOTP device for specified user'

    def add_arguments(self, parser):
        parser.add_argument('user', type=str)

    def handle(self, *args, **options):
        username = options['user']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f"User {username} does not exist")
        if user_has_device(user):
            device = TOTPDevice.objects.filter(user_id=user.id)
            device.delete()
