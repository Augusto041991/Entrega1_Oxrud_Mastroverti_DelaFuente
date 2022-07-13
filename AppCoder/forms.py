from django import forms



class CampeonFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField(max_length=50)
    lore = forms.TimeField()
    imagen = forms.ImageField()



class PosteoFormulario(forms.Form):   
    titulo = forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=50)
    autor = forms.EmailField()
    fecha = forms.DateTimeField()