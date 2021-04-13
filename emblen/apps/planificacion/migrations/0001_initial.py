# Generated by Django 3.1.3 on 2021-04-09 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoModificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('codigo', models.CharField(max_length=2)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('afectacion', models.CharField(choices=[('D', 'Disminucion'), ('A', 'Aumento'), ('T', 'Traspaso')], max_length=1)),
                ('tipo_modificacion', models.CharField(choices=[('I', 'Ingresos'), ('G', 'Gastos')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Modificaciones',
            },
        ),
        migrations.CreateModel(
            name='ModificacionIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('anio', models.CharField(max_length=4)),
                ('fecha', models.DateField()),
                ('periodo', models.CharField(max_length=2)),
                ('numero', models.IntegerField()),
                ('tipo_documento', models.IntegerField(choices=[(0, 'Gaceta'), (1, 'Acta')], verbose_name='Tipo de Documento del Ingreso')),
                ('numero_documento', models.CharField(max_length=10)),
                ('fecha_documento', models.DateField()),
                ('numero_decreto', models.CharField(max_length=10, null=True)),
                ('descripcion', models.TextField(max_length=300)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=22)),
                ('estatus', models.IntegerField(choices=[(0, 'Elaborado'), (1, 'Verificado'), (2, 'Anulado'), (3, 'Reversado')], default=0, verbose_name='Estatus Modificacón de Ingreso')),
                ('anulador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='a_modificaciones_ingresos', to=settings.AUTH_USER_MODEL)),
                ('elaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='e_modificaciones_ingresos', to=settings.AUTH_USER_MODEL)),
                ('ingreso_presupuestario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones_ingresos', to='formulacion.ingresopresupuestario')),
                ('reversor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='r_modificaciones_ingresos', to=settings.AUTH_USER_MODEL)),
                ('tipo_modificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones_ingresos', to='planificacion.tipomodificacion')),
                ('verificador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='v_modificaciones_ingresos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Modificaciones de Ingresos',
            },
        ),
        migrations.CreateModel(
            name='ModificacionGasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('fecha', models.DateField()),
                ('numero', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
                ('estatus', models.IntegerField(choices=[(0, 'Elaborada'), (1, 'Verificada'), (2, 'Anulada'), (3, 'Reversada')], default=0, verbose_name='Estatus Modificación de Gasto')),
                ('anulador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='a_modificaciones_gastos', to=settings.AUTH_USER_MODEL)),
                ('elaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='e_modificaciones_gastos', to=settings.AUTH_USER_MODEL)),
                ('modificacion_ingreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones_gastos', to='planificacion.modificacioningreso')),
                ('movimiento_gasto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones_gastos', to='nucleo.movimientogasto')),
                ('reversor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='r_modificaciones_gastos', to=settings.AUTH_USER_MODEL)),
                ('tipo_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones_gastos', to='planificacion.tipomodificacion')),
                ('verificador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='v_modificaciones_gastos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Modificaciones de Gastos',
            },
        ),
        migrations.CreateModel(
            name='AcumuladosPresupuestario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('anio', models.CharField(max_length=4)),
                ('mes', models.CharField(max_length=2)),
                ('compromiso', models.DecimalField(decimal_places=4, max_digits=22)),
                ('causado', models.DecimalField(decimal_places=4, max_digits=22)),
                ('pago', models.DecimalField(decimal_places=4, max_digits=22)),
                ('aumento', models.DecimalField(decimal_places=4, max_digits=22)),
                ('disminucion', models.DecimalField(decimal_places=4, max_digits=22)),
                ('por_comprometer', models.DecimalField(decimal_places=4, max_digits=22)),
                ('por_causar', models.DecimalField(decimal_places=4, max_digits=22)),
                ('por_pagar', models.DecimalField(decimal_places=4, max_digits=22)),
                ('monto', models.DecimalField(decimal_places=4, max_digits=22)),
                ('saldo', models.DecimalField(decimal_places=4, max_digits=22)),
                ('descripcion', models.CharField(max_length=100)),
                ('partida_accioninterna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='acumuladospresupuestarios', to='formulacion.partidaaccioninterna')),
            ],
            options={
                'verbose_name_plural': 'Acumulados Presupuestario',
                'unique_together': {('partida_accioninterna', 'mes', 'anio')},
            },
        ),
    ]
