from setuptools import find_packages, setup

setup(
    name='otp-plugin',
    version='0.0.1',
    description='An OTP Login NetBox plugin',
    url='https://github.com/k1nky/netbox-otp-plugin',
    author='Andrey Shalashov',
    license='Apache 2.0',
    install_requires=['qrcode', 'django-otp'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
