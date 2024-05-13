from setuptools import find_packages, setup

setup(
    name='netbox_otp_plugin',
    version='1.0.8',
    description='OTP Login NetBox plugin',
    url='https://github.com/marco012024/netbox-otp-plugin',
    author='Andrey Shalashov',
    author_email='avshalashov@yandex.ru',
    license='Apache 2.0',
    keywords='netbox otp login plugin',
    install_requires=['qrcode', 'django-otp'],
    packages=find_packages(),
    package_data={
        "netbox_otp_plugin": [
            "templates/*",
            "management/commands/*"
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
