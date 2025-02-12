from utilities.testing.base import TestCase

from django.urls import reverse
from rest_framework import status


class TestRedirectToOTPMiddleware(TestCase):

    def test_login(self):
        url = reverse('login')
        redirect_to = reverse('plugins:netbox_otp_plugin:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.url, redirect_to)

    def test_not_login(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
