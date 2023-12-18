from django.shortcuts import render
from models import Serie

def lista(request):
    pass

def ficha(request):
    pass

def read(request):
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.read()
    s = {'idSerie': serie.idSerie,
         'nombre': serie.nombre,
         'imagen': serie.imagen,
         'puntuacion': serie.puntuacion,
         'anyo': serie.anyo}
    return render(request, 'serie/ficha.html', {'serie': serie})

def add(request):
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.puntuacion = request.POST['puntuacion']
    serie.anyo = request.POST['anyo']
    serie.add()
    return render(request, 'serie/ficha.html', {'idSerie': serie.idSerie})

def delete(request):
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.delete()
    return render(request, 'serie/index.html')

def mod(request):
    serie = Serie()
    serie.idSerie = request.POST['idSerie']
    serie.nombre = request.POST['nombre']
    serie.imagen = request.POST['imagen']
    serie.idSerie = request.POST['idSerie']
    serie.mod()
    return render(request, 'serie/ficha.html', {'idSerie': serie.idSerie})

