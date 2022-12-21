from django.contrib.auth.views import LoginView

class OTPLoginView(LoginView):
    template_name = 'otp_login.html'
