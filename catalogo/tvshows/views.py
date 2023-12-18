from django.shortcuts import render
from .models import Personaje

import requests
import json


def p_lista(request):
    lista = []
    url = 'https://apiseriespersonajes.azurewebsites.net/api/Personajes'
    response = requests.get(url)
    personajes = response.json()
    for personaje in personajes:
        lista.append((personaje['idPersonaje'],
                      personaje['nombre'],
                      personaje['imagen'],
                      personaje['idSerie']))
    contexto = {'lista': lista,
                'all': True}
    return render(request, 'personajes/index.html', contexto)


def p_search(request):
    lista = []
    search_term = request.POST['search_term']
    url = 'https://apiseriespersonajes.azurewebsites.net/api/Personajes'
    response = requests.get(url)
    personajes = response.json()
    for personaje in personajes:
        if search_term.lower() in search_term in personaje['nombre'].lower():
            lista.append((personaje['idPersonaje'],
                          personaje['nombre'],
                          personaje['imagen'],
                          personaje['idSerie']))
    contexto = {'lista': lista,
                'all': False}
    return render(request, 'personajes/index.html', contexto)


def p_ficha(request):
    personaje = Personaje()
    personaje.idPersonaje = request.GET.get('id')
    personaje.read()
    p = {'idPersonaje': personaje.idPersonaje,
         'nombre': personaje.nombre,
         'imagen': personaje.imagen,
         'idSerie': personaje.idSerie}
    return render(request, 'personajes/ficha.html', p)


def p_read(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.read()
    # p = {'idPersonaje': personaje.idPersonaje,
    #      'nombre': personaje.nombre,
    #      'imagen': personaje.imagen,
    #      'idSerie': personaje.idSerie}
    # return render(request, 'personajes/ficha.html', p)


def p_add(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = request.POST['idSerie']
    p = {'idPersonaje': personaje.idPersonaje,
         'nombre': personaje.nombre,
         'imagen': personaje.imagen,
         'idSerie': personaje.idSerie}
    personaje.add()

    return render(request, 'personajes/ficha.html', p)



def p_operate(request):
    op = request.POST['operacion']
    if op == 'delete':
        p_delete(request)
    elif op == 'update':
        p_update(request)
    else:
        pass
    return render(request, 'personajes/mod.html')

def p_delete(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.delete()
    return render(request, 'personaje/index.html')


def p_update(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = request.POST['idSerie']
    personaje.mod()
    return render(request, 'personaje/ficha.html', {'idPersonaje': personaje.idPersonaje})
