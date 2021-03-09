# Generated by Django 3.1.3 on 2021-03-08 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formulacion', '0001_initial'),
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
                ('afectacion', models.CharField(choices=[('D', 'Disminucion'), ('A', 'Aumento')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Modificaciones',
            },
        ),
        migrations.CreateModel(
            name='Modificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('anio', models.CharField(max_length=4)),
                ('numero', models.IntegerField()),
                ('documento_referenciado', models.IntegerField(blank=True, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=22)),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True)),
                ('descripcion', models.CharField(max_length=300)),
                ('estatus', models.IntegerField(choices=[(0, 'Elaborado'), (1, 'Verificado'), (2, 'Anulado')], default=0, verbose_name='Estatus Modificación de Egreso')),
                ('anulador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='a_modificaciones_egreso', to=settings.AUTH_USER_MODEL)),
                ('elaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='e_modificaciones_egreso', to=settings.AUTH_USER_MODEL)),
                ('modificacion_ingreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones', to='formulacion.modificacioningreso')),
                ('partida_accioninterna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones', to='formulacion.partidaaccioninterna')),
                ('tipo_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modificaciones', to='planificacion.tipomodificacion')),
                ('verificador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='v_modificaciones_egreso', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Modificaciones',
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
