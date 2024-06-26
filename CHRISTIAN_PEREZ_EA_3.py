from datetime import date

def mostrar_mapa(mapa_asientos):
    for enumeracion in range(0,50,10):
        fila = ""
        for columna in range(10):
            fila += f"{mapa_asientos[enumeracion + columna]} \t"
        print(fila)

def calcular_precio(asiento):
    if  1 <= asiento <= 20:
        return 100000
    elif 20 < asiento <= 30:
        return 50000
    elif 30 < asiento <= 50:
        return 10000

def mostrar_rut(lista_rut):
    print("\t***LISTADO DE RUT INGRESADOS***")
    for rut in lista_rut:
        print(rut)

def comprar(mapa_asientos):
    total_precio = 0

    cantidad_entradas = int(input("Ingrese cantidad de entradas a comprar (Max.2): "))
    while cantidad_entradas < 1 or cantidad_entradas > 2:
        print("\nSolamente puede comprar de 1 a 2 entradas.")
        cantidad_entradas = int(input("Intente nuevamente (Max.2): "))

    for contador in range(cantidad_entradas):
        mostrar_mapa(mapa_asientos)
        asiento = int(input("\nCompra N° "+ str(contador+1) + ", ingrese el asiento que desea comprar: "))
        while asiento > 50 or asiento < 1 or mapa_asientos[asiento - 1] == "X":
            print("No está disponible")
            asiento = int(input("Eliga un asiento entre el 1 al 50 que no este ocupado: "))
        
        mapa_asientos[asiento - 1] = "X"
        ingreso_rut = int(input("Ingrese su rut: "))
        lista_rut.append(ingreso_rut)
        lista_rut.sort()
        print("Operación realizada correctamente.")
        total_precio += calcular_precio(asiento)
    return total_precio

mapa_asientos = []
for contador in range(1,51):
    mapa_asientos.append(contador)

lista_rut = []

ganancias_totales = 0

dia = date.today()

while True:
    print("""
    1) Comprar entradas
    2) Mostrar ubicaciones disponibles
    3) Ver listado de asistencia
    4) Mostrar ganancias totales
    5) Salir
    """)
    try:    
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("*****Opción no válida, intente nuevamente*****")
        opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            ganancia = comprar(mapa_asientos)
            ganancias_totales += ganancia
        case 2:
            mostrar_mapa(mapa_asientos)
        case 3:
            mostrar_rut(lista_rut)
        case 4:
            print("Las ganancias totales de ventas hasta ahora son de:")
            print("$", ganancias_totales)
        case 5:
            print("Christian Matias Pérez Vera "+ str(dia))
            break
        case _:
            print("*****Opción no válida, intente nuevamente*****")