# Generated by Django 3.2.9 on 2021-11-06 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('nombre_departamento', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('tipodocumento', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name': 'Tipo Documento',
                'verbose_name_plural': 'Tipo Documentos',
            },
        ),
        migrations.CreateModel(
            name='Colombia',
            fields=[
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('numerodocumento', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Numero de documento')),
                ('correo', models.CharField(max_length=40, verbose_name='Direccion de correo electronico')),
                ('telofono', models.CharField(max_length=20, verbose_name='Numero de telefono')),
                ('fecharegistro', models.DateField(verbose_name='Fecha de inicio de cuarentena')),
                ('fechafin', models.DateField(verbose_name='Fecha de fin de cuarentena')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contagios.departamento', verbose_name='Departamento')),
                ('tipodocumento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contagios.documento', verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name': 'Contagio',
                'verbose_name_plural': 'Contagios',
            },
        ),
    ]
