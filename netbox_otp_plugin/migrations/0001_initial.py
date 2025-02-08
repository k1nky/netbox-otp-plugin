from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otp_totp', '0003_add_timestamps'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDevice',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('otp_totp.totpdevice',),
        ),
    ]
