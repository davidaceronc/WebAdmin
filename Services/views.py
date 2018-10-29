from django.shortcuts import render,redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Service, Location, MissingItem, Office, SQLQuery
from .forms import ServiceForm, MissingItemForm, LocationForm, OfficeForm

def base_service(request):
    return render(request, "Services/base.html")

# Servicio
class ServiceListView(ListView):
    model = Service
    template_name = "Services/service_list.html"

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service-list')


# Catalogo de objetos perdidos
def item_configure(request,service_id):
    items = MissingItem.objects.all().filter(Service=Service.objects.get(pk=service_id))
    return render(request, 'Services/item_configure.html', {'object_list':items,'service_id':service_id})

def item_create(request,service_id):
    success_url = reverse_lazy('service-list')
    if request.method == 'POST':
        form = MissingItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Service = Service.objects.get(pk=service_id)
            post.save()
            return render(request, 'Services/item_form.html')

    else: 
        form = MissingItemForm()
        return render(request, 'Services/item_form.html', {'form':form, 'service_id':service_id})

class MissingItemListView(ListView):
    model = MissingItem
    template_name = "Services/item_detail.html"

class MissingItemCreateView(CreateView):
    model = MissingItem
    fields = '__all__'
    #form_class = MissingItemForm
    #template_name = "Services/item_form.html"

class MissingItemUpdateView(UpdateView):
    model = MissingItem
    fields = '__all__'
    #form_class = MissingItemForm
    #template_name = "Services/item_form.html"

class MissingItemDeleteView(DeleteView):
    model = MissingItem
    success_url = reverse_lazy('service-list')


# Directorio de dependencias
def office_configure(request,service_id):
    offices = Office.objects.all().filter(Service=Service.objects.get(pk=service_id))
    return render(request, 'Services/office_configure.html', {'object_list':offices,'service_id':service_id})

def office_create(request,service_id):
    success_url = reverse_lazy('service-list')
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Service = Service.objects.get(pk=service_id)
            post.save()
            return render(request, 'Services/office_form.html')

    else: 
        form = OfficeForm()
        return render(request, 'Services/office_form.html', {'form':form, 'service_id':service_id})

class OfficeListView(ListView):
    model = Office
    template_name = "Services/office_list.html"

class OfficeCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class OfficeUpdateView(UpdateView):
    model = Office
    success_url = reverse_lazy('service-list')
    form_class = OfficeForm
    template_name = "Services/office_form.html"

class OfficeDeleteView(DeleteView):
    model = Office
    success_url = reverse_lazy('service-list')

# Mapa de bloques
def location_configure(request,service_id):
    locations = Location.objects.all().filter(Service=Service.objects.get(pk=service_id))
    return render(request, 'Services/location_configure.html', {'object_list':locations,'service_id':service_id})

def location_create(request,service_id):
    success_url = reverse_lazy('service-list')
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Service = Service.objects.get(pk=service_id)
            post.save()
            return render(request, 'Services/location_form.html')

    else: 
        form = LocationForm()
        return render(request, 'Services/location_form.html', {'form':form, 'service_id':service_id})

class LocationListView(ListView):
    model = Location
    template_name = "Services/location_list.html"

class LocationCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class LocationUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class LocationDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service-list')


# Consulta SQL
def query_configure(request,service_id):
    query = SQLQuery.objects.get(Service=Service.objects.get(pk=service_id))
    return render(request, 'Services/query_form.html', {'object_list':query,'service_id':service_id})

class SQLQueryListView(ListView):
    model = SQLQuery
    template_name = "Services/query_list.html"









