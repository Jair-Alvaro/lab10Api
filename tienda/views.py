from django.shortcuts import render,get_object_or_404

from .models import Categoria,Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.all()
    category_list = Categoria.objects.all()

    context = {
        'product_list': product_list,
        'category_list': category_list
        }
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    context = {
            'producto': producto,
        }
    return render(request,'producto.html',context )

def productocat(request, producto_id,categoria_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    context = {
            'producto': producto,
            'categoria': categoria
        }
    return render(request,'producto.html',context )

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    product_list = categoria.producto_set.all()
    category_list = Categoria.objects.all()
    context = {
        'product_list': product_list,
        'category_list': category_list
        }
    return render(request,'index.html',context)
