# Generated by Django 3.1.3 on 2020-12-04 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulacion', '0002_auto_20201203_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=14)),
                ('descripcion', models.TextField()),
                ('estatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=14)),
                ('descripcion', models.TextField()),
                ('estatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ano', models.CharField(max_length=4)),
                ('codigo', models.CharField(max_length=14)),
                ('resumen', models.CharField(max_length=500)),
                ('descripcion', models.TextField()),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('objetivo_historico', models.TextField()),
                ('objetivo_nacional', models.TextField()),
                ('objetivo_estrategico', models.TextField()),
                ('objetivo_general', models.TextField()),
                ('problema', models.TextField()),
                ('codigo_estado', models.CharField(max_length=14)),
                ('codigo_municipio', models.CharField(max_length=14)),
                ('codigo_parroquia', models.CharField(max_length=14)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='formulacion.dependencia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dependencia',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependencias', to='formulacion.sector'),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=14)),
                ('descripcion', models.TextField()),
                ('nivel', models.IntegerField()),
                ('estatus', models.BooleanField(default=True)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='formulacion.dependencia')),
            ],
        ),
        migrations.CreateModel(
            name='AccionEspecifica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=14)),
                ('resumen', models.CharField(max_length=500)),
                ('descripcion', models.TextField()),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('objetivo_historico', models.TextField()),
                ('objetivo_nacional', models.TextField()),
                ('objetivo_estrategico', models.TextField()),
                ('objetivo_general', models.TextField()),
                ('problema', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_especificas', to='formulacion.proyecto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
