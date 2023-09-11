# Generated by Django 4.2.1 on 2023-09-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musculo', models.TextField(max_length=25)),
                ('ejercicio', models.TextField(max_length=25)),
                ('series', models.FloatField(max_length=25)),
                ('repeticiones', models.FloatField(max_length=25)),
                ('rir', models.FloatField(max_length=25)),
                ('cadencia', models.FloatField(max_length=25)),
                ('microPausa', models.FloatField(max_length=25)),
                ('macroPausa', models.FloatField(max_length=25)),
                ('descripcion', models.TextField(max_length=25)),
                ('imagen', models.TextField(max_length=25)),
            ],
        ),
    ]
