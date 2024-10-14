from django import forms
from .models import Enseignant
from .models import Examen
from .models import Note
from .models import RessourcesUE
from .models import UnitesEnseignement
from .models import Etudiant

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['titre', 'date', 'coefficient']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('examen', 'etudiant', 'note', 'appreciation')

class RessourceForm(forms.ModelForm):
    class Meta:
        model = RessourcesUE
        fields = ['code_ressource', 'nom', 'descriptif', 'coefficient']

class UniteForm(forms.ModelForm):
    class Meta:
        model = UnitesEnseignement
        fields = '__all__'

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'groupe', 'email']

from django import forms

class ChooseStudentForm(forms.Form):
    student_id = forms.ChoiceField(label='Choisir l\'étudiant', choices=())

    def __init__(self, *args, **kwargs):
        students = kwargs.pop('students', [])
        super(ChooseStudentForm, self).__init__(*args, **kwargs)
        self.fields['student_id'].choices = [(student.numero_etudiant, f"{student.nom} {student.prenom}") for student in students]