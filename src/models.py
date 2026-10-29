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

@dataclass
class Ruta:
    costo_total: float
    camino: list[str]