# Generated by Django 5.0.6 on 2024-06-25 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpasisApp', '0006_indicador_foto_indicador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='nome_indicador',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='nota_indicador',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
