from models import SistemaClientes, Cliente

def main():
    sistema = SistemaClientes()

    # while True:
    #     print("\nMenú del Sistema de Clientes")
    #     print("1. Agregar cliente")
    #     print("2. Eliminar cliente")
    #     print("3. Buscar cliente")
    #     print("4. Listar clientes")
    #     print("5. Salir")


        # opcion = input("Seleccione una opción: ")

    while True:
        print("\n===========================")
        print("Menú del Sistema de Clientes")
        print("===========================")
        print("1. Agregar cliente")
        print("2. Eliminar cliente")
        print("3. Buscar cliente")
        print("4. Listar clientes")
        print("5. Salir")

        print("===========================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            cliente = Cliente(nombre, email, telefono)
            sistema.agregar_cliente(cliente)
            print(f"Cliente '{nombre}' agregado al sistema.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente a eliminar: ")
            if sistema.eliminar_cliente(nombre):
                print(f"Cliente '{nombre}' eliminado del sistema")
            else:
                print("No se encontró el cliente.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            cliente = sistema.buscar_cliente(nombre)
            if cliente:
                 print(f"Cliente encontrado: {cliente.nombre} -  Email: {cliente.email}, Teléfono: {cliente.telefono}")
            else:
                print("Cliente no encontrado.")
        elif opcion == "4":
            sistema.listar_clientes()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()