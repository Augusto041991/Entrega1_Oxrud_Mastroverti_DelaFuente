from django.shortcuts import render
from django.http.request import QueryDict
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from App_intermedia.models import Ventas, Contabilidad, Produccion


# Create your views here.


def ventas(request):

      ventas =  Ventas(nombre="Fabian", sueldo="100000", email="fabian@coder.com")
      ventas.save()
      documentoDeTexto = f"--->Nombre: {ventas.nombre}   Sueldo: {ventas.sueldo}    email: {ventas.email}"


      return HttpResponse(documentoDeTexto)

def contabilidad(request):

      contabilidad =  Contabilidad(nombre="Hector", sueldo="80000", email="Hector@coder.com")
      contabilidad.save()
      documentoDeTexto = f"--->Nombre: {contabilidad.nombre}   Sueldo: {contabilidad.sueldo}    email: {contabilidad.email}"


      return HttpResponse(documentoDeTexto)


def produccion(request):

      produccion =  Produccion(nombre="Maria", sueldo="50000", email="Maria@coder.com")
      produccion.save()
      documentoDeTexto = f"--->Nombre: {produccion.nombre}   Sueldo: {produccion.sueldo}    email: {produccion.email}"


      return HttpResponse(documentoDeTexto)


def test(request):

      return render(request, "App_intermedia/template.html")