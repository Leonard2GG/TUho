from django import forms
from django.forms import ModelForm
from .models import Noticias

# Formulario de Noticias
class CrearNoticiasForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    class Meta:
        model = Noticias
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'type':"text",'name':"titulo", 'class':"input", 'required':'true'}),
            'cuerpo' : forms.Textarea(attrs={'name':"cuerpo", 'class':"input", 'required':'true', 'id': 'inputText'}),
        }