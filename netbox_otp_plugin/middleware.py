from django.http import HttpResponseRedirect
from django.urls import reverse


class RedirectToOTPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/login'):
            return HttpResponseRedirect(reverse('plugins:netbox_otp_plugin:login'))

        return self.get_response(request)
