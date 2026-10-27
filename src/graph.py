from .models import Interseccion, Tramo

class RedVial:
    def __init__(self) -> None:
        self.intersecciones: dict[str, Interseccion] = {}
        self.adyacencias: dict[str, list[Tramo]] = {}

    def agregar_interseccion(self, interseccion: Interseccion)-> None:
        if interseccion.id in self.intersecciones:
            raise ValueError("La interseccion ya existe")
        self.intersecciones[interseccion.id] = interseccion
        self.adyacencias[interseccion.id] = []

    def conectar_intersecciones(self, tramo: Tramo) -> None:
        if tramo.origen_id not in self.intersecciones or tramo.destino_id not in self.intersecciones:
            raise ValueError("El ID de origen o el ID de destino no estan en la red")
        if tramo.distancia <= 0 or tramo.tiempo_estimado <= 0:
            raise ValueError("El tiempo estimado y la distancia deben ser mayores a cero") 
        self.adyacencias[tramo.origen_id].append(tramo)

    def obtener_vecinos(self, interseccion_id: str) -> list[Tramo]:
        if interseccion_id not in self.intersecciones:
            raise ValueError(f"La interseccion {interseccion_id} no existe en la red")
        return self.adyacencias[interseccion_id].copy()