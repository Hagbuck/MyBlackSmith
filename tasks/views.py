from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import action
from .serializers import TaskSerializer

from .models import Task, Comment
from .form import UpdateTaskForm

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
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()

        print( task.project )
        if task.project != None:
            return HttpResponseRedirect(reverse('projects:project', kwargs = { 'pk' : task.project.id }))
        else:
            return HttpResponseRedirect(reverse('tasks:tasks'))

class TaskDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'tasks/task.html'
    model = Task

    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user.id)

class UpdateTask(LoginRequiredMixin, generic.UpdateView):
    template_name = 'tasks/update_task.html'
    model = Task
    form_class = UpdateTaskForm

    def get_form_kwargs(self):
        """
        Pass the request to the form class. Necessary to filter label that belong to the current user
        """
        kwargs = super(UpdateTask, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_queryset(self):
        return Task.objects.all().filter(user = self.request.user.id)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return HttpResponseRedirect(reverse('tasks:task', kwargs={'pk': self.kwargs['pk']}))

class DeleteTask(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:tasks')

    def get_queryset(self):
        return Task.objects.all().filter(user = self.request.user.id)


def comment(request, task_id):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, pk = task_id, user = request.user)
        text = request.POST['text']
        
        if not text:
            return HttpResponse("Text can't be empty", status=400)

        com = Comment(task = task, user = request.user, text = text)
        com.save()
        return HttpResponseRedirect(reverse('tasks:task', args=(task.id,)))
    else:
        return HttpResponse('Unauthorized', status=401)


#######################
#         API         #
#######################

# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        return Task.objects.all().filter(user = self.request.user)


    # @action(detail = True, methods = ['POST'])
    # def comment(self, request, pk = None):
    #     task = get_object_or_404(Task, pk = pk, user = request.user.id)

    #     serializer = TaskSerializer(data = request.data)

    #     text = serializer.date['text']

    #     if serializer.is_valid() and text:
    #         com = Comment(task = taks, user = request.user, text = text)
    #         com.save()
    #         return Response(serializer.data)

    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)