# Generated by Django 2.0.9 on 2018-11-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_persona_contrasena'),
    ]

    operations = [
        migrations.AddField(
            model_name='luchador',
            name='pertenece',
            field=models.CharField(default='Ingresado por Administrador', max_length=30),
            preserve_default=False,
        ),
    ]
