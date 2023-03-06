from django.db import models


class Municipio(models.Model):
    id_municipio = models.PositiveSmallIntegerField(primary_key=True)
    nombre_municipio = models.CharField(max_length=50)
    poblacion = models.PositiveSmallIntegerField(default=1)
    area = models.PositiveSmallIntegerField(default=1)


class Vivienda(models.Model):
    id_vivienda = models.CharField(max_length=50, primary_key=True)
    direccion = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio, related_name='viviendas', on_delete=models.CASCADE)
    capacidad = models.PositiveSmallIntegerField(default=1)
    pisos = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return (self.id_vivienda)


class Persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50, null=True, blank=True)
    residencia = models.ForeignKey(Vivienda, null=True, blank=True, related_name='personas_vivienda',
                                   on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, related_name='personas_municipio', on_delete=models.CASCADE)
    cabeza_familia = models.ForeignKey('Persona', null=True, blank=True, on_delete=models.CASCADE)
    telefono = models.IntegerField(null=True, blank=True)
    fecha_nacimiento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
