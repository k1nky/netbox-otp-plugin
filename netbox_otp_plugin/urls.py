from django.urls import path

from . import views

app_name = 'otp'
urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name='device_list'),
    path('devices/add/', views.DeviceEditView.as_view(), name='device_add'),
    path('devices/<int:pk>/', views.DeviceView.as_view(), name='device'),
    path('devices/edit/<int:pk>/', views.DeviceEditView.as_view(), name='device_edit'),
    path('devices/delete/<int:pk>/', views.DeviceDeleteView.as_view(), name='device_delete'),
    path('', views.OTPLoginView.as_view(), name='login')
]
