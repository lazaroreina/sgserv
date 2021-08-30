# Generated by Django 3.2.6 on 2021-08-30 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_compromisso_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compromisso',
            name='situacao',
            field=models.CharField(choices=[('0', 'A iniciar'), ('1', 'Em andamento'), ('2', 'Encerrada')], default=('0', 'A iniciar'), max_length=30),
        ),
    ]
