from django.http import Http404, HttpResponseRedirect

class RedirectToOTPMiddleware:
    """
    If LOGIN_REQUIRED is True, redirect all non-authenticated users to the login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Redirect unauthenticated requests (except those exempted) to the login page if LOGIN_REQUIRED is true
        print(request.path)
        if request.path.startswith('/login'):
                # login_url = f'{settings.LOGIN_URL}?next={parse.quote(request.get_full_path_info())}'
                return HttpResponseRedirect('/plugins/otp')

        return self.get_response(request)
