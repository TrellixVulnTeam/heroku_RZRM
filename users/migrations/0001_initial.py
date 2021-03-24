# Generated by Django 3.1.7 on 2021-03-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(blank=True, max_length=60, verbose_name='Nome Completo:')),
                ('idadi', models.CharField(blank=True, max_length=15, verbose_name='Idade:')),
                ('ocupacao', models.CharField(blank=True, max_length=100, verbose_name='Cargo:')),
                ('estado', models.CharField(blank=True, max_length=20, verbose_name='Situação:')),
                ('aniversario', models.CharField(blank=True, max_length=30, verbose_name='Data de Aniversário:')),
                ('convert', models.CharField(blank=True, max_length=30, verbose_name='Data de Conversão:')),
                ('banho', models.CharField(blank=True, max_length=30, verbose_name='Data de Batismo:')),
                ('casa', models.CharField(blank=True, max_length=200, verbose_name='Endereço:')),
                ('tel', models.CharField(blank=True, max_length=30, verbose_name='Telefone:')),
            ],
        ),
    ]
