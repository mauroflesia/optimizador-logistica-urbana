from src.models import Interseccion, Tramo
from src.graph import RedVial
from src.dijkstra import calcular_ruta_minima

def test_calcular_ruta_minima_tramo_directo():
    red_prueba = RedVial()
    prueba_interseccion_1 = Interseccion("E1", "Rivadavia", (13.2, 43.3))
    prueba_interseccion_2 = Interseccion("E2", "San Martin", (43.1, 44.2))
    red_prueba.agregar_interseccion(prueba_interseccion_1)
    red_prueba.agregar_interseccion(prueba_interseccion_2)
    prueba_tramo = Tramo(prueba_interseccion_1.id, prueba_interseccion_2.id, 10.0, 2.5)
    red_prueba.conectar_intersecciones(prueba_tramo)
    resultado = calcular_ruta_minima(red_prueba, prueba_interseccion_1.id, prueba_interseccion_2.id, criterio="distancia")
    assert resultado.costo_total == 10.0
    assert resultado.camino == ["E1", "E2"]
