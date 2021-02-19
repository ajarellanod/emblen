# Generated by Django 3.1.3 on 2021-02-18 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formulacion', '0019_partida_publicacion'),
    ]

    operations = [
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
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cuentas_contables', to='formulacion.publicacion')),
            ],
            options={
                'verbose_name_plural': 'Cuentas Contables',
                'ordering': ('-creado',),
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False, editable=False)),
                ('mes', models.CharField(max_length=2)),
                ('anio', models.CharField(max_length=4)),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('monto', models.DecimalField(decimal_places=4, max_digits=22)),
            ],
            options={
                'verbose_name_plural': 'Comprobantes',
                'unique_together': {('mes', 'anio', 'codigo')},
            },
        ),
    ]
