# Generated by Django 4.1.4 on 2023-03-05 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre_municipio', models.CharField(max_length=50)),
                ('poblacion', models.PositiveSmallIntegerField(default=1)),
                ('area', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id_vivienda', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('capacidad', models.PositiveSmallIntegerField(default=1)),
                ('pisos', models.PositiveSmallIntegerField(default=1)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viviendas',
                                                to='lab0.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.CharField(max_length=50)),
                ('cabeza_familia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                     to='lab0.persona')),
                ('municipio',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas_muni',
                                   to='lab0.municipio')),
                ('residencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='personas_vivi', to='lab0.vivienda')),
            ],
        ),
    ]
