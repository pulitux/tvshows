from django.db import models
import requests
import json

class Catalogo:
    def __init__(self):
        p = Personaje()
        self.personajes = p.lista()

    def personajes_tabla(self):
        t = []
        for p in self.personajes:
            i = {'idPeronaje': p.idPersonaje,
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
        self.idPersonaje = None

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
        print (lista)
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
                #print("Entire JSON response")
                #print(jsonResponse)
            except:
                print(f'Other error occurred: {err}')

    def add(self): # post
        url = self.api_url
        personaje = {'idPersonaje': int(self.idPersonaje),
                     'nombre': self.nombre.capitalize(),
                     'imagen': self.imagen,
                     'idSerie': int(self.idSerie)}
        response = requests.post(url, json=personaje)
        print (response.status_code)
        print (response)
        # personaje = requests.get(url)
        # return personaje['idPersonaje']

    def mod(self): # put
        url = self.api_url
        personaje = {'idPersonaje': self.idPersonaje,
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'idSerie': self.idSerie}
        response = requests.put(url, json=personaje)
        return response.status_code

    def delete(self): # delete
        url = self.api_url + "/" + self.idPersonaje
        response = requests.delete(url)
        return response.status_code