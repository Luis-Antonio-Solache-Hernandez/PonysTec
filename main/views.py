from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from .forms import ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required


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
        formulario = ProductoForm(request.POST)
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
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos')
    return render_to_response('formulario.html', {
        'formulario': formulario,
        'titulo': 'Editar un producto',
    }, RequestContext(request))
