from django import forms

class CursoFormulario(forms.Form):

    #Especificar los campos#ACTUALIZAR
    curso = forms.CharField()
    camada = forms.IntegerField()


#class ProfesorFormulario(forms.Form):   #ACTUALIZAR
#    nombre= forms.CharField(max_length=30)
#    apellido= forms.CharField(max_length=30)
#    email= forms.EmailField()
#    profesion= forms.CharField(max_length=30)