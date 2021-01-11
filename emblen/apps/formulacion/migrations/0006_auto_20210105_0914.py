# Generated by Django 3.1.3 on 2021-01-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulacion', '0005_auto_20210102_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programa',
            name='sexo_benificiario',
        ),
        migrations.AddField(
            model_name='programa',
            name='sexo_beneficiario',
            field=models.IntegerField(choices=[(0, 'Femenino'), (1, 'Masculino'), (2, 'No Definido')], default=2, verbose_name='Sexo del Beneficiario'),
        ),
        migrations.AlterField(
            model_name='accionespecifica',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='accioninterna',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='areainversion',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='categoriaareainversion',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='ccostoaccint',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='centrocosto',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='condicionprograma',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='ctasccostoaint',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='dependencia',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='estado',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='estatusfinanciamientoexterno',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='estimacion',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='fuentefinanciamiento',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='lineaplan',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='lineaprograma',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='partida',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='periodoactualizacion',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='plandesarrollo',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='programa',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='programa',
            name='estado',
            field=models.CharField(default='INI', max_length=3),
        ),
        migrations.AlterField(
            model_name='programa',
            name='nivel',
            field=models.IntegerField(choices=[(0, 'Proyecto'), (1, 'Acción Centralizada')]),
        ),
        migrations.AlterField(
            model_name='sector',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='sectordesarrollador',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='tipoareainversion',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='tipobeneficiario',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='tipogasto',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='tipoorganismo',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='unidadejecutora',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='unidadmedida',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
