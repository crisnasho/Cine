def mostrar_asientos(asientos_seleccionados):
    # Imprime los asientos del cine, marcando los seleccionados con una "x"
    print("\nAsientos:")
    for i in range(1, 101):
        if i in asientos_seleccionados:
            print("x", end=" ")  # Imprime "x" para los asientos seleccionados
        else:
            print(i, end=" ")  # Imprime el número del asiento si está disponible
        
        if i % 10 == 0:
            print()  # Nueva línea cada 10 asientos para una mejor visualización

def comprar_entradas(asientos_seleccionados):
    # Permite al usuario comprar entradas y seleccionar asientos
    cantidad = int(input("¿Cuántas entradas deseas comprar? "))
    precio_entrada = 5  # Precio fijo por entrada
    total_entradas = cantidad * precio_entrada  # Calcula el costo total de las entradas
    
    for _ in range(cantidad):
        while True:
            seleccion_asiento = input("Selecciona tu asiento (1...100): ")
            if seleccion_asiento.isdigit():
                asiento_num = int(seleccion_asiento)
                if 1 <= asiento_num <= 100:
                    if asiento_num not in asientos_seleccionados:
                        asientos_seleccionados.append(asiento_num)
                        print(f"Asiento {asiento_num} seleccionado.")
                        break  # Sale del bucle si el asiento es válido y está disponible
                    else:
                        print("Ese asiento ya ha sido seleccionado.")
                else:
                    print("Por favor, selecciona un número de asiento válido (1...100).")
            else:
                print("Entrada no válida. Por favor, introduce un número de asiento.")
    
    return asientos_seleccionados, cantidad, total_entradas

def seleccionar_bebestibles(bebestibles=None):
    # Permite al usuario seleccionar bebestibles y calcular el costo total
    if bebestibles is None:
        bebestibles = {"Pequeño": 0, "Mediano": 0, "Grande": 0}
    
    precios = {"Pequeño": 2, "Mediano": 3, "Grande": 4}  # Precios de los bebestibles
    total_bebestibles = 0  # Inicializa el costo total de los bebestibles

    comprar = input("¿Deseas comprar bebestibles? (si/no): ").strip().lower()
    if comprar == "si":
        while True:
            print("\nMenú de Bebestibles:")
            print("1. Pequeño - $2")
            print("2. Mediano - $3")
            print("3. Grande - $4")
            print("4. Terminar selección")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                bebestibles["Pequeño"] += int(input("Cantidad de bebestibles pequeños: "))
            elif opcion == "2":
                bebestibles["Mediano"] += int(input("Cantidad de bebestibles medianos: "))
            elif opcion == "3":
                bebestibles["Grande"] += int(input("Cantidad de bebestibles grandes: "))
            elif opcion == "4":
                break  # Termina la selección de bebestibles
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

        total_bebestibles = (bebestibles["Pequeño"] * precios["Pequeño"] +
                             bebestibles["Mediano"] * precios["Mediano"] +
                             bebestibles["Grande"] * precios["Grande"])
    
    return bebestibles, total_bebestibles

def seleccionar_cabritas(cabritas=None):
    # Permite al usuario seleccionar cabritas y calcular el costo total
    if cabritas is None:
        cabritas = {"Pequeño": 0, "Mediano": 0, "Grande": 0}
    
    precios = {"Pequeño": 3, "Mediano": 5, "Grande": 7}  # Precios de las cabritas
    total_cabritas = 0  # Inicializa el costo total de las cabritas

    comprar = input("¿Deseas comprar cabritas? (si/no): ").strip().lower()
    if comprar == "si":
        while True:
            print("\nMenú de Cabritas:")
            print("1. Pequeño - $3")
            print("2. Mediano - $5")
            print("3. Grande - $7")
            print("4. Terminar selección")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                cabritas["Pequeño"] += int(input("Cantidad de cabritas pequeñas: "))
            elif opcion == "2":
                cabritas["Mediano"] += int(input("Cantidad de cabritas medianas: "))
            elif opcion == "3":
                cabritas["Grande"] += int(input("Cantidad de cabritas grandes: "))
            elif opcion == "4":
                break  # Termina la selección de cabritas
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

        total_cabritas = (cabritas["Pequeño"] * precios["Pequeño"] +
                          cabritas["Mediano"] * precios["Mediano"] +
                          cabritas["Grande"] * precios["Grande"])
    
    return cabritas, total_cabritas

