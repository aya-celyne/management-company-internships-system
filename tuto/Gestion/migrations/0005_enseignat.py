# Generated by Django 4.0.1 on 2022-01-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0004_groupe_etudiant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomEns', models.CharField(max_length=20)),
                ('PrenomEns', models.CharField(max_length=20)),
                ('Ntele', models.IntegerField(null=True)),
            ],
        ),
    ]
