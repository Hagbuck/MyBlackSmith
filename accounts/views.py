from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class AccountView(LoginRequiredMixin, generic.DetailView):
    model = User
    fields = ['username', 'firstname', 'lastname', 'email']
    template_name = "accounts/index.html"

    def get_object(self):
        return self.request.user