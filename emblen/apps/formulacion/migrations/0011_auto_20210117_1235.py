# Generated by Django 3.1.3 on 2021-01-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulacion', '0010_auto_20210113_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accioninterna',
            name='codigo',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='accioninterna',
            name='nivel',
            field=models.IntegerField(choices=[(1, 'Nivel 1'), (2, 'Nivel 2'), (3, 'Nivel 3')]),
        ),
    ]
