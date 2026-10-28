from src.graph import RedVial
from src.models import Interseccion



def test_agregar_interseccion_existosamente():
    prueba_interseccion = Interseccion("E1", "San Martin", (23, 45))
    prueba_red = RedVial()
    prueba_red.agregar_interseccion(prueba_interseccion)
    assert prueba_interseccion.id in prueba_red.intersecciones
    assert prueba_red.adyacencias[prueba_interseccion.id] == []