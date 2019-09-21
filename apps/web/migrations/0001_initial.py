# Generated by Django 2.2.2 on 2019-09-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre: ')),
                ('perfil', models.CharField(max_length=50, verbose_name='Perfil: ')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electrónico: ')),
                ('telefono', models.CharField(max_length=30, verbose_name='Telefono: ')),
                ('contenido', models.TextField(verbose_name='Acerca de mí')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(blank='False', max_length=40, verbose_name='Especialidad: ')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicios', models.CharField(max_length=150, verbose_name='Descripción: ')),
                ('hacking', models.TextField(verbose_name='Hacking Ético: ')),
                ('web', models.TextField(verbose_name='Desarrollo Web')),
                ('software', models.TextField(verbose_name='Desarrollo de Sofware')),
                ('videos', models.TextField(verbose_name='Edición de Videos: ')),
                ('responsive', models.TextField(verbose_name='Diseño Responsive: ')),
                ('bd', models.TextField(verbose_name='Bases de Datos')),
            ],
        ),
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=50, verbose_name='Nombre del Proyecto: ')),
                ('fecha', models.DateTimeField(verbose_name='Fecha de creación: ')),
                ('imagen', models.ImageField(upload_to=False, verbose_name='Imagen Descriptiva: ')),
                ('categoria', models.ForeignKey(on_delete=True, to='web.Especialidades')),
            ],
        ),
    ]
