from setuptools import find_packages, setup

setup(
    name='netbox_otp_plugin',
    version='1.0.0',
    description='An OTP Login NetBox plugin',
    url='https://github.com/k1nky/netbox-otp-plugin',
    author='Andrey Shalashov',
    author_email='avshalashov@yandex.ru',
    license='Apache 2.0',
    install_requires=['qrcode', 'django-otp'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
