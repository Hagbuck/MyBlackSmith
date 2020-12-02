from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework import permissions
from accounts.serializers import UserSerializer

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class AccountView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']  
    template_name = "accounts/index.html"
    success_url = reverse_lazy('accounts:account')

    def get_object(self):
        return self.request.user

#######################
#         API         #
#######################

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'head', 'options', 'put']


    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.all().filter(id = self.request.user.id)