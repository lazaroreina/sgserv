# Generated by Django 3.2.6 on 2021-08-30 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_compromisso_equipamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='compromisso',
            name='situacao',
            field=models.CharField(choices=[('0', 'A iniciar'), ('1', 'Em andamento'), ('2', 'Encerrada')], default='1', max_length=30),
            preserve_default=False,
        ),
    ]
