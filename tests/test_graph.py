from src.graph import RedVial
from src.models import Interseccion, Tramo
import pytest 


def test_agregar_interseccion_existosamente():
    prueba_interseccion = Interseccion("E1", "San Martin", (23, 45))
    prueba_red = RedVial()
    prueba_red.agregar_interseccion(prueba_interseccion)
    assert prueba_interseccion.id in prueba_red.intersecciones
    assert prueba_red._adyacencias[prueba_interseccion.id] == []

def test_agregar_interseccion_duplicado_error():
    prueba_interseccion = Interseccion("D4", "Rivadavia", (23.44, 55.22))
    prueba_red = RedVial()
    prueba_red.agregar_interseccion(prueba_interseccion)
    prueba_interseccion_2 = Interseccion("D4", "San Martin", (33.53, 66.12))
    with pytest.raises(ValueError, match=f"ID {prueba_interseccion_2.id}"):
        prueba_red.agregar_interseccion(prueba_interseccion_2)

def test_conectar_intersecciones_exitosamente():
    prueba_interseccion_1 = Interseccion("E1", "Corrientes", (42.45, 78.31))
    prueba_interseccion_2 = Interseccion("K1", "Rivadavia", (11.45, 81.45))
    prueba_red = RedVial()
    prueba_red.agregar_interseccion(prueba_interseccion_1)
    prueba_red.agregar_interseccion(prueba_interseccion_2)
    prueba_tramo = Tramo(prueba_interseccion_1.id, prueba_interseccion_2.id, 101.43, 3.11)
    prueba_red.conectar_intersecciones(prueba_tramo)
    tramos = prueba_red.obtener_tramos_desde(prueba_interseccion_1.id)
    assert len(tramos) == 1
    assert tramos[0] == prueba_tramo
    assert len(prueba_red.obtener_tramos_desde(prueba_interseccion_2.id)) == 0

def test_conectar_intersecciones_id_inexistente_error():
    prueba_red = RedVial()
    prueba_interseccion_1 = Interseccion("E1", "Corrientes", (42.45, 78.31))
    prueba_red.agregar_interseccion(prueba_interseccion_1)
    prueba_tramo = Tramo(prueba_interseccion_1.id, "E_INEXISTENTE" , 100, 4.11)
    with pytest.raises(ValueError, match="El ID de origen"):
        prueba_red.conectar_intersecciones(prueba_tramo)
