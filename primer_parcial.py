# UTN-Capital, una reconocida aplicación que opera en la bolsa desea registrar la información de
# las transacciones que realiza un grupo vip de 15 clientes. Se necesita contabilizar la cantidad de
# acciones que compró cada cliente. Las acciones más relevantes son: Apple, Tesla y NVIDIA. Los
# precios de cada acción se detallan en la siguiente tabla:
# Necesitamos un programa que permita realizar la carga de la cantidad de acciones que adquirió
# cada cliente (realizada a mano con una carga secuencial en donde el la cantidad de acciones
# debe ser un número positivo, incluyendo el cero, hasta 500). Luego realizar un menú que
# resuelva en cada opción los siguientes requerimientos:

# 1. La cantidad de acciones que dispone cada cliente.
# 2. Porcentaje de cada tipo de acción, sobre el total de acciones de todos los clientes.
# Necesitamos saber también cuál fue la o las acciones con el menor porcentaje.
# 3. Total de la inversión en dólares de cada cliente.
# Acción Precio en USD
# Apple 70
# Tesla 90
# NVIDIA 105
# 4. Realizar un informe que muestre por cada cliente, sus tenencias en dólares, ordenadas
# de mayor a menor.
# 5. La cantidad de clientes que hayan invertido en Apple, pero no en Tesla. Mostrar además
# el porcentaje que representa esa cantidad respecto al total de clientes.

################################################################################################################################################
# 1. La cantidad de acciones que dispone cada cliente.

def calcular_acciones_por_cliente(inversiones: list) -> list:
    acciones_por_cliente = [0] * len(inversiones)
    for c in range(len(inversiones)): # Cliente (fila)
        acumulador = 0
        for a in range(len(inversiones[c])): # Acciones (columna)
            acumulador += inversiones[c][a]
        acciones_por_cliente[c] = acumulador
    return acciones_por_cliente

# 2. Porcentaje de cada tipo de acción, sobre el total de acciones de todos los clientes.
# Necesitamos saber también cuál fue la o las acciones con el menor porcentaje.

def calcular_total_acciones (inversiones: list) -> list:
    total_acciones = [0] * len(inversiones[0])
    for a in range(len(inversiones[0])):    #calcula el total de acciones
        acumulador = 0
        for c in range(len(inversiones)):
            acumulador += inversiones[c][a]
        total_acciones[a] = acumulador

    return total_acciones

def obtener_totalidad_acciones(total_acciones: list) -> int:
    total = 0
    for a in range(len(total_acciones)):
        total += total_acciones[a]
    # VERSION BERRETA DE CALCULAR TOTAL
    # for c in range(len(inversiones)):
    #     for a in range(len(inversiones[0])):
    #         total += inversiones[c][a]
    # print(total)
    return total

def calcular_porcentajes(total_acciones: list, total: int) -> list:
    porcentajes = [0] * len(total_acciones)
    for a in range(len(total_acciones)):
        porcentajes[a] = (total_acciones[a] * 100) / total
    return porcentajes


def calcular_minimo_porcentaje (inversiones: list, acciones: list) -> list:
    total_acciones = calcular_total_acciones(inversiones)
    total = obtener_totalidad_acciones(total_acciones)
    porcentajes = calcular_porcentajes(total_acciones, total)

    print(porcentajes)
    minimo = 0
    bandera = False
    for a in range(len(acciones)):
        if bandera == False or minimo > porcentajes[a]:
            minimo = porcentajes[a]
            bandera = True

    print(f"El minimo es:{minimo} y la/s accion/es son:")
    for a in range(len(acciones)):
        if minimo == porcentajes[a]:
            print(f"\t |{acciones[a]}|")

# 3. Total de la inversión en dólares de cada cliente.

def calcular_inversion_cliente(inversiones: list, precios: list,) -> list:
    inversion_dolares = [0] * len(inversiones)
    for c in range(len(inversiones)):
        for a in range(len(inversiones[c])):
            inversion_dolares[c] += inversiones[c][a] * precios[a]                                               
    return inversion_dolares

# 4. Realizar un informe que muestre por cada cliente, sus tenencias en dólares, ordenadas
# de mayor a menor.

def ordenar_dolares_clientes() -> list:
    inversion_dolares = calcular_inversion_cliente(inversiones, precios)
    auxiliar = 0
    dolares_ordenados = inversion_dolares
    for i in range(len(inversion_dolares)):
        for j in range(len(inversion_dolares)- 1):
            if dolares_ordenados[j] < dolares_ordenados[j + 1]:
                auxiliar = dolares_ordenados[j]
                dolares_ordenados[j] = dolares_ordenados[j + 1]
                dolares_ordenados[j + 1] = auxiliar
    return dolares_ordenados

