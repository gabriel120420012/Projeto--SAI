# Generated by Django 5.0.6 on 2024-05-19 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dimensao',
            fields=[
                ('id_dim', models.AutoField(primary_key=True, serialize=False)),
                ('nome_dim', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eixo',
            fields=[
                ('id_eixo', models.AutoField(primary_key=True, serialize=False)),
                ('nome_eixo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id_indicador', models.AutoField(primary_key=True, serialize=False)),
                ('nome_indicador', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('nota_indicador', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('id_dim', models.ForeignKey(blank=True, db_column='id_dim', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cpasisApp.dimensao')),
                ('id_eixo', models.ForeignKey(blank=True, db_column='id_eixo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cpasisApp.eixo')),
            ],
        ),
    ]