# Generated by Django 4.0.1 on 2022-01-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0015_remove_entreprise_nombre_de_stageaires'),
    ]

    operations = [
        migrations.AddField(
            model_name='entreprise',
            name='Nombre_de_stageaires',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
