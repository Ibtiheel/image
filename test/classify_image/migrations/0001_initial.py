# Generated by Django 2.1.1 on 2019-04-20 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, default=None, max_length=200, null=True, unique=True)),
                ('dept', models.CharField(default=None, max_length=20)),
                ('message', models.CharField(default=None, max_length=20)),
            ],
        ),
    ]
