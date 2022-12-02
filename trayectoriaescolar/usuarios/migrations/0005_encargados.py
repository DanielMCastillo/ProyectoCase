# Generated by Django 4.1.2 on 2022-12-01 23:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuarios', '0004_remove_alumnos_matricula_alter_alumnos_user_ptr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encargados',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('correo', models.CharField(max_length=70)),
                ('nombre', models.TextField(max_length=50)),
                ('nombre2', models.TextField(blank=True, max_length=50, null=True)),
                ('apellidoP', models.TextField(max_length=50)),
                ('apellidoM', models.TextField(blank=True, max_length=50, null=True)),
                ('programa_academico', models.TextField(max_length=70)),
                ('unidad_academica', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]