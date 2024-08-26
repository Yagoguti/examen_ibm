import pytest
from unittest.mock import patch
from main import main
from models import Cliente, SistemaClientes

# Test para agregar un cliente
def test_agregar_cliente(mocker):
    sistema = SistemaClientes()
    mocker.patch('builtins.input', side_effect=['1', 'Juan', 'juan@example.com', '123456789', '5'])
    mocker.patch('builtins.print')
    
    with patch('main.SistemaClientes', return_value=sistema):
        main()
    
    assert len(sistema.clientes) == 1
    assert sistema.clientes[0].nombre == 'Juan'

# Test para eliminar un cliente
def test_eliminar_cliente(mocker):
    sistema = SistemaClientes()
    cliente = Cliente('Juan', 'juan@example.com', '123456789')
    sistema.agregar_cliente(cliente)
    
    mocker.patch('builtins.input', side_effect=['2', 'Juan', '5'])
    mocker.patch('builtins.print')
    
    with patch('main.SistemaClientes', return_value=sistema):
        main()
    
    assert len(sistema.clientes) == 0

# Test para buscar un cliente
def test_buscar_cliente(mocker):
    sistema = SistemaClientes()
    cliente = Cliente('Juan', 'juan@example.com', '123456789')
    sistema.agregar_cliente(cliente)
    
    mocker.patch('builtins.input', side_effect=['3', 'Juan', '5'])
    mocker.patch('builtins.print')
    
    with patch('main.SistemaClientes', return_value=sistema):
        main()
    
    # Aquí deberías verificar que la salida (print) contiene la información del cliente
    # Esto puede ser más complejo y requerir un enfoque diferente para capturar la salida

# Test para listar clientes
def test_listar_clientes(mocker):
    sistema = SistemaClientes()
    cliente = Cliente('Juan', 'juan@example.com', '123456789')
    sistema.agregar_cliente(cliente)
    
    mocker.patch('builtins.input', side_effect=['4', '5'])
    mocker.patch('builtins.print')
    
    with patch('main.SistemaClientes', return_value=sistema):
        main()
    
    # Similar al caso anterior, verificar la salida impresa

# Nota: Estos tests son básicos y pueden necesitar ajustes para capturar y verificar correctamente las salidas impresas.