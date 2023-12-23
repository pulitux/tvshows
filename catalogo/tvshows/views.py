from django.shortcuts import render
from .models import Personaje, Catalogo, Serie

################################################################
# Pagina principal TODO poner bonita index.html (catalogo)
################################################################

catalogo = Catalogo()

def index(request):
    # global catalogo = Catalogo()
    personajes = catalogo.personajes_nombres()
    series = catalogo.series_nombres()
    contexto = {'personajes': personajes, 'series': series}
    return render(request, 'catalogo/index.html', contexto)

################################################################################################
# Vistas de personaje
#   p_lista() -> llama a index.html y pasa como contexto los personajes del catalogo (lista de objetos)
#   p_search() -> llama a index.html y pasa como contexto los personajes del catalogo que coinciden
#   p_ficha() -> llama a ficha.html (contexto objeto personaje)
#   p_add() -> añade objeto y llama a ficha.html (contexto objeto personaje)
#   p_delete() -> borra objeto y llama a index.html y pasa como contexto los personajes del catalogo
#   p_update() -> modifica objeto y llama a ficha.html (contexto objeto personaje)
################################################################################################

def p_lista(request):
    return render(request, 'personajes/index.html', {'lista': catalogo.personajes, 'all': True})

def p_search(request):
    lista = []
    search_term = request.POST['search_term']
    for personaje in catalogo.personajes:
        if search_term.lower() in personaje.nombre.lower():
            lista.append(personaje)
        elif search_term.lower() in personaje.serie.nombre.lower():
            lista.append(personaje)
    return render(request, 'personajes/index.html', {'lista': lista, 'all': False})

def p_ficha(request):
    personaje = catalogo.personaje(request.GET.get('idPersonaje'))
    return render(request, 'personajes/ficha.html', {'personaje': personaje})

def p_add(request):
    global catalogo
    personaje = Personaje()
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = request.POST['idSerie']
    personaje.add()
    catalogo.personajes = personaje.lista(catalogo)
    return render(request, 'personajes/ficha.html', {'personaje': personaje})

def p_delete(request):
    global catalogo
    personaje = catalogo.personaje(request.POST['idPersonaje'])
    personaje.delete()
    catalogo.personajes = personaje.lista(catalogo)
    return render(request, 'personajes/index.html', {'lista': catalogo.personajes, 'all': True})

def p_update(request):
    global catalogo
    personaje = catalogo.personaje(request.POST.get('idPersonaje'))
    personaje.idPersonaje = request.POST['idPersonaje']
    personaje.nombre = request.POST['nombre']
    personaje.imagen = request.POST['imagen']
    personaje.idSerie = request.POST['idSerie']
    personaje.mod()
    catalogo.personajes = personaje.lista(catalogo)
    return render(request, 'personajes/ficha.html', {'personaje': personaje})

################################################################################################
# Vistas de serie
#   s_lista() -> llama a index.html y pasa como contexto las series del catalogo (lista de objetos)
#   s_search() -> llama a index.html y pasa como contexto las series del catalogo que coinciden
#   s_ficha() -> llama a ficha.html (contexto objeto serie)
#   s_add() -> añade objeto y llama a ficha.html (contexto objeto serie)
#   s_delete() -> borra objeto y llama a index.html y pasa como contexto los series del catalogo
#   s_update() -> modifica objeto y llama a ficha.html (contexto objeto serie)
################################################################################################

def s_lista(request):
    global catalogo
    return render(request, 'series/index.html', {'lista': catalogo.series, 'all': True})

def s_search(request):
    lista = []
    search_term = request.POST['search_term']
    for serie in catalogo.series:
        if search_term.lower() in serie.nombre.lower():
            lista.append(serie)
    return render(request, 'series/index.html', {'lista': lista, 'all': False})

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
    global catalogo
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.puntuacion = request.POST['puntuacion']
    serie.anyo = request.POST['anyo']
    # s = {'idSerie': serie.idSerie,
    #      'nombre': serie.nombre,
    #      'imagen': serie.imagen,
    #      'puntuacion': serie.puntuacion,
    #      'anyo': serie.anyo}
    serie.add()
    catalogo.series = serie.lista()
    return render(request, 'series/ficha.html', {'serie': serie})

def s_delete(request):
    global catalogo
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.delete()
    catalogo.series = serie.lista()
    return render(request, 'series/index.html', {'catalogo': catalogo, 'all': True})

def s_update(request):
    global catalogo
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.puntuacion = request.POST['puntuacion']
    serie.anyo = request.POST['anyo']
    serie.mod()
    catalogo.series = serie.lista()
    return render(request, 'series/ficha.html', {'serie': serie})
