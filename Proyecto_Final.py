from datetime import datetime #Importamos librería date time para el log de archivos.
import time, sys  # Importamos librerías necesarias, para tiempo y sistema.


# Variables
tipo_producto = [
    "Tamal Rojo",
    "Tamal Verde",
    "Tamal de Pollo",
    "Tamal Dulce",
    "Litros Atole",
]  # Lista de tipo de producto

# Diccionario global de archivos
archivos_disponibles = {
    "1": "ingredientes.txt",
    "2": "produccion.txt",
    "3": "apartados.txt",
    "4": "ventas.txt",
}

# costo_unitario = [costo_rojo, costo_verde, costo_pollo, costo_dulce, costo_atole] 
# En desarrollo veáse comentario en fase1_compra

cantidades = [0, 0, 0, 0, 0]  # Cantidades definidas en una lista
precio_salado = 22.0  # Constantes de precio para cada tipo de producto
precio_dulce = 20.0
precio_atole = 28.0


"""
En esta primera sección he añadido nuevas funciones de acuerdo a la rúbrica del proyecto final, la lógica del programa original permanece intacta, intenté integrar los nuevos conceptos que aprendí a lo largo de las últimas semanas al programa original pero, lamentablemente, se volvió un estropicio en gran parte de la ejecución. Lo mantendré simple por ahora apegandome a la rúbrica para irlo expandiendo más adelante, deseo que este se convierta en un proyecto real que logre transportar en una aplicación.
"""

# Cree esta función para terminar la ejecución del programa


def salir_sistema():
    confirmar = input("¿Estás seguro que deseas salir? (si/no): ").lower()
    if confirmar == "si":
        print("Gracias por usar el sistema. ¡Hasta la próxima!")
        sys.exit()  # Usamos sys.exit para cerrar el programa
    else:
        print("Regresando al menú principal...\n")
        return False  # Indicador de continuar en el menú

# Cree una nueva función para inicio de sesión, también es llamada para cambiar de usuario

def inicio_sesion(): 
    usuario = input("Ingrese su nombre o nickname: ")
    print(
        "\nBienvenido/a, " + usuario + " al sistema de gestión Tamales Lucía."
    )  # Mensaje de bienvenida, concatenamos el string de nombre de usuario
    #time.sleep(3) #Mi siempre favorita función time para espera de 3 segundos con fines de interactividad
    print("Cargando programa, por favor espere...")
    #time.sleep(3) #Otra espera
    print("Sistema listo. ¡Comencemos!\n")
    #time.sleep(2) #Otra espera para que el usuario alcance a leer el mensaje anterior

    return usuario

# Cree esta función para validar la inactividad del programa.
# Primero definimos si el input está inactivo
def input_con_inactividad(mensaje, limite=600, confirmacion=30):
    """
    Pide input() y si el usuario tarda demasiado, aplica la lógica de inactividad.
    """
    inicio = time.time()
    try:
        opcion = input(mensaje)  # aquí se pide la opción normalmente
        return opcion
    except KeyboardInterrupt:
        # si el usuario no responde, aplicamos la validación
        return validar_inactividad(limite, confirmacion)

    
#Iniciamos la validación de inactividad
# IMPORTANTE, el input() bloquea la terminal por lo que el tiempo no se contabiliza
# la siguiente función sigue la rúbrica y solicitud de las instrucciones.

def validar_inactividad(limite=600, confirmacion=30):
    """
    Función que mide el tiempo de inactividad usando un ciclo for.
    limite = 600 segundos (10 minutos)
    confirmacion = 30 segundos adicionales para confirmar
    """
    opcion = None
    # Ciclo for que simula el paso del tiempo
    for segundos in range(limite):
        # Aquí se podría pedir la opción en cada iteración, sin embargo input() en python vanilla bloquea la terminal hasta que el usuario escriba algo, así que lo dejamos como demostración:
        time.sleep(1)  # Simula el paso de cada segundo
        if opcion:  # Si el usuario escribió algo, rompe
            return opcion

    # Despues de 10 minutos no hubo respuesta
    continuar = input("¿Sigues ahí?. ¿Deseas continuar? (si/no): ").lower()
    if continuar == "no":
        print("Gracias por usar el sistema. ¡Hasta la próxima!")
        time.sleep(2)
        sys.exit()
    elif continuar == "si":
        print("Continuando en el menú...")
        return "continuar"  # Regresa al menú sin cerrar

    # Segunda confirmación con otro ciclo for
    for segundos in range(confirmacion):
        time.sleep(1)
        if opcion:  # Si el usuario responde en este lapso
            return opcion
    print("No se obtuvo respuesta. El sistema se cerrará automáticamente.")
    time.sleep(2)
    sys.exit()

