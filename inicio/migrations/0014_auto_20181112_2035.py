# Generated by Django 2.0.9 on 2018-11-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0013_persona_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luchador',
            name='imagen',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
