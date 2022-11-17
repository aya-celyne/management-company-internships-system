# Generated by Django 4.0.1 on 2022-01-15 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='groupe',
        ),
        migrations.RemoveField(
            model_name='promoteur',
            name='entreprise',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='encadreur',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='entreprise',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='groupe_des_etudiants',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='promoteur',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='type_stage',
        ),
        migrations.DeleteModel(
            name='Enseignat',
        ),
        migrations.DeleteModel(
            name='Entreprise',
        ),
        migrations.DeleteModel(
            name='Etudiant',
        ),
        migrations.DeleteModel(
            name='Groupe_Etudiant',
        ),
        migrations.DeleteModel(
            name='Promoteur',
        ),
        migrations.DeleteModel(
            name='Stage',
        ),
        migrations.DeleteModel(
            name='Type_Stage',
        ),
    ]
