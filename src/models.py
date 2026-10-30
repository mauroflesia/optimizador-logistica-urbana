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

@dataclass
class Pedido:
    id: str
    destino_id: str
    peso: float
    def __post_init__(self) -> None:
        if self.peso <= 0:
            raise ValueError("El peso del pedido debe ser mayor a cero")

@dataclass
class Vehiculo:
    deposito_id: str
    carga_maxima: float
    def __post_init__(self) -> None:
        if self.carga_maxima <= 0:
            raise ValueError("La carga maxima del vehiculo debe ser mayor a cero")
