from django.db import models
import requests
import json

class Personaje:
    api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Personajes'

    def __init__(self): #, idPersonaje = 0):
        # self.idPersonaje = idPersonaje
        pass

    def read(self): # get
        url = self.api_url + "/" + self.idPersonaje

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