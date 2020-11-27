from django.urls import path

from . import views

app_name = 'labels'

urlpatterns = [
    path('', views.LabelsList.as_view(), name="labels"),
    path('create', views.CreateLabel.as_view(), name="create_label"),
    path('<int:pk>', views.LabelDetail.as_view(), name="label"),
    path('<int:pk>/update', views.UpdateLabel.as_view(), name="update_label"),
    path('<int:pk>/delete', views.DeleteLabel.as_view(), name="delete_label"),
]