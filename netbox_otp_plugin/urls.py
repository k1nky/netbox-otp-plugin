from django.urls import path

from . import views

app_name = 'otp'
urlpatterns = [
    path('', views.OTPLoginView.as_view(), name='otp')
]
