# Generated by Django 4.2.4 on 2023-09-20 22:54

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
            ],
        ),
    ]
