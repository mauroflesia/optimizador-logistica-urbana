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

