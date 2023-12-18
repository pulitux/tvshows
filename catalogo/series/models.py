from django.db import models
import requests
import json

class Serie:
    api_url = 'https://apiseriesseries.azurewebsites.net/api/series'

    def __init__(self): #, idSerie = 0):
        # self.idSerie = idSerie
        pass

    def read(self): # get
        url = self.api_url + "/" + self.idSerie

        try:
            response = requests.get(url)
            response.raise_for_status()
            serie = response.json()
            self.idSerie = serie['idSerie']
            self.nombre = serie['nombre']
            self.imagen = serie['imagen']
            self.puntuacion = serie['puntuacion']
            self.anyo = serie['anyo']
            print("Entire JSON response")
            print(jsonResponse)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def add(self): # post
        url = self.api_url
        serie = {'idSerie': self.idSerie,
                    'nombre': self.nombre,
                    'imagen': self.imagen,
                    'puntuacion': self.puntuacion,
                    'anyo': self.anyo}
        response = requests.post(url, json=serie)
        return response.status_code

    def mod(self): # put
        url = self.api_url
        serie = {'idSerie': self.idSerie,
                    'nombre': self.nombre,
                    'imagen': self.imagen,
                    'puntuacion': self.puntuacion,
                    'anyo': self.anyo}
        response = requests.put(url, json=serie)
        return response.status_code

    def delete(self): # delete
        url = self.api_url + "/" + self.idSerie
        response = requests.delete(url)
        return response.status_code