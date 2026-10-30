from src.models import PlanEntrega, Vehiculo, Pedido, Interseccion, Tramo
import pytest
from src.graph import RedVial
from src.optimizer import optimizar_ruta_entregas
def test_optimizar_ruta_un_solo_pedido_ida_y_vuelta():
    prueba_red = RedVial()
    interseccion_1 = Interseccion("DEP", "Rivadavia", (45.1, 54.4))
    interseccion_2 = Interseccion("CLIENTE", "San Martin", (45.4, 66.3))
    prueba_red.agregar_interseccion(interseccion_1)
    prueba_red.agregar_interseccion(interseccion_2)
    tramo_ida = Tramo("DEP", "CLIENTE", 10.0, 4.1)
    tramo_vuelta = Tramo("CLIENTE", "DEP", 10.0, 4.1)
    prueba_red.conectar_intersecciones(tramo_ida)
    prueba_red.conectar_intersecciones(tramo_vuelta)
    vehiculo_1 = Vehiculo("DEP", 100.0)
    pedido_1 = Pedido("P1", "CLIENTE", 15.0)
    plan = optimizar_ruta_entregas(prueba_red, vehiculo_1, [pedido_1], criterio="distancia")
    assert plan.pedidos_entregados == ["P1"]
    assert plan.camino_completo == ["DEP", "CLIENTE", "DEP"]
    assert plan.costo_total == 20.0

def test_optimizar_ruta_elige_pedido_mas_cercano_primero():
    red = RedVial()
    interseccion_1 = Interseccion("DEP", "Rivadavia", (46.53, 88.63))
    interseccion_2 = Interseccion("LEJOS", "25 de Mayo", (92.33, 77.33))
    interseccion_3 = Interseccion("CERCA", "Hernandarias", (31.33, 51.33))
    red.agregar_interseccion(interseccion_1)
    red.agregar_interseccion(interseccion_2)
    red.agregar_interseccion(interseccion_3)
    pedido_1 = Pedido("P_LEJOS", "LEJOS", 5.0)
    pedido_2 = Pedido("P_CERCA", "CERCA", 6.0)
    tramo_1 = Tramo("CERCA", "LEJOS", 15.0, 5.0)
    tramo_2 = Tramo("LEJOS", "DEP", 40.0, 10.0)
    tramo_3 = Tramo("DEP", "CERCA", 10.0, 5.0)
    tramo_4 = Tramo("DEP", "LEJOS", 50.0, 16.0)
    red.conectar_intersecciones(tramo_1)
    red.conectar_intersecciones(tramo_2)
    red.conectar_intersecciones(tramo_3)
    red.conectar_intersecciones(tramo_4)
    vehiculo_1 = Vehiculo("DEP", 100.0)
    plan = optimizar_ruta_entregas(red, vehiculo_1, [pedido_1, pedido_2], criterio="distancia")
    assert plan.pedidos_entregados == ["P_CERCA", "P_LEJOS"]
    assert plan.camino_completo == ["DEP","CERCA", "LEJOS", "DEP"]
    assert plan.costo_total == 65.0

def test_optimizar_ruta_respeta_capacidad_maxima_vehiculo():
    red = RedVial()
    interseccion_1 = Interseccion("DEP","Martin", (45.33, 65.65))
    interseccion_2 = Interseccion("C1", "Rivadavia", (41.45, 88.11))
    interseccion_3 = Interseccion("C2", "Juramento", (90.31, 71.45))
    red.agregar_interseccion(interseccion_1)
    red.agregar_interseccion(interseccion_2)
    red.agregar_interseccion(interseccion_3)
    tramo_1 = Tramo("DEP", "C1", 10.0, 4.5)
    tramo_2 = Tramo("C1", "C2", 30.0, 10.0)
    tramo_3 = Tramo("C2", "DEP", 25.0, 9.0)
    tramo_4 = Tramo("C1", "DEP", 15.0, 7.5)
    red.conectar_intersecciones(tramo_1)
    red.conectar_intersecciones(tramo_2)
    red.conectar_intersecciones(tramo_3)
    red.conectar_intersecciones(tramo_4)
    vehiculo_1 = Vehiculo("DEP", 10.0)
    pedido_1 = Pedido("P1", "C1", 6.0)
    pedido_2 = Pedido("P2", "C2", 8.0)
    plan = optimizar_ruta_entregas(red, vehiculo_1, [pedido_1, pedido_2], criterio="distancia")
    assert plan.pedidos_entregados == ["P1"]
    assert plan.camino_completo == ["DEP", "C1", "DEP"]
    assert plan.costo_total == 25.0

def test_optimizar_ruta_sin_pedidos():
    red = RedVial()
    interseccion_1 = Interseccion("DEP", "Moreno", (31.44, 42.46))
    red.agregar_interseccion(interseccion_1)
    vehiculo_1 = Vehiculo("DEP", 600.0)
    plan = optimizar_ruta_entregas(red,vehiculo_1, [], criterio="distancia")
    assert plan.pedidos_entregados == []
    assert plan.camino_completo == [vehiculo_1.deposito_id]
    assert plan.costo_total == 0.0


