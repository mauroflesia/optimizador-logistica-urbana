from src.models import Vehiculo, Pedido
import pytest
def test_instanciar_pedido_y_vehiculo_correctamente():
    vehiculo_1 = Vehiculo("E2", 800.0)
    pedido_1 = Pedido("FS4", "D2", 900.0)
    assert vehiculo_1.deposito_id == "E2"
    assert vehiculo_1.carga_maxima == 800.0
    assert pedido_1.id == "FS4"
    assert pedido_1.destino_id == "D2"
    assert pedido_1.peso == 900.0

def test_crear_pedido_peso_invalido_error():
    with pytest.raises(ValueError, match="El peso del pedido debe ser"):
        Pedido("P1", "D1", -5.0)
def test_crear_vehiculo_carga_invalida_error():
    with pytest.raises(ValueError, match="carga maxima"):
        Vehiculo("D1", -34)