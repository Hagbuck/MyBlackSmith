from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

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
