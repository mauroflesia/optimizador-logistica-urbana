from src.models import Vehiculo, Pedido, PlanEntrega
from src.graph import RedVial
from src.dijkstra import calcular_ruta_minima

def optimizar_ruta_entregas(red: RedVial, vehiculo: Vehiculo, pedidos: list[Pedido], criterio: str="distancia") -> PlanEntrega:
    posicion_actual = vehiculo.deposito_id
    capacidad_restante = vehiculo.carga_maxima
    pendientes = list(pedidos)
    pedidos_entregados = []
    costo_total = 0.0
    camino_completo = [posicion_actual]
    while pendientes:
        mejor_pedido = None
        mejor_ruta = None
        menor_costo = float("inf")
        for pedido in pendientes:
            if pedido.peso <= capacidad_restante:
                ruta = calcular_ruta_minima(red, posicion_actual, pedido.destino_id, criterio)
                if ruta is not None and ruta.costo_total < menor_costo:
                    mejor_pedido = pedido
                    mejor_ruta = ruta
                    menor_costo = ruta.costo_total
        if mejor_pedido is None:
            break
        else:
            capacidad_restante -= mejor_pedido.peso
            costo_total += mejor_ruta.costo_total
            camino_completo.extend(mejor_ruta.camino[1:])
            pedidos_entregados.append(mejor_pedido.id)
            posicion_actual = mejor_pedido.destino_id
            pendientes.remove(mejor_pedido)
    if posicion_actual != vehiculo.deposito_id:
        ruta_retorno = calcular_ruta_minima(red, posicion_actual, vehiculo.deposito_id, criterio)
        if ruta_retorno is not None:
            costo_total += ruta_retorno.costo_total
            camino_completo.extend(ruta_retorno.camino[1:])
    return PlanEntrega(pedidos_entregados, camino_completo, costo_total)


