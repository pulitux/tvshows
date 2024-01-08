import requests


class Catalogo:
    def __init__(self):
        self.series = []
        self.personajes = []
        p = Personaje()
        s = Serie()
        self.series = s.lista(self)
        self.personajes = p.lista(self)

    def personaje(self, idPersonaje):
        for p in self.personajes:
            if int(p.idPersonaje) == int(idPersonaje):
                return p
        return None

    def next_personaje(self):
        p_next = 0
        for p in self.personajes:
            if int(p.idPersonaje) > int(p_next):
                p_next = int(p.idPersonaje)
        return p_next + 1

    def next_serie(self):
        s_next = 0
        for s in self.series:
            if int(s.idSerie) > int(s_next):
                s_next = int(s.idSerie)
        return s_next + 1

    def personajes_nombres(self):
        lista = []
        for p in self.personajes:
            lista.append(p.nombre)
        lista.sort()
        return lista

    def serie(self, idSerie):
        for s in self.series:
            if s.idSerie == idSerie:
                return s
        return None

    def series_nombres(self):
        lista = []
        for s in self.series:
            lista.append(s.nombre)
        lista.sort()
        return lista


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
        for serie in catalogo.series:
            serie.personajes = []
        for personaje in personajes:
            p = Personaje()
            p.idPersonaje = personaje['idPersonaje']
            p.nombre = personaje['nombre']
            p.imagen = personaje['imagen']
            p.idSerie = personaje['idSerie']
            p.serie = catalogo.serie(p.idSerie)
            for s in catalogo.series:
                if s.idSerie == p.idSerie:
                    if p not in s.personajes:
                        s.personajes.append(p)
            lista.append(p)
        lista.sort(key=lambda x: x.nombre)
        return lista

    def add(self):
        self.nombre = ' '.join(list(n.capitalize() for n in self.nombre.split()))
        self.idSerie = int(self.idSerie)
        personaje = {'idPersonaje': self.idPersonaje,
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'idSerie': self.idSerie,
                     }
        requests.post(self.api_url, json=personaje)

    def mod(self):
        self.idPersonaje = int(self.idPersonaje)
        self.nombre = ' '.join(list(n.capitalize() for n in self.nombre.split()))
        self.idSerie = int(self.idSerie)
        personaje = {'idPersonaje': self.idPersonaje,
                     'nombre': self.nombre,
                     'imagen': self.imagen,
                     'idSerie': self.idSerie,
                     }
        requests.put(self.api_url, json=personaje)

    def delete(self):
        url = self.api_url + "/" + str(self.idPersonaje)
        requests.delete(url)


class Serie:
    api_url = 'https://apiseriespersonajes.azurewebsites.net/api/Series'

    def __init__(self):
        self.idSerie = None
        self.nombre = None
        self.imagen = None
        self.puntuacion = None
        self.anyo = None
        self.personajes = []

    def lista(self, catalogo):
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
            s.personajes = []
            for p in catalogo.personajes:
                if s.idSerie == p.idSerie:
                    if p not in s.personajes:
                        s.personajes.append(p)
            lista.append(s)
        lista.sort(key=lambda x: x.nombre)
        return lista

    def add(self):
        self.idSerie = int(self.idSerie)
        self.nombre = ' '.join(list(n.capitalize() for n in self.nombre.split()))
        self.puntuacion = int(self.puntuacion)
        self.anyo = int(self.anyo)
        serie = {'idSerie': self.idSerie,
                 'nombre': self.nombre,
                 'imagen': self.imagen,
                 'puntuacion': self.puntuacion,
                 'anyo': self.anyo}
        requests.post(self.api_url, json=serie)

    def mod(self):
        self.idSerie = int(self.idSerie)
        self.nombre = ' '.join(list(n.capitalize() for n in self.nombre.split()))
        self.puntuacion = int(self.puntuacion)
        self.anyo = int(self.anyo)
        serie = {'idSerie': self.idSerie,
                 'nombre': self.nombre,
                 'imagen': self.imagen,
                 'puntuacion': self.puntuacion,
                 'anyo': self.anyo}
        requests.put(self.api_url, json=serie)

    def delete(self):
        url = self.api_url + "/" + self.idSerie
        requests.delete(url)
