# Generated by Django 2.1.7 on 2019-03-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContratRegister', '0006_contrat_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='duree',
            field=models.DateTimeField(default=None),
        ),
    ]
