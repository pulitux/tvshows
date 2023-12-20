from django.shortcuts import render, HttpResponse
from .models import Personaje, Catalogo

import requests
import json

catalogo = Catalogo()

def index(request):
    # contexto = {'lista': catalogo.personajes,
    #             'all': True}
    return render(request, 'catalogo/index.html')


def p_lista(request):
    contexto = {'catalogo': catalogo,
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
    id = request.GET.get('id')
    personaje.read(id)
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


def p_delete(request):
    personaje = Personaje()
    personaje.idPersonaje = request.GET.get('id')
    personaje.delete()
    catalogo = Catalogo()
    contexto = {'catalogo': catalogo,
                'all': True}
    return render(request, 'personajes/index.html', contexto)


def p_update(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = request.POST['idSerie']
    personaje.mod()
    return render(request, 'personaje/ficha.html', {'idPersonaje': personaje.idPersonaje})
