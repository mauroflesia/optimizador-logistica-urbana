from src.graph import RedVial
from src.models import Interseccion
import pytest 


def test_agregar_interseccion_existosamente():
    prueba_interseccion = Interseccion("E1", "San Martin", (23, 45))
    prueba_red = RedVial()
    prueba_red.agregar_interseccion(prueba_interseccion)
    assert prueba_interseccion.id in prueba_red.intersecciones
    assert prueba_red.adyacencias[prueba_interseccion.id] == []

def test_agregar_interseccion_duplicado_error():
    prueba_interseccion = Interseccion("D4", "Rivadavia", (23.44, 55.22))
    prueba_red = RedVial()
    prueba_red.agregar_interseccion(prueba_interseccion)
    prueba_interseccion_2 = Interseccion("D4", "San Martin", (33.53, 66.12))
    with pytest.raises(ValueError, match=f"ID {prueba_interseccion_2.id}"):
        prueba_red.agregar_interseccion(prueba_interseccion_2)