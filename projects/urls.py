from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectsView.as_view(), name="projects"),
    path('create/', views.CreateProject.as_view(), name="create_project"),
    path('<int:pk>/', views.ProjectDetail.as_view(), name="project"),
    path('<int:pk>/tasks/create', views.CreateTask.as_view(), name="create_task"),
    path('<int:project_id>/tasks/<int:pk>', views.TaskDetail.as_view(), name="task"),
]
