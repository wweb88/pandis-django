# Generated by Django 2.0.9 on 2018-11-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20181108_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luchador',
            name='imagen',
            field=models.ImageField(upload_to='images/subidas/'),
        ),
    ]
