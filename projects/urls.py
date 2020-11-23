from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectsView.as_view(), name="projects"),
    path('create/', views.CreateProject.as_view(), name="create_project"),
    path('<int:pk>/', views.ProjectDetail.as_view(), name="project"),
    path('<int:pk>/update', views.UpdateProject.as_view(), name="update_project"),
]
