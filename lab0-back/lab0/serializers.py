from rest_framework import serializers
from .models import Vivienda, Municipio, Persona
from drf_writable_nested import WritableNestedModelSerializer 

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id_persona', 'nombre', 'sexo', 'telefono', 'fecha_nacimiento']


class ViviendaSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    personas_vivienda = PersonaSerializer(many=True)
    class Meta:
        model = Vivienda
        fields = ['id_vivienda', 'direccion', 'capacidad','pisos', 'personas_vivienda']

class MunicipioSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    viviendas = ViviendaSerializer(many=True)
    
    class Meta:
        model = Municipio
        fields = ['id_municipio', 'nombre_municipio', 'poblacion', 'area', 'viviendas']

