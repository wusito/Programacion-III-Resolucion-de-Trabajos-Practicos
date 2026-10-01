# Librerías importadas y parámetros fijos.
import subprocess
import os

def pressEnterToContinue():
    input("\nPresiona la tecla Enter para continuar...")

def mostrarMenu():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print("""
        \n ------- MENÚ DE OPCIONES ------- \n
        1 - EJERCICIO N°1
        2 - EJERCICIO N°2
        3 - EJERCICIO N°3
        4 - EJERCICIO N°4
        5 - SALIR
        """)





""" ----------------------------------------------------------------------------------------------------------------

Ejercicio Nro 1: Validación de entrada y búsqueda en una Lista.

Implementar un programa que valide la entrada de un número entero y verifique su presencia en
una lista.

Requisitos:
    1. Solicitar al usuario que ingrese un número entero del 0 al 9.
    2. Mientras el número ingresado no esté en el rango especificado, repetir la solicitud.
    3. Verificar si el número se encuentra en una lista predefinida de números.
    4. Notificar al usuario si el número está o no en la lista.

Concepto útil: Utilizar la sintaxis [valor] in [lista] para comprobar la presencia de un valor en una
lista.

---------------------------------------------------------------------------------------------------------------- """

def ejercicio1():
    listaNumerica = [3, 6, 7, 9]
    band = True

    while band:
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        print(" ---------------------- EJERCICIO N°1 ----------------------")
        
        try:
            numeroIngresado = int(input("\nIngrese un número entero: "))
        except ValueError:
            print("Por favor, ingrese un número válido (no letras).")
            pressEnterToContinue()
            continue

        if numeroIngresado >= 0 and numeroIngresado <= 9:
            if numeroIngresado in listaNumerica:
                print("El número ingresado SI se encuentra en la lista predefinida.")
                band = False
            else:
                print("El número ingresado NO se encuentra en la lista predefinida.")
            
            pressEnterToContinue()
        else:
            print("Ingrese un número válido (entre 0 y 9).")
            pressEnterToContinue()





""" ----------------------------------------------------------------------------------------------------------------

Ejercicio Nro 2: Gestión de Conjuntos de Usuarios y Administradores

Requisitos:
    1. Crear un conjunto llamado usuarios con los nombres: Marcela, David, Elvira, Juan, y Marcos.
    2. Crear un conjunto llamado administradores con los nombres: Juan y Marcela.
    3. Eliminar a Juan del conjunto de administradores.
    4. Añadir a Marcos como administrador, pero mantenerlo en el conjunto de usuarios.
    5. Mostrar todos los usuarios, indicando si cada uno es administrador o no.

Sugerencia: Utilizar el método .discard(elemento) para eliminar un elemento de un conjunto.

---------------------------------------------------------------------------------------------------------------- """

def ejercicio2():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print(" ---------------------- EJERCICIO N°2 ----------------------")

    usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"}
    administradores = {"Juan", "Marcela"}

    administradores.discard("Juan")
    administradores.add("Marcos")

    print("\nEstado actual de los usuarios:")
    for usuario in usuarios:
        if usuario in administradores:
            print(f"    - {usuario}: Es Administrador")
        else:
            print(f"    - {usuario}: No es Administrador")

    pressEnterToContinue()





""" ----------------------------------------------------------------------------------------------------------------

Ejercicio Nro 3: Registro de Información en un Diccionario.

Requisitos:
    1. Solicitar al usuario que ingrese los siguientes datos: nombre, edad, dirección y teléfono.
    2. Almacenar los datos en un diccionario llamado usuario_info.
    3. Permitir el ingreso de información para varios usuarios.
    4. Mostrar la información ingresada para cada usuario en formato clave-valor.

---------------------------------------------------------------------------------------------------------------- """

def ejercicio3():
    lista_usuarios = []

    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print(" ---------------------- EJERCICIO N°3 ----------------------")

    while True:
        nombre = input("\nIngrese el nombre: ")
        edad = input("Ingrese la edad: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")

        usuario_info = {
            "Nombre": nombre,
            "Edad": edad,
            "Dirección": direccion,
            "Teléfono": telefono
        }
        
        lista_usuarios.append(usuario_info)
        
        continuar = input("\nDesea registrar otro usuario? (s/n): ").lower()
        if continuar != 's':
            break
        print("\n" + "-" * 60)

    pressEnterToContinue()
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    print("\n--- INFORMACIÓN DE USUARIOS REGISTRADOS ---")
    for i, usuario in enumerate(lista_usuarios, start=1):
        print(f"\nUsuario Nro {i}:")
        for clave, valor in usuario.items():
            print(f"    {clave}: {valor}")

    pressEnterToContinue()





""" ----------------------------------------------------------------------------------------------------------------

Ejercicio Nro 4: Gestión de Inventario de Instrumentos Musicales

Una fábrica de instrumentos musicales posee diferentes sucursales. Cada sucursal tiene un
nombre y una lista de instrumentos disponibles para la venta.
De cada instrumento se conoce:
     ID: identificador alfanumérico.
     Precio: precio del instrumento.
     Tipo: puede ser Percusión, Viento o Cuerda.

Implementar una solución que permita gestionar el inventario.

Requisitos:
    1. listarInstrumentos()
    Mostrar en la consola todos los instrumentos disponibles, indicando sucursal, ID, precio y
    tipo.
    2. instrumentosPorTipo(tipo)
    Recibir como parámetro un tipo de instrumento y devolver una lista con los instrumentos
    que pertenecen a ese tipo.
    3. borrarInstrumento(id)
    Recibir un ID y eliminar el instrumento correspondiente de la sucursal en la que se
    encuentre.
    4. porcInstrumentosPorTipo(sucursal)
    Recibir el nombre de una sucursal y mostrar o retornar el porcentaje de instrumentos
    correspondientes a cada tipo:
        o Percusión
        o Viento
        o Cuerda

---------------------------------------------------------------------------------------------------------------- """

