#from django.shortcuts import render

# Create your views here.
# ! compia
from django.http import HttpResponse

def index(request):
    return HttpResponse("Si funciono Pa!")
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# ! co,
from rest_framework.decorators import api_view
from rest_framework.response import Response
from interpreter import ejecutar_minilang  # importa tu función

@api_view(['POST'])
def run_minilang(request):
    try:
        codigo = request.data.get('codigo', '')
        if not codigo:
            return Response({"error": "No se recibió ningún código."})

        resultado = ejecutar_minilang(codigo)
        if resultado is None:
            resultado = "(sin salida)"  # por si tu intérprete no retorna nada explícito

        return Response({"resultado": str(resultado)})

    except Exception as e:
        return Response({"error": str(e)})
from django.shortcuts import render

def web_index(request):
    return render(request, 'index.html')

