# Generated by Django 3.2.6 on 2021-08-28 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_compromisso_identificador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compromisso',
            name='identificador',
        ),
    ]
