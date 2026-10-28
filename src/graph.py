from .models import Interseccion, Tramo

class RedVial:
    def __init__(self) -> None:
        self.intersecciones: dict[str, Interseccion] = {}
        self.adyacencias: dict[str, list[Tramo]] = {}

    def agregar_interseccion(self, interseccion: Interseccion)-> None:
        """Agrega una interseccion a la red.

        Args:
            interseccion: Es una esquina compuesta por 2 o mas calles.
        Raises:
            ValueError: Cuando la interseccion ya existe en la red.
        """
        if interseccion.id in self.intersecciones:
            raise ValueError( f"La interseccion con ID {interseccion.id} ya existe en la red")
        self.intersecciones[interseccion.id] = interseccion
        self.adyacencias[interseccion.id] = []

    def conectar_intersecciones(self, tramo: Tramo) -> None:
        """Conecta 2 intersecciones siempre que se respete el sentido de conduccion.

        Args:
            tramo: Es una calle por la que podemos transitar con un determinado sentido.
        Raises:
            ValueError: Ocasionado por Invalidez del ID de origen o del ID de destino. Tambien es ocasionado porque ya sea la distancia o el tiempo estimado son 
            menores o iguales a 0.
        """
        if tramo.origen_id not in self.intersecciones or tramo.destino_id not in self.intersecciones:
            raise ValueError("El ID de origen o el ID de destino no estan en la red")
        if tramo.distancia <= 0 or tramo.tiempo_estimado <= 0:
            raise ValueError("El tiempo estimado y la distancia deben ser mayores a cero") 
        self.adyacencias[tramo.origen_id].append(tramo)

    def obtener_vecinos(self, interseccion_id: str) -> list[Tramo]:
        """Devuelve la lista de tramos asociada a determinada interseccion.

        Args: 
            interseccion_id: Es el identificador de una determinada interseccion.
        Returns:
            Una copia independiente de la lista de tramos para determinada interseccion.
        Raises:
            ValueError: Ocasionado cuando ingresamos un ID de interseccion que no existe en la red.
        """
        if interseccion_id not in self.intersecciones:
            raise ValueError(f"La interseccion {interseccion_id} no existe en la red")
        return self.adyacencias[interseccion_id].copy()