# 5. La cantidad de clientes que hayan invertido en Apple, pero no en Tesla. Mostrar además
# el porcentaje que representa esa cantidad respecto al total de clientes.

def clientes_apple_no_tesla(inversiones: list) -> int:
    clientes_apple_no_tesla = 0
    for a in range(len(inversiones[0])):
        for c in range(len(inversiones)):
            if a == 0:
                if inversiones[c][a] > 0 and inversiones[c][a + 1] == 0:
                    clientes_apple_no_tesla += 1
    return clientes_apple_no_tesla

def porcentaje_clientes_apple_no_tesla() -> float:
    clientes_no_tesla = clientes_apple_no_tesla(inversiones)
    porcentaje = (clientes_no_tesla / len(inversiones)) * 100
    return porcentaje

########################################

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial:int) -> list:
    inversiones = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        inversiones += [fila]
    
    return inversiones



def cargar_matriz_inversiones(inversiones: list, acciones: list) -> None:

    for i in range(len(inversiones)):
        for j in range(len(inversiones[i])):
            inversiones[i][j] = int(input(f"Ingrese el numero de acciones (entre 0 y 500) q tiene el cliente {i} en la empresa {acciones[j]}: "))
            while inversiones[i][j] < 0 or inversiones[i][j] > 500:
                inversiones[i][j] = int(input(f"Error. Reingrese el numero de acciones (entre 0 y 500) q tiene el cliente {i} en la empresa {acciones[j]}: "))



def mostrar_matriz_inversiones(inversiones: list) -> None:
    for i in range(len(inversiones)):
        for j in range(len(inversiones[0])):
            print(inversiones[i][j], end="\t")
        print()
    



def probar_boludeces (inversiones):
    long = len(inversiones[0])
    print(long)







################################################################################################################################################
# inversiones = [
#     [500,200,200],
#     [300,0,0],
#     [150,0,0],
#     [200,150,150],
#     [10,30,30]
# ]

# inversiones = [
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     []
# ]

precios = [70,90,105]
acciones = ["Apple", "Tesla", "NVIDIA"]

# calcular_acciones_por_cliente(inversiones)

# calcular_minimo_porcentaje(inversiones, acciones)

# calcular_inversion_cliente(inversiones, precios)

# ordenar_dolares_clientes()

# clientes_apple_no_tesla(inversiones)

while True:
    opcion = input("1. Cargar matriz inversiones\n"
                   "2. Cantidad acciones que dispone cada cliente\n"
                   "3. porcentaje de cada tipo de acciones\n"
                   "4. Menor pocentaje de tipo de acciones\n"
                   "5. Total de la inversión en dólares de cada cliente\n"
                   "6. informe que muestre por cada cliente, sus tenencias en dólares, ordenadas de mayor a menor.\n"
                    "7. La cantidad de clientes que hayan invertido en Apple, pero no en Tesla. Mostrar además el porcentaje que representa esa cantidad respecto al total de clientes\n"
                    "8. Salir.\n")
    match opcion:
        case "1":
            inversiones = crear_matriz(15,3,0)
            cargar_matriz_inversiones(inversiones, acciones)
            mostrar_matriz_inversiones(inversiones)
        case "2":
            acciones_por_cliente = calcular_acciones_por_cliente(inversiones)
            print(f"La cantidad de acciones que dispone cada cliente son {acciones_por_cliente}")
        case "3":
            total_acciones = calcular_total_acciones(inversiones)
            total = obtener_totalidad_acciones(total_acciones)
            porcentaje_tipo_de_accion = calcular_porcentajes(total_acciones, total)
            print(f"El porcentaje de cada tipo de accion son {porcentaje_tipo_de_accion}")
        case "4":
            menor_porcentaje = calcular_minimo_porcentaje(inversiones, acciones)
        case "5":
            total_inversion_dolares_por_cliente = calcular_inversion_cliente(inversiones, precios)
            print(f"El total de inversion de cada cliente son {total_inversion_dolares_por_cliente}")
        case "6":
            dolares_ordenados = ordenar_dolares_clientes()
            print(f"tenencias ordenadas de MAYOR a MENOR {dolares_ordenados}")
        case "7":
            clientes_invertidos_en_apple_no_tesla = clientes_apple_no_tesla(inversiones)
            porcentaje_apple_no_tesla = porcentaje_clientes_apple_no_tesla()
            print(f"La cantidad de clientes que invirtieron en Apple pero no en tesla son {clientes_invertidos_en_apple_no_tesla} y sus porcentajes {porcentaje_apple_no_tesla}")

        case "8":
            print("Saliendo...")
            break
        case _:
            print("INGRESA BIEN EL NUMERITO FLAQUITO")