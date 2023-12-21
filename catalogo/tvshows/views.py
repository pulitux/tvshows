from django.shortcuts import render, HttpResponse
from .models import Personaje, Catalogo, Serie

import requests
import json

catalogo = Catalogo()

# Pagina principal TODO
def index(request):
    # contexto = {'lista': catalogo.personajes,
    #             'all': True}
    return render(request, 'catalogo/index.html')

# Vistas de personaje

def p_lista(request):
    catalogo = Catalogo()
    contexto = {'lista': catalogo.personajes,
                'all': True}
    return render(request, 'personajes/index.html', contexto)

def p_search(request):
    lista = []
    search_term = request.POST['search_term']
    catalogo = Catalogo()
    for personaje in catalogo.personajes:
        if search_term.lower() in personaje.nombre.lower():
            lista.append(personaje)
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
         'idPersonaje': personaje.idPersonaje}
    return render(request, 'personajes/ficha.html', {'personaje': personaje})


def p_add(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idPersonaje = request.POST['idPersonaje']
    p = {'idPersonaje': personaje.idPersonaje,
         'nombre': personaje.nombre,
         'imagen': personaje.imagen,
         'idPersonaje': personaje.idPersonaje}
    print(p)
    personaje.add()
    catalogo = Catalogo()
    return render(request, 'personajes/ficha.html', p)

def p_delete(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.delete()
    catalogo = Catalogo()
    return render(request, 'personajes/index.html', {'catalogo': catalogo, 'all': True})

def p_update(request):
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = request.POST['idSerie']
    print (personaje)
    personaje.mod()
    catalogo = Catalogo()
    return render(request, 'personajes/ficha.html', {'personaje': personaje})

# Vistas de serie
def s_lista(request):
    catalogo = Catalogo()
    contexto = {'lista': catalogo.series,
                'all': True}
    return render(request, 'series/index.html', contexto)

def s_search(request):
    lista = []
    search_term = request.POST['search_term']
    # url = 'https://apiseriesseries.azurewebsites.net/api/Series'
    # response = requests.get(url)
    # series = response.json()
    catalogo = Catalogo()
    for serie in catalogo.series:
        if search_term.lower() in serie.nombre.lower():
            lista.append(serie)
    contexto = {'lista': lista,
                'all': False}
    return render(request, 'series/index.html', contexto)

def s_ficha(request):
    serie = Serie()
    id = request.GET.get('id')
    serie.read(id)
    s = {'idSerie': serie.idSerie,
         'nombre': serie.nombre,
         'imagen': serie.imagen,
         'puntuacion': serie.puntuacion,
         'anyo': serie.anyo}
    return render(request, 'series/ficha.html', {'serie': serie})


def s_add(request):
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.idSerie = request.POST['idSerie']
    s = {'idSerie': serie.idSerie,
         'nombre': serie.nombre,
         'imagen': serie.imagen,
         'puntuacion': serie.puntuacion,
         'anyo': serie.anyo}
    print(s)
    serie.add()
    catalogo = Catalogo()
    return render(request, 'series/ficha.html', s)

def s_delete(request):
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.delete()
    catalogo = Catalogo()
    return render(request, 'series/index.html', {'catalogo': catalogo, 'all': True})

def s_update(request):
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.puntuacion = request.POST['puntuacion']
    serie.anyo = request.POST['anyo']
    print (serie)
    serie.mod()
    catalogo = Catalogo()

    return render(request, 'series/ficha.html', {'serie': serie})

# def p_read(request):
#     personaje = Personaje()
#     idPersonaje = request.POST['idPersonaje']
#     personaje.read(idPersonaje)

