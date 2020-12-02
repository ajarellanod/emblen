# Generated by Django 3.1.3 on 2020-12-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=14)),
                ('descripcion', models.TextField()),
                ('nivel', models.CharField(max_length=1)),
                ('saldo', models.FloatField()),
                ('fecha_c', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1)),
            ],
            options={
                'ordering': ('-fecha_c',),
            },
        ),
    ]
