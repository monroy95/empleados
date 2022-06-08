# Generated by Django 4.0.4 on 2022-05-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Nombre Corto'),
        ),
    ]
