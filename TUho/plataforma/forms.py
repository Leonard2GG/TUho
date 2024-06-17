from django import forms
from django.forms import ModelForm
from .models import Noticias, ConfiguracionGeneral
from django.contrib.auth.models import Group, Permission
from ckeditor.widgets import CKEditorWidget


# Formulario de Noticias
class CrearNoticiasForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    class Meta:
        model = Noticias
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'type':"text",'name':"titulo", 'class':"input", 'required':'true' ,'id': 'inputTitulo'}),
            'imagen_cabecera': forms.FileInput(attrs={'type':"file",'name':"file", 'class':"input", 'id': 'inputImagen'}),
            'resumen': forms.TextInput(attrs={'type':"text",'name':"resumen", 'class':"input", 'required':'true' ,'id': 'inputResumen'}),
            'cuerpo' : CKEditorWidget(),
        }

        
class ConfiguracionEmail(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    class Meta:
        model = ConfiguracionGeneral
        fields = '__all__'
        widgets = {
            'correo' : forms.EmailInput(attrs={'type':"email",'name':"correo", 'class':"input", 'required':'true' ,'id': 'inputCorreo'}),
            'contraseña_correo': forms.TextInput(attrs={'type':"text",'name':"contraseña_correo", 'class':"input", 'id': 'inputContraseña_Correo'}),
        }