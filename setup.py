from setuptools import find_packages, setup

setup(
    name='netbox_otp_plugin',
    version='1.3.1',
    description='OTP Login NetBox plugin',
    url='https://github.com/k1nky/netbox-otp-plugin',
    author='Andrey Shalashov',
    author_email='avshalashov@yandex.ru',
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    keywords='netbox otp login plugin',
    install_requires=[
        'qrcode',
        'django-otp',
        'django-qr-code',
    ],
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
