# Generated by Django 4.2.1 on 2023-09-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brazo_Izquierdo', models.IntegerField()),
                ('Brazo_Derecho', models.IntegerField()),
                ('Torax', models.IntegerField()),
                ('Brazo_Relajado', models.IntegerField()),
                ('Cadera', models.IntegerField()),
                ('Cintura', models.IntegerField()),
                ('Muslo_Derecho_Contraido', models.IntegerField()),
                ('Muslo_Izquierdo_Contraido', models.IntegerField()),
                ('Pantorrilla_Derecha_Contraida', models.IntegerField()),
                ('Pantorrilla_Izquierda_Contraida', models.IntegerField()),
            ],
        ),
    ]