def pedir_fecha():  # Creamos una función que recolectará la fecha definida por el usuario
    fecha_str = input(
        "Ingrese la fecha en formato dd/mm/aaaa: "
    )  # Para fines prácticos le indicamos como se estructura la fecha
    try:
        dia, mes, año = fecha_str.split("/")
        fecha = (int(dia), int(mes), int(año))  # Tupla con el tenido de la fecha
        print("Fecha registrada:", fecha)
        return fecha
    except ValueError:  # Si el formato es incorrecto
        print("Formato incorrecto. Intente de nuevo. (ejemplo: 12/06/2025)")
        return pedir_fecha()


# Esta función construye y muestra el catáloogo de archivos disponibles en un diccionario
def mostrar_archivos_disponibles():
    print("\nArchivos disponibles:")
    for clave, nombre in archivos_disponibles.items():
        print(f"{clave}. {nombre}")
    return archivos_disponibles


# Definimos esta función para la lectura de los archivos
def leer_archivo():
    archivos = mostrar_archivos_disponibles()  # Mandamos llamar la función anterior
    opcion = input(
        "Seleccione el número del archivo que desea abrir: "
    )  # Validamos la selección para mostrar el archivo de acuerdo a las claves del diccionario
    try:
        nombre_archivo = archivos[opcion]
        with open(nombre_archivo, "r") as f:
            contenido_archivo = f.read()  # Leemos el contenido
            print("\nContenido del archivo:")
            print(contenido_archivo)
            time.sleep(2)
            print("Regresando al menú anterior...")
    except KeyError:  # Error si elige una opción diferente
        print("Opción inválida. Ingresa solo el número del archivo. Regresando al menú principal.")
    except FileNotFoundError:
        print(
            "No se encontró el archivo. Verifique el nombre."
        )  # Si no encuentra el archivo

def crear_archivo():
    # Primero pedimos la fecha al usuario
    fecha = pedir_fecha()  # Se devuelve la tupla (día, mes, año)

    # Segundo se solicita el nombre del archivo
    nombre = input("Ingrese el nombre del nuevo archivo (ejemplo: nuevo.txt): ")
    try:
        # Abrimos el archivo en modo escritura (crea o sobrescribe)
        with open(nombre, "w") as f:
            contenido = input("Escriba el contenido inicial del archivo: ")
            # Escribe la fecha guardada en la tupla + contenido
            f.write(f"[{fecha[0]}/{fecha[1]}/{fecha[2]}] {contenido}\n")
        print(f"Archivo '{nombre}' creado correctamente.")

        nueva_clave = str(len(archivos_disponibles) + 1)
        archivos_disponibles[nueva_clave] = nombre
        
    except Exception as e:  # Manejo de excepciones genéricas
        print(f"Ocurrió un error al crear el archivo: {e}")

def modificar_archivo():
    # Paso 1: pedir fecha
    fecha = pedir_fecha()  # devuelve tupla (día, mes, año)
    # Paso 2: pedir nombre del archivo
    nombre = input("Ingrese el nombre del archivo a modificar: ")

    try:
        # Paso 3: abrir archivo en modo append (agregar contenido)
        with open(nombre, "r+",) as f:
            contenido = input("Escriba el contenido: ")
            # Paso 4: escribir contenido con fecha
            f.write(f"\n[{fecha[0]}/{fecha[1]}/{fecha[2]}] {contenido}")
        print("Archivo actualizado correctamente.")
    except FileNotFoundError:
        print("El archivo no existe. Use la opción 'crear archivo'.")
    except Exception as e:
        # Paso 5: manejo de excepciones
        print(f"Ocurrió un error al modificar el archivo: {e}")


# Cree la función para mostrar el menú EN FORMA DE MATRIZ. Pero no estaba seguro si se refería a una matriz de datos.

