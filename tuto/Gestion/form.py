from ast import Mod
from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Enseignant, Etudiant, Groupe_Etudiant, Entreprise,Promoteur,Stage,Type_Stage
from django.contrib.auth.models import User
class Etudiantform(ModelForm):
    class Meta:
        model = Etudiant
        fields= "__all__"

class Enseignantform(ModelForm):
    class Meta:
        model = Enseignant
        fields= "__all__"

class Entrepriseform(ModelForm):
     class Meta:
        model = Entreprise
        fields= ['NomEntreprise','adress']

class PromoteurForm(ModelForm):
     class Meta:
        model = Promoteur
        fields= "__all__"

class StageForm(ModelForm):
     class Meta:
        model = Stage
        fields= "__all__"

class GroupeForm(ModelForm):
    class Meta:
        model= Groupe_Etudiant
        fields= "__all__"

class TypeSform(ModelForm):
    class Meta:
        model = Type_Stage
        fields="__all__"
