# Generated by Django 3.1.3 on 2020-12-18 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccionEspecifica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=11)),
                ('condicion', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('detallada', models.TextField()),
                ('especifico', models.TextField()),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('impacto_social', models.TextField()),
                ('articulacion', models.TextField()),
                ('vinculacion', models.BooleanField(default=True)),
                ('financiamiento_externo', models.BooleanField(default=False)),
                ('bien_servicio', models.TextField()),
                ('distincion_genero', models.BooleanField(default=True)),
                ('beneficiario_masculino', models.IntegerField()),
                ('beneficiario_femenino', models.IntegerField()),
                ('directo_masculino', models.IntegerField()),
                ('directo_femenino', models.IntegerField()),
                ('indirecto_masculino', models.IntegerField()),
                ('indirecto_femenino', models.IntegerField()),
                ('extension_territorial', models.BooleanField(default=True)),
                ('plazo_ejecucion', models.IntegerField()),
                ('trimestre_1', models.DecimalField(decimal_places=4, max_digits=22)),
                ('trimestre_2', models.DecimalField(decimal_places=4, max_digits=22)),
                ('trimestre_3', models.DecimalField(decimal_places=4, max_digits=22)),
                ('trimestre_4', models.DecimalField(decimal_places=4, max_digits=22)),
                ('fase', models.CharField(max_length=100)),
                ('fecha_aprobacion_f_e', models.DateTimeField()),
                ('inicio_ejecucion_fisica_f_e', models.DateTimeField()),
                ('ejecucion_fisica', models.FloatField()),
                ('ejecucion_financiera', models.FloatField()),
                ('ejecutado_anio_anterior', models.DecimalField(decimal_places=4, max_digits=22)),
                ('estimado_anio_siguiente', models.DecimalField(decimal_places=4, max_digits=22)),
                ('estimado_anio_ejercicio', models.DecimalField(decimal_places=4, max_digits=22)),
            ],
            options={
                'verbose_name_plural': 'Acciones Especificas',
            },
        ),
        migrations.CreateModel(
            name='AccionInterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=11)),
                ('descripcion', models.TextField()),
                ('nivel', models.CharField(max_length=1)),
                ('auxiliar', models.CharField(max_length=4)),
                ('transferencia', models.BooleanField(default=False)),
                ('estatus', models.BooleanField(default=True)),
                ('accion_especifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_internas', to='formulacion.accionespecifica')),
            ],
            options={
                'verbose_name_plural': 'Acciones Internas',
            },
        ),
        migrations.CreateModel(
            name='AreaInversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Areas de Inversion',
            },
        ),
        migrations.CreateModel(
            name='CategoriaAreaInversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
                ('area_inversion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_area_inversion', to='formulacion.areainversion')),
            ],
            options={
                'verbose_name_plural': 'Categorias de las Areas de Inversion',
            },
        ),
        migrations.CreateModel(
            name='CentroCosto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('nivel', models.IntegerField()),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Centros de Costos',
            },
        ),
        migrations.CreateModel(
            name='CondicionPrograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Condiciones de los Programas',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=14)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=14)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Dependencias',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='EstatusFinanciamientoExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Estatus de Financiamientos Externos',
            },
        ),
        migrations.CreateModel(
            name='FuenteFinanciamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('orden', models.IntegerField()),
                ('externo', models.BooleanField(default=False)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Fuentes de Financiamientos',
            },
        ),
        migrations.CreateModel(
            name='LineaPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(max_length=1)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Lineas del Plan',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='formulacion.estado')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parroquias', to='formulacion.municipio')),
            ],
            options={
                'verbose_name_plural': 'Parroquias',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('cuenta', models.CharField(max_length=12, unique=True)),
                ('descripcion', models.TextField()),
                ('nivel', models.IntegerField()),
                ('saldo', models.DecimalField(decimal_places=4, max_digits=22, null=True)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Programas',
                'ordering': (('-creado',),),
            },
        ),
        migrations.CreateModel(
            name='PeriodoActualizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Periodos de Actualizacion',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=14)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Sectores',
            },
        ),
        migrations.CreateModel(
            name='SectorDesarrollador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Sectores Desarrolladores',
            },
        ),
        migrations.CreateModel(
            name='TipoBeneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Beneficiarios',
            },
        ),
        migrations.CreateModel(
            name='TipoGasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=2)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Gasto',
            },
        ),
        migrations.CreateModel(
            name='TipoOrganismo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=2)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Organismos',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('dimension', models.IntegerField()),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Unidades de Medidas',
            },
        ),
        migrations.CreateModel(
            name='UnidadEjecutora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
                ('adscrito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formulacion.unidadejecutora')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unidadejecutoras', to='formulacion.dependencia')),
            ],
            options={
                'verbose_name_plural': 'Unidades Ejecutoras',
            },
        ),
        migrations.CreateModel(
            name='TipoAreaInversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_area_inversion', to='formulacion.categoriaareainversion')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Areas de Inversion',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('anio', models.CharField(max_length=4)),
                ('codigo', models.CharField(max_length=11)),
                ('nivel', models.IntegerField()),
                ('detallada', models.TextField()),
                ('estado', models.CharField(max_length=3)),
                ('plan_inversion_social', models.BooleanField(default=False)),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('extension_territorial', models.BooleanField(default=True)),
                ('desarrollo_sostenible', models.TextField()),
                ('estrategico', models.TextField()),
                ('problematica', models.TextField()),
                ('especifico', models.TextField()),
                ('resumen', models.TextField()),
                ('bien_servicio', models.TextField()),
                ('indicador_situacion', models.TextField()),
                ('indicador_fuente', models.TextField()),
                ('indicador_formula', models.TextField()),
                ('indicador_objetivo', models.TextField()),
                ('trimestre_1', models.DecimalField(decimal_places=4, max_digits=22)),
                ('trimestre_2', models.DecimalField(decimal_places=4, max_digits=22)),
                ('trimestre_3', models.DecimalField(decimal_places=4, max_digits=22)),
                ('trimestre_4', models.DecimalField(decimal_places=4, max_digits=22)),
                ('distincion_genero', models.BooleanField(default=True)),
                ('beneficiario_masculino', models.IntegerField()),
                ('beneficiario_femenino', models.IntegerField()),
                ('directo_masculino', models.IntegerField()),
                ('directo_femenino', models.IntegerField()),
                ('indirecto_masculino', models.IntegerField()),
                ('indirecto_femenino', models.IntegerField()),
                ('ejecucion_fisica', models.FloatField()),
                ('ejecucion_financiera', models.FloatField()),
                ('condicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.condicionprograma')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.dependencia')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.parroquia')),
                ('periodo_actualizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.periodoactualizacion')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.departamento')),
                ('sector_desarrollador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.sectordesarrollador')),
                ('tipo_beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.tipobeneficiario')),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='formulacion.unidadmedida')),
            ],
            options={
                'verbose_name_plural': 'Programas',
            },
        ),
        migrations.CreateModel(
            name='PlanDesarrollo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('plan_metas', models.TextField()),
                ('metas', models.TextField()),
                ('solucion', models.TextField()),
                ('estatus', models.BooleanField(default=True)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_desarrollos', to='formulacion.lineaplan')),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_desarrollos', to='formulacion.programa')),
            ],
            options={
                'verbose_name_plural': 'Planes de Desarrollo',
            },
        ),
        migrations.CreateModel(
            name='LineaPrograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nacional', models.TextField()),
                ('estrategico', models.TextField()),
                ('general', models.TextField()),
                ('estatus', models.BooleanField(default=True)),
                ('historico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineas_programas', to='formulacion.lineaplan')),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineas_programas', to='formulacion.programa')),
            ],
            options={
                'verbose_name_plural': 'Lineas del Programa',
            },
        ),
        migrations.AddField(
            model_name='dependencia',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependencias', to='formulacion.sector'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='dependencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='formulacion.dependencia'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='unidad_ejecutora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='formulacion.unidadejecutora'),
        ),
        migrations.CreateModel(
            name='CCostoAccInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('anio', models.CharField(max_length=4)),
                ('estatus', models.BooleanField(default=True)),
                ('accion_interna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ccosto_accint', to='formulacion.accioninterna')),
                ('centro_costo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ccosto_accint', to='formulacion.centrocosto')),
            ],
            options={
                'verbose_name_plural': 'Centros de Costos - Acciones Internas',
            },
        ),
        migrations.AddField(
            model_name='accioninterna',
            name='fuente_financiamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_internas', to='formulacion.fuentefinanciamiento'),
        ),
        migrations.AddField(
            model_name='accioninterna',
            name='tipo_gasto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_internas', to='formulacion.tipogasto'),
        ),
        migrations.AddField(
            model_name='accioninterna',
            name='tipo_organismo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_internas', to='formulacion.tipoorganismo'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='estatus_financiamiento_externo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.estatusfinanciamientoexterno'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='parroquia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.parroquia'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.programa'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.departamento'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.sectordesarrollador'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='tipo_area_inversion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.tipoareainversion'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='tipo_beneficiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.tipobeneficiario'),
        ),
        migrations.AddField(
            model_name='accionespecifica',
            name='unidad_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.unidadmedida'),
        ),
        migrations.CreateModel(
            name='Estimacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('monto', models.DecimalField(decimal_places=4, max_digits=22)),
                ('estatus', models.BooleanField(default=True)),
                ('anio', models.CharField(max_length=4)),
                ('accion_especifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estimaciones', to='formulacion.accionespecifica')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estimaciones', to='formulacion.partida')),
            ],
            options={
                'verbose_name_plural': 'Estimaciones por Partidas',
                'unique_together': {('accion_especifica', 'partida', 'anio')},
            },
        ),
        migrations.CreateModel(
            name='CtasCCostoAInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('anio', models.CharField(max_length=4)),
                ('mto_original', models.DecimalField(decimal_places=4, max_digits=22)),
                ('mto_actualizado', models.DecimalField(decimal_places=4, max_digits=22)),
                ('estatus', models.BooleanField(default=True)),
                ('ccosto_accint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ctas_ccosto_aint', to='formulacion.ccostoaccint')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ctas_ccosto_aint', to='formulacion.partida')),
            ],
            options={
                'verbose_name_plural': ('Cuentas - Centros de Costos - Acciones Internas',),
                'unique_together': {('ccosto_accint', 'partida', 'anio')},
            },
        ),
    ]
