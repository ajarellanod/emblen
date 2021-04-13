# Generated by Django 3.1.3 on 2021-04-09 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contabilidad', '0001_initial'),
        ('nucleo', '0001_initial'),
        ('ejecucion', '0001_initial'),
        ('compras', '0002_auto_20210409_1707'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contratopartida',
            name='movimiento_gasto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_partidas', to='nucleo.movimientogasto'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='addendum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contratos', to='compras.contrato'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tipo_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos', to='compras.tipocontrato'),
        ),
        migrations.AddField(
            model_name='compromiso',
            name='movimiento_gasto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compromisos', to='nucleo.movimientogasto'),
        ),
        migrations.AddField(
            model_name='compromiso',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compromisos', to='compras.orden'),
        ),
        migrations.AddField(
            model_name='beneficiariocontrato',
            name='beneficiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiarios_contratos', to='compras.beneficiario'),
        ),
        migrations.AddField(
            model_name='beneficiariocontrato',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiarios_contratos', to='compras.contrato'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='cuenta_anticipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='anticipo_beneficiarios', to='contabilidad.cuentacontable'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='cuenta_contable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cuenta_beneficiarios', to='contabilidad.cuentacontable'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='tipo_beneficiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiarios', to='compras.tipobeneficiario'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='usuario_inscripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiarios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anticipocontrato',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='anticipos_contratos', to='compras.contrato'),
        ),
        migrations.AddField(
            model_name='anticipocontrato',
            name='orden_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='anticipos_contratos', to='ejecucion.ordenpago'),
        ),
        migrations.AlterUniqueTogether(
            name='documentopagar',
            unique_together={('numero', 'anio', 'beneficiario')},
        ),
    ]