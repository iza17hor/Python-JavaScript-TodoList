# Generated by Django 3.1.4 on 2021-02-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cele',
            name='rozwiniecie',
            field=models.BooleanField(),
        ),
    ]