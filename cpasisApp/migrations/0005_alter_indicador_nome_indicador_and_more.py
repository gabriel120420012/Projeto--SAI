# Generated by Django 5.0.6 on 2024-06-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpasisApp', '0004_indicador_id_campus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='nome_indicador',
            field=models.TextField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='nota_indicador',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]
