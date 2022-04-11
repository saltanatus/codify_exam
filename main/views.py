from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from . import forms
from .models import Worker, Document, Project, Membership, Customer, VIPCustomer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class WorkerListView(ListView):
    model = Worker
    template_name = 'worker_list.html'

    def get_queryset(self):
        q = self.request.GET.get('query')
        if q:
            return self.model.objects.filter(fullname__icontains = q)
        else:
            return self.model.objects.all()


class WorkerCreateView(LoginRequiredMixin, CreateView):
    form_class = forms.WorkerForm
    template_name = 'worker_form.html'

class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'worker_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['membership'] = Membership.objects.filter(worker=self.get_object())
        return context

class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'worker_delete.html'
    success_url = reverse_lazy('worker_list')

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().delete(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('worker_list'))


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    form_class = forms.WorkerForm
    model = Worker
    template_name = 'worker_form.html'
