# Generated by Django 3.1.3 on 2021-02-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulacion', '0007_auto_20210225_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accionespecifica',
            name='ejecucion_financiera',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accionespecifica',
            name='ejecucion_fisica',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accionespecifica',
            name='ejecutado_anio_anterior',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='accionespecifica',
            name='estimado_anio_ejercicio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='accionespecifica',
            name='estimado_anio_siguiente',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='accionespecifica',
            name='fecha_aprobacion_f_e',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accionespecifica',
            name='inicio_ejecucion_fisica_f_e',
            field=models.DateField(blank=True, null=True),
        ),
    ]
