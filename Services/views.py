from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Service, Location, MissingItem, Office, SQLQuery
from .forms import ServiceForm


def base_service(request):
    return render(request, "Services/base.html")

class ServicesCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class ServicesListView(ListView):
    model = Service
    template_name = "Services/service_list.html"

class ServicesUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class ServicesDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('list-services')