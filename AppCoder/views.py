from unicodedata import name
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppCoder.forms import CampeonFormulario, PosteoFormulario

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
    if request.method == 'POST':
    
        form= PosteoFormulario(request.POST)
        print(form)
        
        if form.is_valid:
            info= form.cleaned_data
            titulo=info["titulo"]
            cuerpo=info["cuerpo"]
            autor=info["autor"]
            fecha=info["fecha"]
            posteo= Posteo (titulo=titulo, cuerpo=cuerpo, autor=autor, fecha=fecha)
            posteo.save()
            return render(request,'AppCoder/inicio.html')        

    else:
            form=PosteoFormulario()
    return render(request, "AppCoder/insert_post.html", {"form":form})