def ejercicio4():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    print(" ---------------------- EJERCICIO N°4 ----------------------")

    class Instrumento:
        def __init__(self, id_alfanumerico, precio, tipo):
            self.id = id_alfanumerico
            self.precio = precio
            self.tipo = tipo  # Percusión, Viento o Cuerda.

        def __str__(self):
            return f"ID: {self.id} | Tipo: {self.tipo} | Precio: ${self.precio:.2f}"

    class Sucursal:
        def __init__(self, nombre):
            self.nombre = nombre
            self.instrumentos = []

        def agregar_instrumento(self, instrumento):
            self.instrumentos.append(instrumento)

    class Fabrica:
        def __init__(self):
            self.sucursales = []

        def agregar_sucursal(self, sucursal):
            self.sucursales.append(sucursal)

        # Requisito 1: listarInstrumentos().
        def listarInstrumentos(self):
            print("\n--- INVENTARIO GLOBAL DE INSTRUMENTOS ---")
            for suc in self.sucursales:
                for inst in suc.instrumentos:
                    print(f"Sucursal: {suc.nombre} | {inst}")

        # Requisito 2: instrumentosPorTipo(tipo).
        def instrumentosPorTipo(self, tipo):
            resultado = []
            for suc in self.sucursales:
                for inst in suc.instrumentos:
                    if inst.tipo.lower() == tipo.lower():
                        resultado.append(inst)
            return resultado

        # Requisito 3: borrarInstrumento(id).
        def borrarInstrumento(self, id_buscar):
            eliminado = False
            for suc in self.sucursales:
                for inst in suc.instrumentos:
                    if inst.id == id_buscar:
                        suc.instrumentos.remove(inst)
                        print(f"\n[OK] Instrumento {id_buscar} eliminado de la sucursal {suc.nombre}.")
                        eliminado = True
                        break
            if not eliminado:
                print(f"\n[Error] No se encontró ningún instrumento con ID {id_buscar}.")

        # Requisito 4: porcInstrumentosPorTipo(sucursal).
        def porcInstrumentosPorTipo(self, nombre_sucursal):
            sucursal_encontrada = None
            for suc in self.sucursales:
                if suc.nombre.lower() == nombre_sucursal.lower():
                    sucursal_encontrada = suc
                    break

            if not sucursal_encontrada:
                print(f"\n[Error] La sucursal '{nombre_sucursal}' no existe.")
                return

            total = len(sucursal_encontrada.instrumentos)
            if total == 0:
                print(f"\nLa sucursal {sucursal_encontrada.nombre} no tiene instrumentos en stock.")
                return

            conteo = {"Percusión": 0, "Viento": 0, "Cuerda": 0}
            for inst in sucursal_encontrada.instrumentos:
                if inst.tipo in conteo:
                    conteo[inst.tipo] += 1

            print(f"\nPorcentajes de inventario para Sucursal: {sucursal_encontrada.nombre}")
            for tipo, cantidad in conteo.items():
                porcentaje = (cantidad / total) * 100
                print(f"- {tipo}: {porcentaje:.2f}%")


    # Pruebas del sistema.
    mi_fabrica = Fabrica()

    sucursal_norte = Sucursal("Sucursal Norte")
    sucursal_sur = Sucursal("Sucursal Sur")

    sucursal_norte.agregar_instrumento(Instrumento("G01", 15000, "Cuerda"))
    sucursal_norte.agregar_instrumento(Instrumento("B01", 25000, "Percusión"))
    sucursal_norte.agregar_instrumento(Instrumento("V01", 12000, "Viento"))
    sucursal_norte.agregar_instrumento(Instrumento("G02", 45000, "Cuerda"))

    sucursal_sur.agregar_instrumento(Instrumento("V02", 18000, "Viento"))
    sucursal_sur.agregar_instrumento(Instrumento("B02", 30000, "Percusión"))

    mi_fabrica.agregar_sucursal(sucursal_norte)
    mi_fabrica.agregar_sucursal(sucursal_sur)

    mi_fabrica.listarInstrumentos()

    tipo_buscado = "Cuerda"
    print(f"\n--- Instrumentos de tipo {tipo_buscado} ---")
    for inst in mi_fabrica.instrumentosPorTipo(tipo_buscado):
        print(inst)

    mi_fabrica.borrarInstrumento("B01")
    mi_fabrica.listarInstrumentos()

    mi_fabrica.porcInstrumentosPorTipo("Sucursal Norte")

    pressEnterToContinue()





# Función principal.
def main():
    opc = -1

    while opc != 0:
        mostrarMenu()
        opc = int(input("Selecciones una opción (en números): "))

        if opc == 1:
            ejercicio1()
        elif opc == 2:
            ejercicio2()
        elif opc == 3:
            ejercicio3()
        elif opc == 4:
            ejercicio4()
        elif opc == 5:
            pressEnterToContinue()
            break
        else:
            print("Opción inválida, intente nuevamente.")
            pressEnterToContinue()

# La función main se ejecuta como predefinida predefinida.
if __name__ == "__main__":
    main()