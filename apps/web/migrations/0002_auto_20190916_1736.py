# Generated by Django 2.2.2 on 2019-09-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='imagen',
            field=models.ImageField(upload_to='portafolio', verbose_name='Imagen Descriptiva: '),
        ),
    ]
