from django.urls import path
from App_intermedia import views


urlpatterns = [
   
    #path('', views.inicio, name="Inicio"), #esta era nuestra primer view REVISAR
    path('ventas', views.ventas, name="Ventas"),
    path('contabilidad', views.contabilidad, name="Contabilidad"),
    path('produccion', views.produccion, name="Produccion"),
    path('test', views.test, name="Test")

    ]

    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    #path('buscar/', views.buscar),
