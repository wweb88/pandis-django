# Generated by Django 2.0.9 on 2018-11-13 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0015_auto_20181112_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='luchador',
            name='contador',
            field=models.IntegerField(default=0),
        ),
    ]