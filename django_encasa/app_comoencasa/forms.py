
from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre...'}))

    apellido = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))

    direccion = forms.CharField(label='Direccion', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su dirección...'}))

    ciudad = forms.CharField(label='Ciudad', max_length=100, initial='CABA', widget=forms.TextInput(attrs={'placeholder': 'Ingrese su ciudad'}))

    zipcode = forms.CharField(label='Codigo Postal', max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su codigo postal...'}))

    nacimiento = forms.DateField(label='Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    
    email = forms.EmailField(label='Mail', widget=forms.EmailInput(attrs={'placeholder': 'minombre@gmail.com...'}))