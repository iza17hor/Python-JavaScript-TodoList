# Generated by Django 3.1.4 on 2021-02-20 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0002_auto_20210220_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dni',
            old_name='course',
            new_name='co',
        ),
    ]
