# Generated by Django 4.1.2 on 2022-12-01 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alumnos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='apellidoM',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='nombre2',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
