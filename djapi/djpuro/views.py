from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import categoria

# Create your views here.
def categoria_list(request):
    MAX_OBJECTS= 20
    cat= categoria.objects.all()[:MAX_OBJECTS]
    data= {'results':list(cat.values("descripcion","activo"))}
    return JsonResponse(data)
def categoria_detalle(request,pk):
    cat= get_object_or_404(categoria,pk=pk)
    data={
        "results": {
            "descripcion": cat.descripcion,
            "activo" : cat.activo
        }
    }
    return JsonResponse(data)
