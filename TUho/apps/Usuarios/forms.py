from django import forms
from django.forms import ModelForm
from .models import Usuario


class InformacionPersonal(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'type':"text",'name':"name", 'class':"input", 'required':'true', 'id': 'inputName'}),
            'last_name' : forms.TextInput(attrs={'type':"text",'name':"name", 'class':"input", 'required':'true', 'id': 'inputLastName'}),
            'carnet' : forms.TextInput(attrs={'type':"text",'name':"name", 'class':"input", 'required':'true', 'id': 'inputCi'}),
            'email': forms.EmailInput(attrs={'type':"text",'name':"email", 'class':"input", 'required':'true', 'id': 'inputEmail'}),
            'telefono' : forms.TextInput(attrs={'type':"text",'name':"phone", 'class':"input", 'required':'true', 'id': 'inputNt'}),
            'direccion' : forms.Textarea(attrs={'name':"message", 'class':"input", 'required':'true', 'id': 'inputText'}),
        }


