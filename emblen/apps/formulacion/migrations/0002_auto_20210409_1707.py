# Generated by Django 3.1.3 on 2021-04-09 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulacion', '0001_initial'),
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='publicacion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='partidas', to='nucleo.publicacion'),
        ),
        migrations.AddField(
            model_name='parroquia',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parroquias', to='formulacion.municipio'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='municipios', to='formulacion.estado'),
        ),
        migrations.AddField(
            model_name='lineaprograma',
            name='historico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lineas_programas', to='formulacion.lineaplan'),
        ),
        migrations.AddField(
            model_name='lineaprograma',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lineas_programas', to='formulacion.programa'),
        ),
        migrations.AddField(
            model_name='ingresopresupuestario',
            name='partida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ingresos_presupuestarios', to='formulacion.partida'),
        ),
        migrations.AddField(
            model_name='estimacion',
            name='accion_especifica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estimaciones', to='formulacion.accionespecifica'),
        ),
        migrations.AddField(
            model_name='estimacion',
            name='partida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estimaciones', to='formulacion.partida'),
        ),
        migrations.AlterUniqueTogether(
            name='ejerciciopresupuestario',
            unique_together={('anio', 'eliminado')},
        ),
        migrations.AddField(
            model_name='dependencia',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dependencias', to='formulacion.sector'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='unidad_ejecutora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departamentos', to='formulacion.unidadejecutora'),
        ),
        migrations.AddField(
            model_name='categoriaareainversion',
            name='area_inversion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categoria_area_inversion', to='formulacion.areainversion'),
        ),
        migrations.AddField(
            model_name='accioninterna',
            name='accion_especifica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_internas', to='formulacion.accionespecifica'),
        ),
        migrations.AddField(
            model_name='accioninterna',
            name='fuente_financiamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_internas', to='formulacion.fuentefinanciamiento'),
        ),
        migrations.AddField(
            model_name='accioninterna',
            name='tipo_gasto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_internas', to='formulacion.tipogasto'),
        ),
        migrations.AddField(
            model_name='accioninterna',
            name='tipo_organismo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_internas', to='formulacion.tipoorganismo'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='centro_costo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.centrocosto'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='condicion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.condicionprograma'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='estatus_financiamiento_externo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.estatusfinanciamientoexterno'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='parroquia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.parroquia'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.programa'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.departamento'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.sectordesarrollador'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='tipo_area_inversion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.tipoareainversion'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='tipo_beneficiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.tipobeneficiario'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='unidad_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acciones_especificas', to='formulacion.unidadmedida'),
        ),
        migrations.AlterUniqueTogether(
            name='programa',
            unique_together={('anio', 'nivel', 'contador')},
        ),
        migrations.AlterUniqueTogether(
            name='partidaaccioninterna',
            unique_together={('accion_interna', 'partida', 'anio')},
        ),
        migrations.AlterUniqueTogether(
            name='ingresopresupuestario',
            unique_together={('partida', 'anio')},
        ),
        migrations.AlterUniqueTogether(
            name='estimacion',
            unique_together={('accion_especifica', 'partida', 'anio', 'eliminado')},
        ),
    ]
