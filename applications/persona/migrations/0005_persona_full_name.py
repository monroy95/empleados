# Generated by Django 4.0.4 on 2022-05-31 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_persona_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre Completo'),
        ),
    ]
