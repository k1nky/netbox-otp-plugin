from django.http import Http404, HttpResponseRedirect

class RedirectToOTPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/login'):
                return HttpResponseRedirect('/plugins/otp/')
        if request.path.startswith('/admin/login'):
                return HttpResponseRedirect('/plugins/otp/')

        return self.get_response(request)
