# Generated by Django 3.2.4 on 2021-06-20 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contasapagar_contasareceber'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.BigIntegerField()),
                ('tipo', models.CharField(choices=[('0', 'Entrada'), ('1', 'Saída')], max_length=10)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='contasapagar',
            name='notafiscal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.notafiscal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contasareceber',
            name='notafiscal',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='app.notafiscal'),
            preserve_default=False,
        ),
    ]