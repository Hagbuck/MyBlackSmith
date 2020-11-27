from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import Label

class LabelsList(LoginRequiredMixin, generic.ListView):
    template_name = "labels/labels.html"
    context_object_name = "label_list"

    def get_queryset(self):
        return Label.objects.all().filter(user = self.request.user.id)

class CreateLabel(LoginRequiredMixin, generic.CreateView):
    template_name = 'labels/create_label.html'
    model = Label
    fields = ['name', 'color', 'project']

    def form_valid(self, form):
        label = form.save(commit=False)
        label.user = self.request.user
        label.save()
        return HttpResponseRedirect(reverse('labels:labels'))


class LabelDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'labels/label.html'
    model = Label

    def get_queryset(self):
        return Label.objects.all().filter(user = self.request.user.id)

class UpdateLabel(LoginRequiredMixin, generic.UpdateView):
    template_name = 'labels/update_label.html'
    model = Label
    fields = ['name', 'color', 'project']

    def get_queryset(self):
        return Label.objects.all().filter(user = self.request.user.id)

    def form_valid(self, form):
        label = form.save(commit=False)
        label.user = self.request.user
        label.save()
        return HttpResponseRedirect(reverse('labels:label', kwargs={'pk': self.kwargs['pk']}))

class DeleteLabel(LoginRequiredMixin, generic.DeleteView):
    model = Label
    success_url = reverse_lazy('labels:labels')

    def get_queryset(self):
        return Label.objects.all().filter(user = self.request.user.id)
