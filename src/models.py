from dataclasses import dataclass

@dataclass
class Interseccion:
    id: str
    nombre: str
    coordenadas: tuple[float, float]

@dataclass
class Tramo:
    origen_id: str
    destino_id: str
    distancia: float
    tiempo_estimado: float

class RedVial:
    def __init__(self):
        self.intersecciones: dict [str, Interseccion] = {}
        self.adyacencias: dict [str, list[Tramo]] = {}

    def agregar_interseccion(self, interseccion: Interseccion)-> None:
        if interseccion.id in self.intersecciones:
            raise ValueError("Esta interseccion ya existe")
        self.intersecciones[interseccion.id] = interseccion
        self.adyacencias[interseccion.id] = []