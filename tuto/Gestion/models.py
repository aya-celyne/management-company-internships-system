from django.db import models
#from .views import fun

# Create your models here.
class Etudiant(models.Model):
    NomEt= models.CharField(max_length=20,null=False)
    PrenomEt= models.CharField(max_length=20,null=False)
    Année_Etude =models.IntegerField(null=True)
    Ntel= models.IntegerField(null=True)
    groupe=models.ForeignKey("Groupe_Etudiant",on_delete=models.CASCADE,null=True)

class Groupe_Etudiant(models.Model):
    Nombre_Etudians=models.IntegerField(default=0, null=True)
    

class Enseignant(models.Model):
    NomEns=models.CharField(max_length=20,null=False)
    PrenomEns= models.CharField(max_length=20,null=True)
    Ntele= models.IntegerField(null=True)
class Entreprise(models.Model):
    NomEntreprise=models.CharField(max_length=40,primary_key=True)
    adress=models.CharField(max_length=40)
    Nombre_de_stageaires = models.IntegerField(default=0,null=True)


class Promoteur(models.Model):
    NomPr=models.CharField(max_length=20,null=False)
    PrenomPr= models.CharField(max_length=20,null=False)
    Ntelephone= models.IntegerField(null=True)
    entreprise = models.ForeignKey("Entreprise",on_delete=models.CASCADE,null=True)

class Type_Stage(models.Model):
    name=models.CharField(max_length=40,primary_key=True)
    Duree=models.IntegerField()
    PeriodeDebut= models.DateField()
    PeriodeFin= models.DateField()

class Stage(models.Model):

    sujet= models.CharField(max_length=50, null=True)
    Date_debut=  models.DateField()
    Date_fin =  models.DateField()
    type_stage = models.ForeignKey("Type_Stage",on_delete=models.CASCADE,null=True)
    entreprise = models.ForeignKey("Entreprise",on_delete=models.CASCADE,null=True)
    groupe_des_etudiants= models.ForeignKey("Groupe_Etudiant",on_delete=models.CASCADE,null=True)
    promoteur=models.ForeignKey("Promoteur",on_delete=models.CASCADE,null=True)
    encadreur=models.ForeignKey("Enseignant",on_delete=models.CASCADE,null=True)
    