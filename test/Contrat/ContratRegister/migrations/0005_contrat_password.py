# Generated by Django 2.1.7 on 2019-03-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContratRegister', '0004_contrat_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='password',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
