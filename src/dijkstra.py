import heapq
from .graph import RedVial
from .models import Ruta

def calcular_ruta_minima(red: RedVial, origen_id: str, destino_id: str, criterio: str = "distancia") -> Ruta | None:
    if origen_id not in red.intersecciones or destino_id not in red.intersecciones:
        raise ValueError("El origen o el destino no existen en la red")
    if criterio not in ("distancia", "tiempo"):
        raise ValueError(f"El criterio '{criterio}' no es valido")
    cola_prioridad = [(0.0, origen_id)]
    distancias = {origen_id: 0.0}
    predecesores = {origen_id: None}
    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        if nodo_actual == destino_id:
            break
        for tramo in red.obtener_tramos_desde(nodo_actual):
            if criterio == "distancia":
                nuevo_costo = costo_actual + tramo.distancia
            else:
                nuevo_costo = costo_actual + tramo.tiempo_estimado
            vecino_id = tramo.destino_id
            if nuevo_costo < distancias.get(vecino_id, float("inf")):
                distancias[vecino_id] = nuevo_costo
                predecesores[vecino_id] = nodo_actual
                heapq.heappush(cola_prioridad, (nuevo_costo, vecino_id))
    if destino_id not in distancias:
        return None
    camino = []
    actual = destino_id
    while actual is not None:
        camino.append(actual)
        actual = predecesores[actual]
    camino.reverse()
    return Ruta(costo_total=distancias[destino_id], camino=camino)