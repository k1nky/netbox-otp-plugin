from django.urls import path
from netbox_otp_plugin.forms import OTPLoginForm

from . import views

app_name = 'otp'
urlpatterns = [
    path('', views.OTPLoginView.as_view(authentication_form=OTPLoginForm), name='otp')
]
