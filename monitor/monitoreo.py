
services = {
    "Autenticacion": False,
    "Usuarios": False,
    "BaseConocimientos": False,
}

def imprimir_estado() :
    #Imprimir encabezado
    print(f"{'Servicio':<20} {'Estado':<10}")
    print("-" * 30)

    # Recorrer el diccionario e imprimir cada clave y valor en formato tabla
    for servicio, estado in services.items():
       print(f"{servicio:<20} {str(estado):<10}")

def cambiar_estado(property):
    services[property] = True
    print(services)


if __name__ == "__main__":
    imprimir_estado()

