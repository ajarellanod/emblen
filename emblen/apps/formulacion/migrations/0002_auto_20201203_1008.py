# Generated by Django 3.1.3 on 2020-12-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partida',
            options={'ordering': ('-creado',)},
        ),
        migrations.RenameField(
            model_name='partida',
            old_name='fecha_c',
            new_name='creado',
        ),
        migrations.AddField(
            model_name='partida',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='estatus',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='partida',
            name='nivel',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='partida',
            name='saldo',
            field=models.DecimalField(decimal_places=4, max_digits=22),
        ),
    ]
