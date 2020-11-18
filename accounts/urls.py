from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountView.as_view(), name = 'account'),
    path('signup/', views.SignupView.as_view(), name = 'signup'),
]
