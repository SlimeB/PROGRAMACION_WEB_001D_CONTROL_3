from django.shortcuts import get_object_or_404
from main.models import Producto
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from rest_framework.views import APIView

# Create your views here.
class producto_create(APIView):
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class producto_update(APIView):
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def producto_read(request, id):
    if request.method == "GET":
        objeto = get_object_or_404(Producto, idProduco = id)
        serializer = ProductoSerializer(objeto)
        return Response(serializer.data)

@api_view(["GET"])
def producto_read_all(request):
    if request.method == "GET":
        lista = Producto.objects.all()
        serializer = ProductoSerializer(lista, many = True)
        return Response(serializer.data)

@api_view(["DELETE"])
def producto_delete(request, id):
    if request.method == "DELETE":
        try:
            Producto.objects.get(idProduco = id).delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)