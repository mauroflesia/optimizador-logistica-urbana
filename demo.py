"""Simulación demostrativa de optimización logística urbana de última milla."""

from src.graph import RedVial
from src.models import Interseccion, Tramo, Vehiculo, Pedido
from src.optimizer import optimizar_ruta_entregas


def main() -> None:
    print("=" * 65)
    print(">> SIMULADOR DE OPTIMIZACION LOGISTICA URBANA (ULTIMA MILLA)")
    print("=" * 65)

    # 1. Construcción de la Red Vial Urbana
    red = RedVial()
    esquinas = [
        Interseccion("HUB", "Centro Logistico Central", (-34.6037, -58.3816)),
        Interseccion("PALERMO", "Av. Santa Fe y Scalabrini Ortiz", (-34.5828, -58.4199)),
        Interseccion("BELGRANO", "Av. Cabildo y Juramento", (-34.5623, -58.4566)),
        Interseccion("CABALLITO", "Av. Rivadavia y Acoyte", (-34.6186, -58.4367)),
        Interseccion("RECOLETA", "Av. Las Heras y Pueyrredon", (-34.5895, -58.3974)),
    ]

    for esquina in esquinas:
        red.agregar_interseccion(esquina)

    # Red de tramos viales (origen, destino, distancia_km, tiempo_mins)
    tramos = [
        # Salidas del HUB
        Tramo("HUB", "RECOLETA", 4.0, 12.0),
        Tramo("HUB", "CABALLITO", 7.0, 20.0),
        # Conexiones intermedias
        Tramo("RECOLETA", "PALERMO", 3.5, 10.0),
        Tramo("PALERMO", "BELGRANO", 4.2, 14.0),
        Tramo("CABALLITO", "PALERMO", 5.0, 18.0),
        # Conexiones cruzadas y retornos
        Tramo("BELGRANO", "CABALLITO", 8.0, 22.0),
        Tramo("BELGRANO", "HUB", 10.0, 30.0),
        Tramo("PALERMO", "HUB", 6.5, 20.0),
        Tramo("CABALLITO", "HUB", 6.0, 18.0),
    ]

    for tramo in tramos:
        red.conectar_intersecciones(tramo)

    # 2. Configurar la Flota y los Pedidos
    camioneta = Vehiculo(deposito_id="HUB", carga_maxima=150.0)

    pedidos = [
        Pedido(id="ORD-101", destino_id="BELGRANO", peso=45.0),
        Pedido(id="ORD-102", destino_id="RECOLETA", peso=30.0),
        Pedido(id="ORD-103", destino_id="PALERMO", peso=50.0),
        Pedido(id="ORD-104", destino_id="CABALLITO", peso=80.0),  # Excede la capacidad restante
    ]

    peso_total = sum(p.peso for p in pedidos)
    print(f"\n[*] Pedidos recibidos para despacho: {len(pedidos)} (Total: {peso_total} kg)")
    for p in pedidos:
        print(f"   - [{p.id}] Destino: {p.destino_id:<10} | Peso: {p.peso} kg")

    print(f"\n[+] Vehiculo asignado:")
    print(f"   - Base: {camioneta.deposito_id}")
    print(f"   - Capacidad maxima de carga: {camioneta.carga_maxima} kg")

    # 3. Ejecutar la Optimización Voraz
    print("\n[~] Calculando plan de ruteo optimo (Greedy Nearest Neighbor + Dijkstra)...")
    plan = optimizar_ruta_entregas(red, camioneta, pedidos, criterio="distancia")

    # 4. Presentar Resultados
    peso_cargado = sum(p.peso for p in pedidos if p.id in plan.pedidos_entregados)
    pedidos_postergados = [p.id for p in pedidos if p.id not in plan.pedidos_entregados]

    print("\n" + "=" * 65)
    print("HOJA DE RUTA OPTIMIZADA")
    print("=" * 65)
    print(f"[OK] Pedidos Entregados ({len(plan.pedidos_entregados)}): {', '.join(plan.pedidos_entregados)}")
    if pedidos_postergados:
        print(f"[!]  Pedidos Postergados por Exceso de Carga: {', '.join(pedidos_postergados)}")
    print(f"[*]  Carga Utilizada: {peso_cargado} kg / {camioneta.carga_maxima} kg ({(peso_cargado / camioneta.carga_maxima) * 100:.1f}%)")
    print(f"[*]  Itinerario GPS: {' -> '.join(plan.camino_completo)}")
    print(f"[*]  Distancia Total Recorrida: {plan.costo_total:.1f} km")
    print("=" * 65)


if __name__ == "__main__":
    main()
