# Generated by Django 4.2.1 on 2023-09-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nutricion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.TextField(max_length=350)),
                ('hora', models.TextField(max_length=350)),
                ('tipo_comida', models.TextField(max_length=350)),
                ('alimento', models.TextField(max_length=350)),
                ('porcion', models.TextField(max_length=350)),
                ('evitar', models.TextField(max_length=350)),
                ('otras_recomendaciones', models.TextField(max_length=350)),
                ('ingesta_agua', models.TextField(max_length=350)),
                ('dia_trampa', models.TextField(max_length=350)),
                ('suplementos', models.TextField(max_length=350)),
                ('lista_compra', models.TextField(max_length=350)),
            ],
        ),
    ]
