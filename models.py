class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"
    

class SistemaClientes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def eliminar_cliente(self, nombre):
        cliente_encontrado = None
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                cliente_encontrado = cliente
                break
        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)
            return True
        else:
            return False

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)