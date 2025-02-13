from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from estoque.forms import CustomUserCreationForm

class LoginPageView(LoginView):
   redirect_authenticated_user = True
   template_name = 'login.html'

class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
