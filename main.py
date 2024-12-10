# Juego de ahorcado

'''
Samuel Ospina
Salomon Castaño
Grupo 4
'''

#Importación de módulos
from ahorcado import *


"""
Instrucciones:

¡Bienvenido al juego del ahorcado!

En el juego deberás ingresar letras hasta encontrar la palabra secreta o gastar todas tus vidas y por lo tanto morir.

Primero que todo debes iniciar un modo de juego:

1. Ingresar palabra secreta
*Si eliges la opción 1, deberás ingresar una palabra secreta para que otro jugador la adivine. 

2. Seleccionar de un archivo
*Si eliges la opción 2, se cargará una lista de palabras desde un archivo y se elegirá una al azar 
para que otro jugador la adivine.

Cuando se haya seleccionado el modo de juego, debes empezar a ingresar letras. Si la letra que
ingresaste está en la palabra secreta, se mostrará la posición sin un "_" mostrando la letra.
Por otra parte si no está en la palabra, perderás una vida.

Tienes 8 vidas para adivinar la palabra. Si se se acaban tus vidas antes de adivinar la palabra, perderás el juego. 
Si adivinas la palabra antes de agotar tus vidas, ganarás un viaje a Cuba.

Al finalizar cada turno tendrás la opción de continuar o terminar la ejecución del programa.
13/04/2023
Version 1.3 

"""


# Despliegue de la introducción
printIntro('intro.txt')

# Variables globales
letrasIntentadas = ' ' # Letras que ha intentado el usuario
numeroIntentos = 8 # Número de intentos que tiene el usuario
IntentosGraficos = 0 #Posicion del modo gráfico
otraVez = 'y' # Inicialización de la variable para jugar otra vez
ContPalabrasIntentadas = 0 #Contador de palabras adivinadas durante el tiempo de ejecución total del programa 
ContPalabrasAdivinadas = 0 #Contador de palabras intentadas durante el tiempo de ejecución total del programa

while otraVez.lower() == 'y':

    ''' Inicio ciclo de nuevo juego '''
    # Selección del modo de juego (1: palabra secreta, 2: archivo)
    print("** SELECCIÓN DEL MODO DE JUEGO ** \n 1.Ingresar palabra secreta \n 2.Seleccionar de un archivo \n ")
 
    # Código para la selección del modo de juego
    #modo = validar_modo()
    modo = ""
    while modo != "1" and modo != "2":
        modo = input("Seleccione una opción: ")
        if modo  != "1" and modo != "2":
            print("Ingrese una opción valida ")


    if modo == "1":

        caracteresInvalidos = "0123456789!@#\$%\^&\*\(\)_\+-=\[\]{}\\\|;':\",.<>\?\/"
        contCaracteresInvalidos = 1

        while contCaracteresInvalidos != 0:
            contCaracteresInvalidos = 0
            p = inputSecret()
            for caracter in p:
                if caracter in caracteresInvalidos:
                    contCaracteresInvalidos += 1
                    print("Ingrese una palabra valida")
                    break

    elif modo == "2":
        print("Cargando una lista de super heroes desde el archivo superHeroes.txt")
        p = pickWord(loadWords("superHeroes.txt"),",")

    ContPalabrasIntentadas += 1
    # Inicialización de la bandera que indica si se terminó una ronda
    ban = 1

    # Código para imprimir las estadísticas
    vidas_grafica("vidas_grafica.txt","?",IntentosGraficos)
    print("-----------------------------------------------")
    print("Usted tiene", numeroIntentos, "vidas disponibles")
    print("Usted tiene disponibles las siguientes letras:", obtenerLetrasDisponibles(letrasIntentadas))
    print("Palabra secreta: ", obtenerParteAdivinada(p, letrasIntentadas))
    print("El número de palabras adivinadas es", ContPalabrasAdivinadas)
    print("El número de palabras intentadas es:", ContPalabrasIntentadas)
    while ban == 1:


		# Solicitud interactiva de letras
		# Código para la solicitud interactiva de letras
        while True:

            ingresar_letra = input("Ingrese una letra: ").lower()
            if len(ingresar_letra) != 1 or not ingresar_letra.isalpha():
                print("Ingrese una letra valida")
            elif ingresar_letra in letrasIntentadas:
                print("Esta letra ya fue ingresada, por favor intente con otra letra")
            else:
                letrasIntentadas += ingresar_letra
                break

        # Verificación de la letra y actualización de la palabra oculta        
        if verificarLetraIngresada(ingresar_letra.lower(),p):
            print("Letra Acertada")
        else:
            print("Letra no se encuentra en la palabra")
            numeroIntentos -= 1
            IntentosGraficos += 1

		# Impresión del estado del juego (número de intentos, letras disponibles)
		# Código para imprimir el estado del juego
        vidas_grafica("vidas_grafica.txt","?",IntentosGraficos)    
        print("-----------------------------------------------")
        print("Usted tiene", numeroIntentos, "vidas")
        print("Usted tiene disponibles las siguientes letras:", obtenerLetrasDisponibles(letrasIntentadas))
        print("Palabra secreta: ", obtenerParteAdivinada(p, letrasIntentadas))

		# Verificación de la condición de finalización del juego
        
		# Códigos para verificar la condición de finalización del juego
        if palabraAdivinada(p,letrasIntentadas):
            print("Felicitaciones la palabra secreta es:", p, "has ganado un viaje a Cuba")
            ContPalabrasAdivinadas += 1
            print("-----------------------------------------------")
            ban = 0
            break
        elif numeroIntentos == 0:
            print("Lo lamento, has perdido, la palabra secreta era:", p, ". Animo")
            print("-----------------------------------------------")
            ban = 0
            break
        ''' Fin ciclo para adivinar la palabra oculta '''

    #Solicitud nuevo juego
    deNuevo= ""
    while deNuevo != "y" and deNuevo != "n":
        deNuevo = input("Desea jugar otra vez (y/n): ").lower()
        if deNuevo != "y" and deNuevo != "n":
            print("ingrese una opción valida")
    otraVez = deNuevo
    print("-- ---------------------------------------------")

	# Reinicialización de las variables necesarias
	# Código para reinicializar las variables necesarias
    letrasIntentadas = ' ' # Letras que ha intentado el usuario
    numeroIntentos = 8 # Número de intentos que tiene el usuario
    IntentosGraficos = 0

