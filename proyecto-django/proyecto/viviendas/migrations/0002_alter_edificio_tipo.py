# Generated by Django 4.2.2 on 2023-07-24 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificio',
            name='tipo',
            field=models.CharField(choices=[('Residencial', 'Residencial'), ('Público', 'Público'), ('Negocio', 'Negocio')], max_length=30),
        ),
    ]
