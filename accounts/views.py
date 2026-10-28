from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

# Create your views here.
class CustomLoginView(LoginView):
    template_name = "accountsTemplates/login.html"

class CustomLogoutView(LogoutView):
    template_name = "accountsTemplates/logout.html"