def menu_principal_archivo(usuario):
    while True:
        print("")
        print("|-----------------------------------------|")
        print("| === MENÚ ARCHIVOS | TAMALERÍA LUCÍA === |")
        print("|-----------------------------------------|")
        print("| 1. Leer archivo   | 2. Modificar archivo|")
        print("| 3. Crear archivo  | 4. Cambiar usuario  |")
        print("| 5. Menú Tamales   | 6. Salir            |")
        print("| ----------------------------------------|")
        print("")
        opcion = input_con_inactividad("Seleccione una opción: ")
        
        if opcion is None:
            usuario = inicio_sesion()
            continue
        elif opcion == "continuar":
            continue
        # Usamos la estructura de decisión para la creación de archivos
        if opcion == "1":
            leer_archivo()
            time.sleep(1)
            
        elif opcion == "2":  # Modificar archivo 
            modificar_archivo()
            time.sleep(1)
                
        elif opcion == "3":  # Crear archivo
            crear_archivo()
            time.sleep(1)

        elif opcion == "4": # Cambiar usuario
            usuario = inicio_sesion()  
            time.sleep(1)
        elif opcion == '5':
            menu_principal_tamales()

        elif opcion == "6": # Salir sistema
            if salir_sistema():
                break
        else:
            print("Opción no válida. Intente de nuevo.")
    return usuario


def fase1_compra():  # Definimos la función fase 1
    print(
        "\n--- FASE 1: Compra de materia prima ---"
    )  # Mostramos mensaje de la fase tras selección del menú
    print(
        "\nLas compras de ingredientes se hacen en miércoles y jueves."
    )  # Indicamos cuando se hace la compra de la materia prima, véase comentario a continuación.

# Estuve intentando hacer una validación sobre el día en que se realiza la compra. Pero no le encontré un buen uso aún.
# En este apartado planeo solicitar las cantidades, peso y registrar toda la compra de la materia prima para calcular el costo unitario y al final dar un margen de utilidad.
# Aún está en desarrollo.

"""
    dia = input("Ingrese el día de la semana: ").lower()
    if dia in ["miércoles", "jueves"]:
        continuar = input("¿Desea registrar la compra de materia prima? (S/N): ").lower() #.lower para que la validación no sea case sensitive
        if continuar == "s":
            print("Compra registrada correctamente.")
        else:
            print("Compra no registrada.")
    else:
        print("Hoy no es día de compra. Solo se compra miércoles o jueves.")

"""

# El usuario ingresa la cantidad de tamales y atole producidos
# Version 2.0: Ahora el registro de producción crea un doble registro, uno en memoria para cálculos y otro en el archivo de producción .txt


def fase2_produccion():
    print("\n--- FASE 2: PRODUCCIÓN DE TAMALES ---")

    # Obtenemos fecha y hora actual
    ahora = datetime.now()
    marca_tiempo = ahora.strftime("%d/%m/%Y %H:%M:%S")

    # Abrimos archivo en modo append para acumular registros
    with open("produccion.txt", "a") as f:
        f.write(f"\n=== Registro de Producción ({marca_tiempo}) ===\n")

        # Iniciamos bucle para registrar cada tipo de producto
        for i in range(len(tipo_producto)):
            try:
                cantidad = int(input(f"Ingrese cantidad producida de {tipo_producto[i]}: "))
                if cantidad < 0:
                    print("No se puede registrar una cantidad negativa. Se registrará 0.")
                    cantidad = 0
                cantidades[i] = cantidad  # Se guarda el registroe n emoria
                f.write(f"{tipo_producto[i]}: {cantidad}\n")  # Guardamos en archivo
            except ValueError:
                print("Entrada inválida. Se registrará 0.")
                cantidades[i] = 0
                f.write(f"{tipo_producto[i]}: 0\n")

    print("Producción registrada correctamente y guardada en 'produccion.txt'.")



# Durante esta etapa, se realizan los apartados que hacen los clientes por teléfono.


