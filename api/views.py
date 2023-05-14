from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from tienda.models import Categoria,Producto
from .serializers import (
    CategoriaSerializer,
    ProductoSerializer
)

class IndexView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer    

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Categoria.objects.all()
    lookup_url_kwarg = 'categoria_id'
    serializer_class = CategoriaSerializer


class ProductoView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer    

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Producto.objects.all()
    lookup_url_kwarg = 'producto_id'
    serializer_class = ProductoSerializer   