from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProjectSerializer

from .models import Project

class ProjectsView(LoginRequiredMixin, generic.ListView):
    template_name = 'projects/projects.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.all().filter(user = self.request.user.id)

class CreateProject(LoginRequiredMixin, generic.CreateView):
    template_name = 'projects/create.html'
    model = Project
    fields = ['name', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('projects:projects'))

class ProjectDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user.id)

class UpdateProject(LoginRequiredMixin, generic.UpdateView):
    template_name = "projects/update.html"
    model = Project
    fields = ['name', 'description']

    def get_queryset(self):
        return Project.objects.all().filter(user = self.request.user.id)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('projects:project', kwargs={'pk': self.kwargs['pk']}))

class DeleteProject(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy('projects:projects')

    def get_queryset(self):
        return Project.objects.all().filter(user = self.request.user.id)



#######################
#         API         #
#######################

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return Project.objects.all()
        return Project.objects.all().filter(id = self.request.user.id)