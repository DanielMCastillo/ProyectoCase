# Generated by Django 4.1.2 on 2022-12-01 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0003_alter_alumnos_apellidom_alter_alumnos_nombre2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='matricula',
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                       parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
