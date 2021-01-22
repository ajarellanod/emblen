# Generated by Django 3.1.3 on 2021-01-21 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulacion', '0011_auto_20210117_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartidaAccionInterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('anio', models.CharField(max_length=4)),
                ('mto_original', models.DecimalField(decimal_places=2, max_digits=22)),
                ('mto_actualizado', models.DecimalField(decimal_places=2, max_digits=22)),
            ],
            options={
                'verbose_name_plural': 'Cuentas - Centros de Costos - Acciones Internas',
            },
        ),
        migrations.AlterUniqueTogether(
            name='ctasccostoaint',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='ctasccostoaint',
            name='ccosto_accint',
        ),
        migrations.RemoveField(
            model_name='ctasccostoaint',
            name='partida',
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='centro_costo',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.centrocosto'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CCostoAccInt',
        ),
    ]
