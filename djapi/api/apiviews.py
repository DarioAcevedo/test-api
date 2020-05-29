from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth import authenticate
from .serializer import productoSerializer, categoriaSerializer, subcategoriaSerializer, userSerializer

#crear api rest
""" class ProductoList(APIView):
    def get(self,request):
        prod= Producto.objects.all()[:20]
        data= productoSerializer(prod, many= True).data
        return Response(data)

class ProductoDetalle(APIView):
    def get(self,request,pk):
        prod= get_object_or_404(Producto, pk=pk)
        data= productoSerializer(prod).data
        return Response(data)
 """
class loginView(APIView):
    permission_classes = ()

    def post(self, request):
        username= request.data.get("username")
        password= request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token':user.auth_token.key})
        else:
            return Response({'error':"Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)

class parseFecha(APIView):
    def post(self,request):
        fecha= "hola"
        return Response({'fecha':fecha})