def fase3_apartados():  # Definimos la función fase 3
    print(
        "\n--- FASE 3: APARTADOS DE CLIENTES ---"
    )  # Mostramos el mensaje al usuario tras selección del menú
    while (
        True
    ):  # Mostramos disponibilidad de inventario basados en lo declarado en la fase 2
        print("\nInventario disponible:")
        for i in range(len(tipo_producto)):
            print(f"{tipo_producto[i]}: {cantidades[i]} disponibles")

        nombre = input(
            "\nIngrese nombre del cliente: "
        )  # Planeo almacenar el nombre del cliente para usarlo después en la solicitud de cobro. Véase "cobro" en fase4
        total = 0
        # Registro de Tamales
        for i in range(4):  # Tamales: Rojo, Verde, Pollo, Dulce
            disponibles = cantidades[i]
            print(f"\n{tipo_producto[i]} disponibles: {disponibles}")
            cantidad = int(
                input(
                    f"Ingrese cantidad de {tipo_producto[i]} que desea encargar (0 a {disponibles}): "
                )
            )  # Muestra la disponibilidad cada vez que va a registrar un pedido por tipo de producto
            if cantidad < 0:
                print(
                    "No se puede registrar una cantidad negativa. Se registrará 0."
                )  # En caso de registrar un número negativo.
                cantidad = 0
            elif (
                cantidad > disponibles
            ):  # Si el cliente desea solicitar más tamales de los disponibles.
                print(
                    f"Solo hay {disponibles} disponibles. No se puede registrar esa cantidad."
                )
                continuar = input(
                    "¿Desea registrar una cantidad menor? (S/N): "
                ).lower()  # Se le da la opción para registrar una menor cantidad
                if continuar == "s":
                    cantidad = int(
                        input(f"Ingrese nueva cantidad (0 a {disponibles}): ")
                    )
                    if cantidad > disponibles:
                        print(
                            "Aún excede el inventario. Se omitirá este tipo."
                        )  # Se omite en tipo de producto si hay una reincidencia y no hay inventario
                        continue
                else:
                    print(
                        f"{tipo_producto[i]} no registrado."
                    )  # Si no se pudo realizar el registro
                    continue
            if i in [
                0,
                1,
                2,
            ]:  # Calculamos con base a la posición de la lista de los tamales salados.
                precio = precio_salado
            else:
                precio = precio_dulce  # De lo contrario son dulces
            total += cantidad * precio  # Calculamos el precio
            cantidades[i] -= cantidad  # Descontamos la existencia del inventario

        # Registro Atole
        # Validación similar a la anterior, pero esta llama a la quinta posición de la lista, Atole.
        disponibles = cantidades[4]
        print(f"\nLitros de atole disponibles: {disponibles}")  # Muestra disponibilidad
        litros_atole = int(
            input(f"¿Cuántos litros de atole desea encargar? (0 a {disponibles}): ")
        )
        if litros_atole < 0:
            print(
                "No se puede registrar una cantidad negativa. Se registrará 0."
            )  # Coloque esta validación porque en una iteración, se rompió todo por colocar un valor negativo.
            litros_atole = 0
        elif litros_atole > disponibles:
            print(
                f"Solo hay {disponibles} litros disponibles. No se puede registrar esa cantidad."
            )  # Si se piden más de los disponibles
            continuar = input(
                "¿Desea registrar una cantidad menor? (S/N): "
            ).lower()  # Se le da la opción para registrar una menor cantidad
            if continuar == "s":
                litros_atole = int(
                    input(f"Ingrese nueva cantidad (0 a {disponibles}): ")
                )
                if litros_atole > disponibles:
                    print(
                        "Aún excede el inventario. No se registrará atole."
                    )  # Se omite en tipo de producto si hay una reincidencia y no hay inventario
                    litros_atole = 0
            else:
                print("Atole no registrado.")
                litros_atole = 0  # No hay existencia
        total += litros_atole * precio_atole  # Calculamos el precio
        cantidades[4] -= litros_atole  # Descontamos la existencia del inventario

        print(
            f"\nTotal a pagar por {nombre}: ${total:.2f}"
        )  # Mostramos el total a pagar del usuario que ha apartado. .2f regresa como máximo 2 decimales.

        seguir = input("\n¿Desea registrar otro apartado? (S/N): ").lower()
        if seguir != "s":
            break  # Interrumpe la ejecución del bucle


# Estoy pensando en ingresar una validación para que cuando ya no haya inventario, notifique al usuario del sistema que no habrá venta en el mostrador. Está en desarrollo.
# Mucho de este código fue reciclado de la fase anterior

# Definimos la fase 3
# Version 2.0: Ahora la fase 3 también realiza un doble registro en archivo y memoria como la fase anterior.