def mostrar_bebestibles(bebestibles):
    # Imprime la cantidad de bebestibles seleccionados
    print("Bebestibles actuales:")
    for tamaño, cantidad in bebestibles.items():
        print(f"  {tamaño}: {cantidad}")

def mostrar_cabritas(cabritas):
    # Imprime la cantidad de cabritas seleccionadas
    print("Cabritas actuales:")
    for tamaño, cantidad in cabritas.items():
        print(f"  {tamaño}: {cantidad}")

def modificar_pedido(asientos_seleccionados, cantidad_entradas, total_entradas, bebestibles, total_bebestibles, cabritas, total_cabritas):
    # Permite modificar el pedido, agregando o eliminando entradas, bebestibles y cabritas
    precios_entradas = 5
    precios_bebestibles = {"Pequeño": 2, "Mediano": 3, "Grande": 4}
    precios_cabritas = {"Pequeño": 3, "Mediano": 5, "Grande": 7}

    while True:
        print("\nOpciones de Modificación:")
        print("1. Modificar cantidad de entradas")
        print("2. Agregar o eliminar bebestibles")
        print("3. Agregar o eliminar cabritas")
        print("4. Terminar modificación")
        opcion_modificar = input("Selecciona una opción: ")

        if opcion_modificar == "1":
            modificar_entradas = input("¿Deseas agregar o eliminar entradas? (agregar/eliminar): ").strip().lower()
            if modificar_entradas == "agregar":
                extra_entradas = int(input("¿Cuántas entradas adicionales deseas comprar? "))
                cantidad_entradas += extra_entradas
                total_entradas += extra_entradas * precios_entradas
                for _ in range(extra_entradas):
                    while True:
                        seleccion_asiento = input("Selecciona tu asiento adicional (1...100): ")
                        if seleccion_asiento.isdigit():
                            asiento_num = int(seleccion_asiento)
                            if 1 <= asiento_num <= 100:
                                if asiento_num not in asientos_seleccionados:
                                    asientos_seleccionados.append(asiento_num)
                                    print(f"Asiento {asiento_num} seleccionado.")
                                    break  # Sale del bucle si el asiento es válido y está disponible
                                else:
                                    print("Ese asiento ya ha sido seleccionado.")
                            else:
                                print("Por favor, selecciona un número de asiento válido (1...100).")
                        else:
                            print("Entrada no válida. Por favor, introduce un número de asiento.")
            elif modificar_entradas == "eliminar":
                eliminar_entradas = int(input("¿Cuántas entradas deseas eliminar? "))
                if eliminar_entradas <= cantidad_entradas:
                    cantidad_entradas -= eliminar_entradas
                    total_entradas -= eliminar_entradas * precios_entradas
                    for _ in range(eliminar_entradas):
                        while True:
                            seleccion_asiento = input("Selecciona el asiento que deseas eliminar (1...100): ")
                            if seleccion_asiento.isdigit():
                                asiento_num = int(seleccion_asiento)
                                if asiento_num in asientos_seleccionados:
                                    asientos_seleccionados.remove(asiento_num)
                                    print(f"Asiento {asiento_num} eliminado.")
                                    break  # Sale del bucle si el asiento es válido y está en la lista de seleccionados
                                else:
                                    print("Ese asiento no está seleccionado.")
                            else:
                                print("Entrada no válida. Por favor, introduce un número de asiento.")
                else:
                    print("No puedes eliminar más entradas de las que has comprado.")
        elif opcion_modificar == "2":
            mostrar_bebestibles(bebestibles)
            modificar_bebestibles = input("¿Deseas agregar o eliminar bebestibles? (agregar/eliminar): ").strip().lower()
            if modificar_bebestibles == "agregar":
                while True:
                    print("\nMenú de Bebestibles:")
                    print("1. Pequeño - $2")
                    print("2. Mediano - $3")
                    print("3. Grande - $4")
                    print("4. Terminar selección")
                    opcion_bebestible = input("Selecciona una opción: ")

                    if opcion_bebestible == "1":
                        cantidad = int(input("Cantidad de bebestibles pequeños: "))
                        bebestibles["Pequeño"] += cantidad
                        total_bebestibles += cantidad * precios_bebestibles["Pequeño"]
                    elif opcion_bebestible == "2":
                        cantidad = int(input("Cantidad de bebestibles medianos: "))
                        bebestibles["Mediano"] += cantidad
                        total_bebestibles += cantidad * precios_bebestibles["Mediano"]
                    elif opcion_bebestible == "3":
                        cantidad = int(input("Cantidad de bebestibles grandes: "))
                        bebestibles["Grande"] += cantidad
                        total_bebestibles += cantidad * precios_bebestibles["Grande"]
                    elif opcion_bebestible == "4":
                        break  # Termina la selección de bebestibles
                    else:
                        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
            elif modificar_bebestibles == "eliminar":
                while True:
                    print("\nMenú de Bebestibles:")
                    print("1. Pequeño - $2")
                    print("2. Mediano - $3")
                    print("3. Grande - $4")
                    print("4. Terminar selección")
                    opcion_bebestible = input("Selecciona una opción: ")

                    if opcion_bebestible == "1":
                        cantidad = int(input("Cantidad de bebestibles pequeños a eliminar: "))
                        if cantidad <= bebestibles["Pequeño"]:
                            bebestibles["Pequeño"] -= cantidad
                            total_bebestibles -= cantidad * precios_bebestibles["Pequeño"]
                        else:
                            print("No puedes eliminar más de lo que has comprado.")
                    elif opcion_bebestible == "2":
                        cantidad = int(input("Cantidad de bebestibles medianos a eliminar: "))
                        if cantidad <= bebestibles["Mediano"]:
                            bebestibles["Mediano"] -= cantidad
                            total_bebestibles -= cantidad * precios_bebestibles["Mediano"]
                        else:
                            print("No puedes eliminar más de lo que has comprado.")
                    elif opcion_bebestible == "3":
                        cantidad = int(input("Cantidad de bebestibles grandes a eliminar: "))
                        if cantidad <= bebestibles["Grande"]:
                            bebestibles["Grande"] -= cantidad
                            total_bebestibles -= cantidad * precios_bebestibles["Grande"]
                        else:
                            print("No puedes eliminar más de lo que has comprado.")
                    elif opcion_bebestible == "4":
                        break  # Termina la eliminación de bebestibles
                    else:
                        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
        elif opcion_modificar == "3":
            mostrar_cabritas(cabritas)
            modificar_cabritas = input("¿Deseas agregar o eliminar cabritas? (agregar/eliminar): ").strip().lower()
            if modificar_cabritas == "agregar":
                while True:
                    print("\nMenú de Cabritas:")
                    print("1. Pequeño - $3")
                    print("2. Mediano - $5")
                    print("3. Grande - $7")
                    print("4. Terminar selección")
                    opcion_cabritas = input("Selecciona una opción: ")

                    if opcion_cabritas == "1":
                        cantidad = int(input("Cantidad de cabritas pequeñas: "))
                        cabritas["Pequeño"] += cantidad
                        total_cabritas += cantidad * precios_cabritas["Pequeño"]
                    elif opcion_cabritas == "2":
                        cantidad = int(input("Cantidad de cabritas medianas: "))
                        cabritas["Mediano"] += cantidad
                        total_cabritas += cantidad * precios_cabritas["Mediano"]
                    elif opcion_cabritas == "3":
                        cantidad = int(input("Cantidad de cabritas grandes: "))
                        cabritas["Grande"] += cantidad
                        total_cabritas += cantidad * precios_cabritas["Grande"]
                    elif opcion_cabritas == "4":
                        break  # Termina la selección de cabritas
                    else:
                        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
            elif modificar_cabritas == "eliminar":
                while True:
                    print("\nMenú de Cabritas:")
                    print("1. Pequeño - $3")
                    print("2. Mediano - $5")
                    print("3. Grande - $7")
                    print("4. Terminar selección")
                    opcion_cabritas = input("Selecciona una opción: ")

                    if opcion_cabritas == "1":
                        cantidad = int(input("Cantidad de cabritas pequeñas a eliminar: "))
                        if cantidad <= cabritas["Pequeño"]:
                            cabritas["Pequeño"] -= cantidad
                            total_cabritas -= cantidad * precios_cabritas["Pequeño"]
                        else:
                            print("No puedes eliminar más de lo que has comprado.")
                    elif opcion_cabritas == "2":
                        cantidad = int(input("Cantidad de cabritas medianas a eliminar: "))
                        if cantidad <= cabritas["Mediano"]:
                            cabritas["Mediano"] -= cantidad
                            total_cabritas -= cantidad * precios_cabritas["Mediano"]
                        else:
                            print("No puedes eliminar más de lo que has comprado.")
                    elif opcion_cabritas == "3":
                        cantidad = int(input("Cantidad de cabritas grandes a eliminar: "))
                        if cantidad <= cabritas["Grande"]:
                            cabritas["Grande"] -= cantidad
                            total_cabritas -= cantidad * precios_cabritas["Grande"]
                        else:
                            print("No puedes eliminar más de lo que has comprado.")
                    elif opcion_cabritas == "4":
                        break  # Termina la eliminación de cabritas
                    else:
                        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
        elif opcion_modificar == "4":
            break  # Termina la modificación del pedido
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
    
    return asientos_seleccionados, cantidad_entradas, total_entradas, bebestibles, total_bebestibles, cabritas, total_cabritas

