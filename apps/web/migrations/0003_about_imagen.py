# Generated by Django 2.2.2 on 2019-09-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190916_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='imagen',
            field=models.ImageField(default='', upload_to='perfil', verbose_name='Imagen de Perfil: '),
            preserve_default=False,
        ),
    ]