def fase3_apartados():
    print("\n--- FASE 3: APARTADOS DE CLIENTES ---")
    nombre_cliente = input("Ingrese nombre del cliente: ")
    total = 0

    # Obtenemos fecha y hora actual
    ahora = datetime.now()
    marca_tiempo = ahora.strftime("%d/%m/%Y %H:%M:%S")

    # Abrimos archivo en modo append para acumular apartados
    with open("apartados.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== Apartado de {nombre_cliente} ({marca_tiempo}) ===\n")

        # Apartados de tamales
        for i in range(4):  # Los primeros 4 son tamales
            disponibles = cantidades[i]
            try:
                cantidad = int(input(f"Ingrese cantidad de {tipo_producto[i]} (0 a {disponibles}): "))
                if 0 <= cantidad <= disponibles:
                    cantidades[i] -= cantidad
                    precio = precio_salado if i < 3 else precio_dulce
                    total += cantidad * precio
                    f.write(f"{tipo_producto[i]}: {cantidad}\n")
                else:
                    print("Cantidad inválida o excede inventario.")
                    f.write(f"{tipo_producto[i]}: 0 (error de entrada)\n")
            except ValueError:
                print("Entrada inválida. Se registrará 0.")
                f.write(f"{tipo_producto[i]}: 0 (entrada inválida)\n")

        # Apartados de atole
        disponibles = cantidades[4]
        try:
            litros = int(input(f"Ingrese litros de atole (0 a {disponibles}): "))
            if 0 <= litros <= disponibles:
                cantidades[4] -= litros
                total += litros * precio_atole
                f.write(f"Litros Atole: {litros}\n")
            else:
                print("Cantidad inválida o excede inventario.")
                f.write("Litros Atole: 0 (error de entrada)\n")
        except ValueError:
            print("Entrada inválida. Se registrará 0.")
            f.write("Litros Atole: 0 (entrada inválida)\n")

        # Guardamos el total del apartado
        f.write(f"Total a pagar: ${total:.2f}\n")

    print(f"Total a pagar por {nombre_cliente}: ${total:.2f}")
    print("Apartado registrado correctamente y guardado en 'apartados.txt'.")

# Definimos la fase 4
# Version 2.0: Ahora la fase 4 sigue la misma ejecución del doble registro

def fase4_venta():
    print("\n--- FASE 4: VENTAS EN MOSTRADOR ---")
    nombre_cliente = input("Ingrese nombre del cliente: ")
    total = 0

    # Obtenemos fecha y hora actual
    ahora = datetime.now()
    marca_tiempo = ahora.strftime("%d/%m/%Y %H:%M:%S")

    # Abrimos archivo en modo append para acumular ventas
    with open("ventas.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== Venta a {nombre_cliente} ({marca_tiempo}) ===\n")

        # Ventas de tamales
        for i in range(4):  # Los primeros 4 son tamales
            disponibles = cantidades[i]
            try:
                cantidad = int(input(f"Ingrese cantidad de {tipo_producto[i]} (0 a {disponibles}): "))
                if 0 <= cantidad <= disponibles:
                    cantidades[i] -= cantidad
                    precio = precio_salado if i < 3 else precio_dulce
                    total += cantidad * precio
                    f.write(f"{tipo_producto[i]}: {cantidad}\n")
                else:
                    print("Cantidad inválida o excede inventario.")
                    f.write(f"{tipo_producto[i]}: 0 (error de entrada)\n")
            except ValueError:
                print("Entrada inválida. Se registrará 0.")
                f.write(f"{tipo_producto[i]}: 0 (entrada inválida)\n")

        # Venta de atole
        disponibles = cantidades[4]
        try:
            litros = int(input(f"Ingrese litros de atole (0 a {disponibles}): "))
            if 0 <= litros <= disponibles:
                cantidades[4] -= litros
                total += litros * precio_atole
                f.write(f"Litros Atole: {litros}\n")
            else:
                print("Cantidad inválida o excede inventario.")
                f.write("Litros Atole: 0 (error de entrada)\n")
        except ValueError:
            print("Entrada inválida. Se registrará 0.")
            f.write("Litros Atole: 0 (entrada inválida)\n")

        # Guardamos el total de la venta
        f.write(f"Total a pagar: ${total:.2f}\n")
        print(f"Total a pagar: ${total:.2f}\n")

    # Cálculo de pago y cambio
    try:
        pago = float(input(f"Ingrese cantidad entregada por {nombre_cliente}: "))
        if pago >= total:
            cambio = pago - total
            print(f"Total a pagar: ${total:.2f}")
            print(f"Pago recibido: ${pago:.2f}")
            print(f"Cambio: ${cambio:.2f}")
        else:
            print("El pago es insuficiente. La venta no se completó.")
    except ValueError:
        print("Entrada inválida para el pago. La venta no se completó.")

    print("Venta registrada correctamente y guardada en 'ventas.txt'.")


