from django.db import models
import requests
import json

class Catalogo:
    def __init__(self):
        p = Personaje()
        s = Serie()
        self.series = s.lista()
        self.personajes = p.lista(self)

    # def personajes_tabla(self):
    #     t = []
    #     for p in self.personajes:
    #         i = {'idPersonaje': p.idPersonaje,
    #              'nombre': p.nombre,
    #              'imagen': p.imagen,
    #              'idSerie': p.idSerie}
    #         t.append(i)
    #     return t

    def personaje(self, idPersonaje):
        for p in self.personajes:
            print (p.idPersonaje)
            if int(p.idPersonaje) == int(idPersonaje):
                return p
        return None

    def personajes_ids(self):
        l = []
        for p in self.personajes:
            i = p.idPersonaje
            l.append(i)
        return l

    def personajes_nombres(self):
        l = []
        for p in self.personajes:
            n = p.nombre
            l.append(n)
        return l

    def personajes_imagenes(self):
        l = []
        for p in self.personajes:
            i = p.imagen
            l.append(i)
        return l

    def personajes_idsSerie(self):
        l = []
        for p in self.personajes:
            i = p.idSerie
            l.append(i)
        return l

    def serie(self, idSerie):
        for s in self.series:
            if s.idSerie == idSerie:
                return s
        return None

class Personaje:
    api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Personajes'

    def __init__(self):
        self.idPersonaje = None
        self.nombre = None
        self.imagen = None
        self.idSerie = None
        self.serie = None

    def lista(self, catalogo):
        lista = []
        response = requests.get(self.api_url)
        personajes = response.json()
        for personaje in personajes:
            p = Personaje()
            p.idPersonaje = personaje['idPersonaje']
            p.nombre = personaje['nombre']
            p.imagen = personaje['imagen']
            p.idSerie = personaje['idSerie']
            p.serie = catalogo.serie(p.idSerie)
            lista.append(p)
        return lista

    # def read(self, id=None): # get
    #     if id:
    #         url = self.api_url + "/" + id
    #
    #         try:
    #             response = requests.get(url)
    #             response.raise_for_status()
    #             personaje = response.json()
    #             self.idPersonaje = personaje['idPersonaje']
    #             self.nombre = personaje['nombre']
    #             self.imagen = personaje['imagen']
    #             self.idSerie = personaje['idSerie']
    #         except:
    #             print(f'Other error occurred: {err}')

    def add(self):
        self.idPersonaje = int(self.idPersonaje)
        self.nombre = ' '.join(list(n.capitalize() for n in self.nombre.split()))
        self.idSerie = int(self.idSerie)
        personaje = {'idPersonaje': self.idPersonaje,
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'idSerie': self.idSerie}
        requests.post(self.api_url, json=personaje)

    def mod(self): # put
        self.idPersonaje = int(self.idPersonaje)
        self.nombre = ' '.join(list(n.capitalize() for n in self.nombre.split()))
        self.idSerie = int(self.idSerie)
        personaje = {'idPersonaje': self.idPersonaje,
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'idSerie': self.idSerie}
        requests.put(self.api_url, json=personaje)

    def delete(self): # delete
        url = self.api_url + "/" + str(self.idPersonaje)
        requests.delete(url)

class Serie:
    api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Series'

    def __init__(self, idSerie = None):
        if idSerie:
            self.read(idSerie)
        else:
            self.idSerie = None
            self.nombre = None
            self.imagen = None
            self.puntuacion = None
            self.anyo = None

    def lista(self):
        lista = []
        response = requests.get(self.api_url)
        series = response.json()
        for serie in series:
            s = Serie()
            s.idSerie = serie['idSerie']
            s.nombre = serie['nombre']
            s.imagen = serie['imagen']
            s.puntuacion = serie['puntuacion']
            s.anyo = serie['anyo']
            lista.append(s)
        return lista

    def read(self, id=None):
        if id:
            url = self.api_url + "/" + str(id)
            try:
                response = requests.get(url)
                response.raise_for_status()
                serie = response.json()
                self.idSerie = serie['idSerie']
                self.nombre = serie['nombre']
                self.imagen = serie['imagen']
                self.puntuacion = serie['puntuacion']
                self.anyo = serie['anyo']
                return True
            except:
                return False
        return False

    def add(self):
        self.idSerie = int(self.idSerie)
        self.nombre = self.nombre.capitalize()
        self.puntuacion = int(self.puntuacion)
        self.anyo = int(self.anyo)
        serie = {'idSerie': self.idSerie,
                 'nombre': self.nombre,
                 'imagen': self.imagen,
                 'puntuacion': self.puntuacion,
                 'anyo': self.anyo}
        requests.post(self.api_url, json=serie)

    def mod(self): # put
        self.idSerie = int(self.idSerie)
        self.nombre = self.nombre.capitalize()
        self.puntuacion = int(self.puntuacion)
        self.anyo = int(self.anyo)
        serie = {'idSerie': self.idSerie,
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'puntuacion': self.puntuacion,
                     'anyo': self.anyo}
        requests.put(self.api_url, json=serie)

    def delete(self): # delete
        url = self.api_url + "/" + self.idSerie
        requests.delete(url)
