# Generated by Django 4.1.3 on 2022-11-18 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_alter_doctors_achiv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='photo',
        ),
    ]
