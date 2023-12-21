from django.db import models
import requests
import json

class Catalogo:
    def __init__(self):
        p = Personaje()
        s = Serie()
        self.personajes = p.lista()
        self.series = s.lista()

    def personajes_tabla(self):
        t = []
        for p in self.personajes:
            i = {'idPersonaje': p.idPersonaje,
                 'nombre': p.nombre,
                 'imagen': p.imagen,
                 'idSerie': p.idSerie}
            t.append(i)
        return t

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


class Personaje:
    api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Personajes'

    def __init__(self): #, idPersonaje = 0):
        self.idPersonaje = None
        self.nombre = None
        self.imagen = None
        self.idSerie = None

    def lista(self):
        lista = []
        response = requests.get(self.api_url)
        personajes = response.json()
        for personaje in personajes:
            p = Personaje()
            p.idPersonaje = personaje['idPersonaje']
            p.nombre = personaje['nombre']
            p.imagen = personaje['imagen']
            p.idSerie = personaje['idSerie']
            lista.append(p)
        # contexto = {'lista': lista,
        #             'all': True}
        return lista

    def read(self, id=None): # get
        if id:
            url = self.api_url + "/" + id

            try:
                response = requests.get(url)
                response.raise_for_status()
                personaje = response.json()
                self.idPersonaje = personaje['idPersonaje']
                self.nombre = personaje['nombre']
                self.imagen = personaje['imagen']
                self.idSerie = personaje['idSerie']
            except:
                print(f'Other error occurred: {err}')

    def add(self): # post
        # url = self.api_url
        personaje = {'idPersonaje': int(self.idPersonaje),
                     'nombre': self.nombre.capitalize(),
                     'imagen': self.imagen,
                     'idSerie': int(self.idSerie)}
        response = requests.post(self.api_url, json=personaje)

    def mod(self): # put
        url = self.api_url
        print (type(self.idSerie))
        personaje = {'idPersonaje': int(self.idPersonaje),
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'idSerie': int(self.idSerie)}
        response = requests.put(url, json=personaje)
        return response.status_code

    def delete(self): # delete
        url = self.api_url + "/" + self.idPersonaje
        response = requests.delete(url)
        return response.status_code

class Serie:
    api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Series'

    def __init__(self): #, idSerie = 0):
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
        # contexto = {'lista': lista,
        #             'all': True}
        return lista

    def read(self, id=None): # get
        if id:
            url = self.api_url + "/" + id

            try:
                response = requests.get(url)
                response.raise_for_status()
                serie = response.json()
                self.idSerie = serie['idSerie']
                self.nombre = serie['nombre']
                self.imagen = serie['imagen']
                self.puntuacion = serie['puntuacion']
                self.anyo = serie['anyo']
            except:
                print(f'Other error occurred: {err}')

    def add(self): # post
        # url = self.api_url
        serie = {'idSerie': int(self.idSerie),
                 'nombre': self.nombre.capitalize(),
                 'imagen': self.imagen,
                 'puntuacion': int(self.puntuacion),
                 'anyo': int(self.anyo)}
        response = requests.post(self.api_url, json=serie)

    def mod(self): # put
        url = self.api_url
        serie = {'idSerie': int(self.idSerie),
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'puntuacion': int(self.puntuacion),
                     'anyo': int(self.anyo)}
        response = requests.put(url, json=serie)
        return response.status_code

    def delete(self): # delete
        url = self.api_url + "/" + self.idSerie
        response = requests.delete(url)
        return response.status_code
