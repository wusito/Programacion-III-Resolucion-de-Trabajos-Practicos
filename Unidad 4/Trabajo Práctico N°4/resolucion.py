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
        



def main():
    opc = -1

    while opc != 0:
        mostrarMenu()
        opc = int(input("Selecciones una opción (en números): "))

        if opc == 1:
            ejercicio1()
        elif opc == 5:
            pressEnterToContinue()
            break
        else:
            print("Opción inválida, intente nuevamente.")
            pressEnterToContinue()




# La función main se ejecuta como predefinida predefinida.
if __name__ == "__main__":
    main()
