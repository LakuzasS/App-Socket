from django import forms
from .models import Capteur, Donnee


class CapteurForm(forms.ModelForm):
    class Meta:
        model = Capteur
        fields = ['id', 'nom', 'piece', 'emplacement']


class DonneeForm(forms.ModelForm):
    class Meta:
        model = Donnee
        fields = ['capteur', 'timestamp', 'temperature', 'presence', 'nombre_individus']