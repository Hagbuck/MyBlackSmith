from django.urls import path

from . import views

app_name = 'chess'

urlpatterns = [
    path('', views.ChessView.as_view(), name='index'),
    path('move/', views.move, name='move')
]