# Generated by Django 4.0.1 on 2022-01-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe_Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Etudians', models.IntegerField()),
            ],
        ),
    ]