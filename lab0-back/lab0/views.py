from django.http import JsonResponse
from .models import Vivienda, Municipio, Persona
from .serializers import ViviendaSerializer, MunicipioSerializer, PersonaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#---------- M U N I C I P I O S -----------------

#Consulta todos los municipios o Crea un nuevo municipio
@api_view(['GET', 'POST'])
def municipio_list(request):
    if request.method == 'GET':
        municipio = Municipio.objects.all()
        serializador = MunicipioSerializer(municipio, many=True)
        return Response(serializador.data)
    
    if request.method == 'POST':
        serializador = MunicipioSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)

#Consulta, Actualiza o Borra un municipio segun su id        
@api_view(['GET','PUT','DELETE'])
def municipio_detail(request, id):
    try:
        municipio = Municipio.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializador = MunicipioSerializer(municipio)
        return Response(serializador.data)
    elif request.method == 'PUT':
        serializador = MunicipioSerializer(municipio, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#---------- V I V I E N D A S -----------------

#Consulta todos las viviendas o Crea una nueva vivienda
@api_view(['GET', 'POST'])
def vivienda_list(request):
    if request.method == 'GET':
        #obtengo viviendas
        viviendas = Vivienda.objects.all()

        #las serializo
        serializador = ViviendaSerializer(viviendas, many=True)

        #retorno el json
        return Response(serializador.data)
    
    if request.method == 'POST':
        serializador = ViviendaSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def vivienda_detail(request, id):
    try:
        vivi = Vivienda.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializador = ViviendaSerializer(vivi)
        return Response(serializador.data)
    elif request.method == 'PUT':
        serializador = ViviendaSerializer(vivi, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vivi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#---------- P E R S O N A S -----------------

#Consulta todos los pernonas o Crea un nuevo persona
@api_view(['GET', 'POST'])
def persona_list(request):
    if request.method == 'GET':
        persona = Persona.objects.all()
        serializador = PersonaSerializer(persona, many=True)
        return Response(serializador.data)
    
    if request.method == 'POST':
        serializador = PersonaSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)

#Consulta, Actualiza o Borra un municipio segun su id        
@api_view(['GET','PUT','DELETE'])
def persona_detail(request, id):
    try:
        persona = Persona.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializador = PersonaSerializer(persona)
        return Response(serializador.data)
    elif request.method == 'PUT':
        serializador = PersonaSerializer(persona, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)