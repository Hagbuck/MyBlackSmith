from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import Task

class TasksList(LoginRequiredMixin, generic.ListView):
    template_name = "tasks/tasks.html"
    context_object_name = 'task_list'

    def get_queryset(self):
        return Task.objects.all().filter(user = self.request.user.id)

class CreateTask(LoginRequiredMixin, generic.CreateView):
    template_name = 'tasks/create_task.html'
    model = Task
    fields = ['name', 'text', 'project']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('tasks:tasks'))
        #return HttpResponseRedirect(reverse('projects:project', kwargs={'pk': self.kwargs['pk']}))

class TaskDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'tasks/task.html'
    model = Task

    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user.id)

class UpdateTask(LoginRequiredMixin, generic.UpdateView):
    template_name = 'tasks/update_task.html'
    model = Task
    fields = ['name', 'text', 'project']

    def get_queryset(self):
        return Task.objects.all().filter(user = self.request.user.id)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('tasks:task', kwargs={'pk': self.kwargs['pk']}))

class DeleteTask(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:tasks')

    def get_queryset(self):
        return Task.objects.all().filter(user = self.request.user.id)