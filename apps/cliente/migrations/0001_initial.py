# Generated by Django 4.2.1 on 2023-09-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCompleto', models.CharField(max_length=100)),
                ('FechaInicio', models.DateField()),
                ('FechaFin', models.DateField()),
                ('FechaPago', models.DateField()),
                ('Edad', models.IntegerField()),
                ('Telefono', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Domicilio', models.CharField(max_length=200)),
            ],
        ),
    ]
