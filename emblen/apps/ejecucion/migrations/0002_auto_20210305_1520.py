# Generated by Django 3.1.3 on 2021-03-05 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ejecucion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('rif', models.CharField(max_length=12)),
                ('razon_social', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=13)),
                ('correo', models.EmailField(max_length=254)),
                ('numero_inscripcion', models.IntegerField()),
                ('fecha_inscripcion', models.DateField()),
                ('numero_registro', models.CharField(max_length=12)),
                ('fecha_registro', models.DateField()),
                ('capital', models.DecimalField(decimal_places=4, max_digits=22)),
                ('representante', models.CharField(max_length=100)),
                ('cedula_representante', models.CharField(max_length=12)),
                ('fecha_vigencia', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Beneficiarios',
            },
        ),
        migrations.CreateModel(
            name='CuentaContable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('cuenta', models.CharField(max_length=12, unique=True)),
                ('descripcion', models.TextField(max_length=100)),
                ('nivel', models.IntegerField()),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cuentas_contables_ejecucion', to='formulacion.publicacion')),
            ],
            options={
                'verbose_name_plural': 'Cuentas Contables',
                'ordering': ('-creado',),
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Documentos',
            },
        ),
        migrations.CreateModel(
            name='TipoBeneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('abreviacion', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=100)),
                ('cuenta_contable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipos_beneficiarios', to='ejecucion.cuentacontable')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Beneficiarios',
            },
        ),
        migrations.CreateModel(
            name='DocumentoPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('anio', models.CharField(max_length=4)),
                ('numero', models.CharField(max_length=10)),
                ('numero_control', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('monto_imponible', models.DecimalField(decimal_places=4, max_digits=22)),
                ('monto_iva', models.DecimalField(decimal_places=4, max_digits=22)),
                ('monto', models.DecimalField(decimal_places=4, max_digits=22)),
                ('descripcion', models.CharField(max_length=100)),
                ('forma_pago', models.IntegerField(choices=[(1, 'Crédito'), (2, 'Contado'), (3, 'Efectivo')], default=1)),
                ('beneficiario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='documentos_pagar_ejecucion', to='ejecucion.beneficiario')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documentos_pagar', to='ejecucion.tipodocumento')),
            ],
            options={
                'verbose_name_plural': 'Documentos a Pagar',
                'unique_together': {('numero', 'anio', 'beneficiario')},
            },
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='cuenta_anticipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='anticipo_beneficiarios_ejecucion', to='ejecucion.cuentacontable'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='cuenta_contable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cuenta_beneficiarios_ejecucion', to='ejecucion.cuentacontable'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='parroquia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiarios_ejecucion', to='formulacion.parroquia'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='tipo_beneficiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiarios_ejecucion', to='ejecucion.tipobeneficiario'),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='usuario_inscripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beneficiarios_ejecucion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AsientoContable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('tipo_afectacion', models.CharField(choices=[('D', 'Débito'), ('C', 'Crédito')], default='D', max_length=1)),
                ('monto', models.DecimalField(decimal_places=4, max_digits=22)),
                ('saldo', models.DecimalField(decimal_places=4, max_digits=22)),
                ('fecha', models.DateField()),
                ('cuenta_contable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asientos_contables_ejecucion', to='ejecucion.cuentacontable')),
                ('orden_pago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asientos_contables_ejecucion', to='ejecucion.ordenpago')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asientos_contables_ejecucion', to='formulacion.partidaaccioninterna')),
            ],
            options={
                'verbose_name_plural': 'Asientos Contables',
            },
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='beneficiario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ordenes_pago', to='ejecucion.beneficiario'),
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='documento_pagar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ordenes_pago', to='ejecucion.documentopagar'),
        ),
    ]
