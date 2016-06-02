from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.http import HttpResponse
from .forms import ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required
import csv
import json


def index(request):
    return render_to_response('index.html', {
        }, RequestContext(request))


def pagina2(request):
    return render_to_response('pagina2.html', {
        }, RequestContext(request))


def Productos(request):
    productos = Producto.objects.all().order_by('tipo', '-precio')
    return render_to_response('productos.html', {
        'productos': productos
    }, RequestContext(request))


@login_required
def creaProducto(request):
    formulario = ProductoForm()
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES,)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos')
    return render_to_response('formulario.html', {
        'formulario': formulario,
        'titulo': 'Alta de un producto',
    }, RequestContext(request))


@login_required
def editarProducto(request, pk):
    producto = Producto.objects.get(id=pk)
    formulario = ProductoForm(instance=producto)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos')
    return render_to_response('formulario.html', {
        'formulario': formulario,
        'titulo': 'Editar un producto',
    }, RequestContext(request))


@login_required
def reporte(request): 
    data = Producto.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Archivo.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Tipo', 'Precio', 'Presentacion'])
    for ele in data:
        writer.writerow([ele.nombre, ele.get_tipo_display(), ele.precio, ele.presentacion])
    return response


def mijson(request):
    data = {}
    data["1234"] = 1234
    data["ale"] = "ama a Diego"
    data["diego"] = "ama a Fil"
    data["fil"] = "ama a Dani"
    data["dani"] = "quiere a Ale"
    vjson = json.JSONEncoder().encode(data)
    return HttpResponse(vjson, content_type='application/json')
