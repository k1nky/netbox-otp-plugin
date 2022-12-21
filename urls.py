from django.urls import path
from django_otp.forms import OTPAuthenticationForm

from . import views

app_name = 'otp'
urlpatterns = [
    path('', views.OTPLoginView.as_view(authentication_form=OTPAuthenticationForm), name='otp')
]
