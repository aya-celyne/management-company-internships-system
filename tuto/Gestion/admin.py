from django.contrib import admin

from Gestion.models import Enseignant, Entreprise, Etudiant, Groupe_Etudiant, Promoteur, Stage, Type_Stage

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Enseignant)
admin.site.register(Groupe_Etudiant)
admin.site.register(Entreprise)
admin.site.register(Promoteur)
admin.site.register(Type_Stage)
admin.site.register(Stage)