from datetime import datetime

def fase5_postventa():
    print("\n--- FASE 5: POST-VENTA ---")
    ingresos_totales = 0

    # Obtenemos fecha y hora actual
    ahora = datetime.now()
    marca_tiempo = ahora.strftime("%d/%m/%Y %H:%M:%S")

    # Abrimos archivo en modo append para acumular cierres
    with open("cierre.txt", "a", encoding="utf-8") as f:
        f.write(f"\n=== Cierre de Post-Venta ({marca_tiempo}) ===\n")

        # Bucle para calcular ingresos por producto
        for i in range(len(tipo_producto)):
            if i in [0, 1, 2]:  # Tamales salados
                precio = precio_salado
            elif i == 3:  # Tamal dulce
                precio = precio_dulce
            else:  # Atole
                precio = precio_atole

            vendidos = cantidades_iniciales[i] - cantidades[i]
            ingresos = vendidos * precio
            ingresos_totales += ingresos

            # Imprimir en pantalla
            print(f"\n{tipo_producto[i]}")
            print(f"  Vendidos: {vendidos}")
            print(f"  Restantes: {cantidades[i]}")
            print(f"  Ingresos generados: ${ingresos:.2f}")

            # Guardar en archivo
            f.write(f"{tipo_producto[i]}:\n")
            f.write(f"  Vendidos: {vendidos}\n")
            f.write(f"  Restantes: {cantidades[i]}\n")
            f.write(f"  Ingresos generados: ${ingresos:.2f}\n")

        # Totales
        print(f"\nIngresos totales del día: ${ingresos_totales:.2f}")
        print("Cierre registrado. Buen día.")

        f.write(f"Ingresos totales del día: ${ingresos_totales:.2f}\n")
        f.write("Cierre registrado. Buen día.\n")


 # Definimos la función de un menú principal para poder ubicarnos en cada una de las fases del sistema
 # Version 2.0 el menú ahora se muestra en una tabla para mantener consistencia visual
def menu_principal_tamales(): 
    while True:
        print("")
        print("|-----------------------------------------------------------|")
        print("| ===    MENÚ TAMALES        |       TAMALERÍA LUCÍA    === |")
        print("|-----------------------------------------------------------|")
        print("| 1. Registro Ingredientes   | 2. Registro Producción       |")
        print("| 3. Registro Apartados      | 4. Venta en Mostrador        |")
        print("| 5. Post-venta y Cierre     | 6. Menú Anterior             |")
        print("| 7. Salir                   |                              |")
        print("|-----------------------------------------------------------|")
        print("")
        
        opcion = input_con_inactividad("Seleccione una opción: ")

        if opcion is None:  # Caso "no" → regresar a inicio de sesión
            usuario = inicio_sesion()
            continue
        elif opcion == "continuar":  # Caso "si" → seguir en el menú
            continue
        # De acuerdo a la opción deseada, se ejecuta la función correspondiente a esa fase

        if opcion == "1":
            fase1_compra()
        elif opcion == "2":
            fase2_produccion()
            global cantidades_iniciales  # Definimos una variable global
            cantidades_iniciales = (
                cantidades.copy()
            )  # haciendo copia de las cantidades registradas en la fase de producción
        elif opcion == "3":
            fase3_apartados()
        elif opcion == "4":
            fase4_venta()
        elif opcion == "5":
            fase5_postventa()
        elif opcion == "6":
            return
        elif opcion == "7":
            salir_sistema()
        else:
            print(
                "Opción no válida. Intente de nuevo."
            )  # En caso de elegir un campo incorrecto


# Punto de entrada del programa
if __name__ == "__main__":
    usuario = inicio_sesion()  # Interacción inicial
    menu_principal_archivo(usuario)
    menu_principal_tamales()