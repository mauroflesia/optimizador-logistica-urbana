from src.models import Interseccion, Tramo
from src.graph import RedVial
from src.dijkstra import calcular_ruta_minima
import pytest

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

def test_calcular_ruta_minima_elige_camino_optimo_segun_criterio():
    prueba_red = RedVial()
    prueba_interseccion_1 = Interseccion("A", "Rivadavia", (13.2, 43.3))
    prueba_interseccion_2 = Interseccion("B", "San Martin", (56.4, 11.2))
    prueba_interseccion_3 = Interseccion("C", "25 de Mayo", (34.1, 9.2))
    prueba_red.agregar_interseccion(prueba_interseccion_1)
    prueba_red.agregar_interseccion(prueba_interseccion_2)
    prueba_red.agregar_interseccion(prueba_interseccion_3)
    prueba_tramo_1 = Tramo(prueba_interseccion_1.id, prueba_interseccion_2.id, 8.0, 10.0)
    prueba_tramo_2 = Tramo(prueba_interseccion_2.id, prueba_interseccion_3.id, 7.0, 10.0)
    prueba_tramo_3 = Tramo(prueba_interseccion_1.id, prueba_interseccion_3.id, 10.0, 45.0)
    prueba_red.conectar_intersecciones(prueba_tramo_1)
    prueba_red.conectar_intersecciones(prueba_tramo_2)
    prueba_red.conectar_intersecciones(prueba_tramo_3)
    ruta_distancia = calcular_ruta_minima(prueba_red, "A", "C", criterio="distancia")
    assert ruta_distancia.camino == ["A", "C"]
    assert ruta_distancia.costo_total == 10.0
    ruta_tiempo = calcular_ruta_minima(prueba_red, "A", "C", criterio="tiempo")
    assert ruta_tiempo.costo_total == 20.0
    assert ruta_tiempo.camino == ["A", "B", "C"]

def test_calcular_ruta_minima_destino_inalcanzable_retorna_none():
    prueba_red = RedVial()
    prueba_interseccion_1 = Interseccion("A", "Rivadavia", (13.2, 43.3))
    prueba_interseccion_2 = Interseccion("B", "San Martin", (56.4, 11.2))
    prueba_red.agregar_interseccion(prueba_interseccion_1)
    prueba_red.agregar_interseccion(prueba_interseccion_2)
    prueba_tramo_1 = Tramo(prueba_interseccion_1.id, prueba_interseccion_2.id, 8.0, 10.0)
    prueba_red.conectar_intersecciones(prueba_tramo_1)
    resultado = calcular_ruta_minima(prueba_red, "B", "A", criterio="distancia")
    assert resultado is None

def test_calcular_ruta_minima_criterio_invalido_error():
    prueba_red = RedVial()
    prueba_interseccion_1 = Interseccion("A", "Rivadavia", (13.2, 43.3))
    prueba_interseccion_2 = Interseccion("B", "San Martin", (56.4, 11.2))
    prueba_red.agregar_interseccion(prueba_interseccion_1)
    prueba_red.agregar_interseccion(prueba_interseccion_2)
    prueba_tramo_1 = Tramo(prueba_interseccion_1.id, prueba_interseccion_2.id, 8.0, 10.0)
    prueba_red.conectar_intersecciones(prueba_tramo_1)
    with pytest.raises(ValueError, match="criterio"):
        resultado = calcular_ruta_minima(prueba_red, "A", "B", criterio="combustible")

def test_calcular_ruta_minima_esquinas_inexistentes_error():
    prueba_red = RedVial()
    prueba_interseccion_1 = Interseccion("A", "Rivadavia", (13.2, 43.3))
    prueba_interseccion_2 = Interseccion("B", "San Martin", (56.4, 11.2))
    prueba_red.agregar_interseccion(prueba_interseccion_1)
    prueba_red.agregar_interseccion(prueba_interseccion_2)
    with pytest.raises(ValueError, match="no existen en la red"):
        resultado = calcular_ruta_minima(prueba_red, "A", "D", criterio="distancia")