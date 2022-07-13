from unicodedata import name
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
"""  """

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def campeones(request):
    campeones = Campeon.objects.all()
    return render(context={'campeones': campeones},request=request, template_name='AppCoder/campeones.html')
 
def items(request):
    items = Item.objects.all()
    return render(context={'items': items},request=request, template_name='AppCoder/items.html')

def posteos(request):
    posteos = Posteo.objects.all()
    return render(context={'posteos': posteos},request=request, template_name='AppCoder/posteos.html')

def buscar_campeon(request):
    if request.GET:
        campeones = Campeon.objects.filter(nombre=request.GET.get('nombre')).all() # de los campeones obtener solamente aquellos en los que el nombre que viene en el request (url) sea igual que alguno que tengamos en la base de datos
    return render(context={'campeones': campeones},request=request, template_name='AppCoder/campeones.html')

def formulario_posteo(request):
    return render(request=request, template_name='AppCoder/insert_post.html')

def insertar_posteo(request):
    if request.POST:
        posteo = Posteo(
                titulo = request.POST.get('titulo'),
                cuerpo = request.POST.get('cuerpo'),
                autor = request.POST.get('autor'),
                fecha = request.POST.get('fecha')
            )
        posteo.save()
    return render(request=request, template_name='AppCoder/posteos.html',context={'posteos': [posteo]})
