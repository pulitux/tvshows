from django.shortcuts import render
from .models import Personaje, Catalogo, Serie

################################################################
# Pagina principal TODO poner bonita index.html (catalogo)
################################################################

catalogo = Catalogo()


def index(request):
    global catalogo
    personajes = catalogo.personajes_nombres()
    series = catalogo.series_nombres()
    contexto = {'personajes': personajes, 'series': series}
    return render(request, 'catalogo/index.html', contexto)


################################################################################################
# Vistas de personaje
#   p_lista() -> llama a index.html y pasa como contexto los personajes del catálogo (lista de objetos)
#   p_search() -> llama a index.html y pasa como contexto los personajes del catálogo que coinciden
#   p_ficha() -> llama a ficha.html (contexto objeto personaje)
#   p_add() -> añade objeto y llama a ficha.html (contexto objeto personaje)
#   p_delete() -> borra objeto y llama a index.html y pasa como contexto los personajes del catalogo
#   p_update() -> modifica objeto y llama a ficha.html (contexto objeto personaje)
################################################################################################


def p_lista(request):
    return render(request, 'personajes/index.html', {'personajes': catalogo.personajes,
                                                     'series': catalogo.series,
                                                     'all': True,
                                                     })


def p_search(request):
    lista = []
    search_term = request.POST['search_term']
    for personaje in catalogo.personajes:
        if search_term.lower() in personaje.nombre.lower():
            lista.append(personaje)
        elif search_term.lower() in personaje.serie.nombre.lower():
            lista.append(personaje)
    return render(request, 'personajes/index.html', {'personajes': lista,
                                                     'series': catalogo.series,
                                                     'all': False,
                                                     })


def p_ficha(request):
    idPersonaje = request.GET.get('idPersonaje')
    for p in catalogo.personajes:
        if p.idPersonaje == int(idPersonaje):
            return render(request, 'personajes/ficha.html', {'personaje': p,
                                                             'series': catalogo.series,
                                                             })


def p_add(request):
    global catalogo
    personaje = Personaje()
    personaje.idPersonaje = catalogo.next_personaje()
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = int(request.POST['idSerie'])
    personaje.add()
    personaje.serie = catalogo.serie(personaje.idSerie)
    catalogo.personajes = personaje.lista(catalogo)
    return render(request, 'personajes/ficha.html', {'personaje': personaje,
                                                     'series': catalogo.series,
                                                     })


def p_delete(request):
    global catalogo

    personaje = catalogo.personaje(request.POST['idPersonaje'])
    personaje.delete()

    catalogo.personajes = personaje.lista(catalogo)

    return render(request, 'personajes/index.html', {'lista': catalogo.personajes,
                                                     'series': catalogo.series,
                                                     'all': True,
                                                     })


def p_update(request):
    global catalogo
    personaje = catalogo.personaje(request.POST.get('idPersonaje'))
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = request.POST['idSerie']
    personaje.mod()
    personaje.serie = catalogo.serie(personaje.idSerie)
    catalogo.personajes = personaje.lista(catalogo)

    return render(request, 'personajes/ficha.html', {'personaje': personaje,
                                                     'series': catalogo.series,
                                                     })


################################################################################################
# Vistas de serie
#   s_lista() -> llama a index.html y pasa como contexto las series del catálogo (lista de objetos)
#   s_search() -> llama a index.html y pasa como contexto las series del catálogo que coinciden
#   s_ficha() -> llama a ficha.html (contexto objeto serie)
#   s_add() -> añade objeto y llama a ficha.html (contexto objeto serie)
#   s_delete() -> borra objeto y llama a index.html y pasa como contexto los series del catalogo
#   s_update() -> modifica objeto y llama a ficha.html (contexto objeto serie)
################################################################################################

def s_lista(request):
    global catalogo

    return render(request, 'series/index.html', {'series': catalogo.series,
                                                                     'all': True,
                                                                     })


def s_search(request):
    global catalogo
    lista = []

    search_term = request.POST['search_term']
    for serie in catalogo.series:
        if search_term.lower() in serie.nombre.lower():
            lista.append(serie)

    return render(request, 'series/index.html', {'series': lista,
                                                                     'all': False,
                                                                     })


def s_ficha(request):
    idSerie = request.GET.get('idSerie')
    for s in catalogo.series:
        if s.idSerie == int(idSerie):
            return render(request, 'series/ficha.html', {'serie': s,
                                                                            })


def s_add(request):
    global catalogo
    serie = Serie()

    serie.idSerie = catalogo.next_serie()
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.puntuacion = request.POST['puntuacion']
    serie.anyo = request.POST['anyo']
    serie.add()

    catalogo.series = serie.lista(catalogo)

    return render(request, 'series/ficha.html', {'serie': serie,
                                                                    })


def s_delete(request):
    global catalogo

    serie = catalogo.personaje(request.POST['idSerie'])
    serie.delete()

    catalogo.series = serie.lista(catalogo)

    return render(request, 'series/index.html', {'catalogo': catalogo,
                                                                     'all': True,
                                                                     })


def s_update(request):
    global catalogo
    serie = Serie()

    serie.idSerie = request.POST['idSerie']
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.puntuacion = request.POST['puntuacion']
    serie.anyo = request.POST['anyo']
    serie.mod()

    catalogo.series = serie.lista(catalogo)
    serie.personajes = []
    for p in catalogo.personajes:
        if serie.idSerie == p.idSerie:
            if p not in serie.personajes:
                serie.personajes.append(p)

    return render(request, 'series/ficha.html', {'serie': serie,
                                                                    })
