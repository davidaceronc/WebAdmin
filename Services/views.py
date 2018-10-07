from django.shortcuts import render
from .models import Service, Location, MissingItem, Office, SQLQuery
#from .forms import ServicioForm, ConsultaForm


def pagina_inicio(request):
    return render(request, 'base.html')

def nuevo_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'base.html')

    else: 
        form = ServicioForm()
        return render(request, 'base.html', {'form':form, 'numero':21})

def nueva_consulta(request, pk):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Servicio = Servicio.objects.get(id=pk)
            post.save()
            return render(request, 'base.html')

    else: 
        form = ConsultaForm()
        return render(request, 'base.html', {'form':form, 'id':pk})