def mostrar_boleta(entradas, total_entradas, bebestibles, total_bebestibles, cabritas, total_cabritas):
    # Muestra un resumen del pedido
    total = total_entradas + total_bebestibles + total_cabritas
    print("\nBoleta:")
    print(f"Entradas ({entradas}): ${total_entradas}")
    print("Bebestibles:")
    for tamaño, cantidad in bebestibles.items():
        print(f"  {tamaño}: {cantidad}")
    print(f"Total Bebestibles: ${total_bebestibles}")
    print("Cabritas:")
    for tamaño, cantidad in cabritas.items():
        print(f"  {tamaño}: {cantidad}")
    print(f"Total Cabritas: ${total_cabritas}")
    print(f"Total a pagar: ${total}")

def main():
    # Función principal del programa
    asientos_seleccionados = []  # Inicializa la lista de asientos seleccionados
    while True:  # Bucle infinito para el menú principal
        print("\nMenú Principal:")
        print("1. Comprar entradas")
        print("2. Mostrar asientos comprados")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")  # Pide al usuario que seleccione una opción del menú

        if opcion == "1":
            asientos_seleccionados, cantidad_entradas, total_entradas = comprar_entradas(asientos_seleccionados)  # Compra entradas
            bebestibles, total_bebestibles = seleccionar_bebestibles()  # Selecciona bebestibles
            cabritas, total_cabritas = seleccionar_cabritas()  # Selecciona cabritas

            while True:
                modificar = input("\n¿Deseas modificar el pedido? (si/no): ").strip().lower()  # Pregunta si desea modificar el pedido
                if modificar == "si":
                    asientos_seleccionados, cantidad_entradas, total_entradas, bebestibles, total_bebestibles, cabritas, total_cabritas = modificar_pedido(
                        asientos_seleccionados, cantidad_entradas, total_entradas, bebestibles, total_bebestibles, cabritas, total_cabritas)  # Modifica el pedido
                elif modificar == "no":
                    break  # Sale del bucle si no desea modificar el pedido
                else:
                    print("Opción no válida. Por favor, selecciona 'si' o 'no'.")  # Opción no válida

            mostrar_boleta(cantidad_entradas, total_entradas, bebestibles, total_bebestibles, cabritas, total_cabritas)  # Muestra la boleta final
        elif opcion == "2":
            mostrar_asientos(asientos_seleccionados)  # Muestra los asientos seleccionados
        elif opcion == "3":
            print("Gracias por usar el sistema de cine. ¡Disfruta tu película!")  # Mensaje de despedida
            break  # Termina el programa
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 3.")  # Opción no válida

if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa
