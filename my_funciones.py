import random


def Verificacion(cadena: str):
   baderaMayus = False
   banderaMinus = False
   banderaNum = False

   for i in range(len(cadena)):
        if cadena[i].isupper() == True:
            baderaMayus = True
        elif cadena[i].islower() == True:
            banderaMinus = True
        elif cadena[i].isdigit() == True:
            banderaNum = True
        
   if(baderaMayus and banderaMinus and banderaNum) == True:
        return True
   else:
        return False
pass

def caracter_aleatorio()-> str:

    letraAleatoria = chr(random.randint(65,90))

    return letraAleatoria


def inicializar_matriz_aleatoria(cantidad_filas: int,cantidad_columnas: int)-> list:
    matriz = []

    for i in range(cantidad_filas):
        fila = [0] * cantidad_columnas

        matriz += [fila]

    for i in range((len(matriz))):
        for j in range((len(matriz[i]))):
            aleatorio = random.randint(1,2)

            if aleatorio == 1:
                matriz[i][j] = random.randint(1,9)
            else:
                matriz[i][j] = caracter_aleatorio()
   
    return matriz
pass

def generar_lista_aleatoria(numeros:int):
    lista = [0] * numeros
    for i in range(len(lista)):
        lista[i] = random.randint(1,100)
    
    return lista


#Funcion que solicita un numero decimal con numero ilimitado de reintentos
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    while True:
        try:
            numero = int(input(f"{mensaje} "))
            
            if minimo <= numero <= maximo:
                return numero  
            else:
                print(mensaje_error)  
        except ValueError:
            print("Error: Debe ingresar un número válido.")  

#Funcion que solicita un numero entero con una cantidad de reintentos
def get_int_con_reintentos(mensaje:str,mensaje_error:str, minimo:int, maximo:int, reintentos:int) ->float|None: 

    i = 0
    numero = int(input(f"{mensaje} :"))

    while(numero <= minimo or numero >= maximo and i < reintentos - 1):
        i +=1
        if(numero < minimo):
            numero = int(input(f"{mensaje_error}ingrese un numero mayor (intento {i+1}):"))
        else:
            numero = int(input(f"{mensaje_error}ingrese un numero menor (intento {i+1}):"))

        if(i == reintentos -1):
            numero == None
    return numero

#Funcion que solicita un numero decimal con numero ilimitado de reintentos
def get_float(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> float:
    while True:
        try:
            numero = float(input(f"{mensaje} "))
            
            if minimo <= numero <= maximo:
                return numero  
            else:
                print(mensaje_error)  
        except ValueError:
            print("Error: Debe ingresar un número válido.")  

#Funcion que solicita un numero decimal con una cantidad de reintentos
def get_float_con_reintentos(mensaje:str,mensaje_error:str, minimo:int, maximo:int, reintentos:int) ->float|None: 

    i = 0
    numero = float(input(f"{mensaje} :"))

    while(numero <= minimo or numero >= maximo and i < reintentos - 1):
        i +=1
        if(numero < minimo):
            numero = float(input(f"{mensaje_error}ingrese un numero mayor (intento {i+1}):"))
        else:
            numero = float(input(f"{mensaje_error}ingrese un numero menor (intento {i+1}):"))

        if(i == reintentos -1):
            numero == None
    return numero

#Funcion que pide un string con numero ilimitado de reintentos
def get_string(mensaje:str,mensaje_error:str, minimo:int, maximo:int) -> str:
    
	string = input(f"{mensaje}")

	while( not string.isalpha() or len(string) > maximo or len(string) < minimo):
		print(f"{mensaje_error}")  
		string = input(f"{mensaje} ")
		
	return string

#Funcion que pide un string con una cantidad de reintentos
def get_str_con_reintentos(mensaje:str,mensaje_error:str, minimo:int, maximo:int, reintentos:int) ->str|None: 

    i = 0
    cadena = str(input(f"{mensaje} :"))

    while((len(cadena) < minimo or len(cadena) > maximo) and i < reintentos - 1):
        i +=1
        if(len(cadena) < minimo):
            cadena = str(input(f"{mensaje_error}{mensaje} (intento {i+1}):"))
        else:
            cadena = str(input(f"{mensaje_error}{mensaje} (intento {i+1}):"))

    if(i == reintentos -1):
        cadena = None
    
    return cadena

#Funcion que inicializa una matriz con la cantidad de fila y cantidad de columas proporcionado ademas de el valor inicial indicado
def inicializar_matriz(cantidad_filas: int,cantidad_columnas: int,valor_inicial: any)-> list:
    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz
pass
#Funcion que modifica la matriz en la fila y la columna indicada
def modificar_matriz(matr:list, fila:int, columna:int):
    estado = 0
    if matr[fila][columna] == 0:
        matr[fila][columna] = 1
        estado = 1

    return matr,estado

#funcion que imprime una matriz proporcionada
def imprimir_matriz(matriz):
    
    for i in range((len(matriz))):
        for j in range((len(matriz[i]))):
            print(matriz[i][j],end= " | ")
        print("")
pass

#funcion que ordena una lista por el metodo de burbujeo
def ordenar_lista_burbujeo(lista:list):

    for i in range(len(lista)):
        for j  in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                cambio = lista[i]
                lista[i] = lista[j]
                lista[j] = cambio
    return lista

#funcion que ordena una lista por el metodo de seleccion
def ordenar_lista_selecion(lista:list,orden:str):

    if orden == "ASC":
        for i in range(len(lista)):       
            min = i                #guardar el valor minimo de la iteracion

            for j in range(i+1,len(lista)):   #recorro el ciclo uno mas adelante
                if lista[min] > lista[j]:     #comparo el minimo que tengo guardado con el que recorro
                    min = j                   # si el nuevo numero es menor , actualizo el minimo

            temp = lista[i]                   #intercambio los valores colocando el minimo encontrado en
            lista[i] = lista[min]             #en la posicion donde deberia ir, asi ordenandolo
            lista[min] = temp
    else:
        for i in range(len(lista)):       
            min = i                #guardar el valor minimo de la iteracion

            for j in range(i+1,len(lista)):   #recorro el ciclo uno mas adelante
                if lista[min] < lista[j]:     #comparo el minimo que tengo guardado con el que recorro
                    min = j                   # si el nuevo numero es menor , actualizo el minimo

            temp = lista[i]                   #intercambio los valores colocando el minimo encontrado en
            lista[i] = lista[min]             #en la posicion donde deberia ir, asi ordenandolo
            lista[min] = temp
   

        
    return lista

#funcion que calcula el maximo d euna lista
def calcular_maximo(lista:list):
    if len(lista) == 0:  
        return 0 
    band = 1
    for i in range(len(lista)):
        if band == 1 or lista[i] >= maximo : 
            maximo = lista[i]
            band = 0

    return maximo
pass

def calcular_minimo(lista:list):
    if len(lista) == 0: 
        return 0 
    band = 1
    for i in range(len(lista)):
        if band == 1 or lista[i] <= maximo : 
            maximo = lista[i]
            band = 0

    return maximo
pass

#Funcion que calcula Los maximos de una lista proporcionada
def calcular_maximos_lista(lista:list)->list:
    if len(lista) == 0:  # Verifica si la lista está vacía
        return 0 
    
    maximo = lista[0]  # Inicializa el máximo con el primer elemento
    posiciones = []  # Lista para almacenar posiciones

    for i in range(len(lista)):
        if lista[i] > maximo:  # Si encuentras un nuevo máximo
            maximo = lista[i]
            posiciones = [i]  # Reinicia la lista de posiciones
        elif lista[i] == maximo:  # Si es igual al máximo, agrega la posición
            posiciones.append(i)

    return posiciones

#funcion que calcula el factorial de un numero de manera recursiva
def calc_factorial(numero):
    if(numero == 0 or numero == 1):
        return 1
    else:
        return numero * calc_factorial(numero-1)

#Funcion que calcula la potencia de forma recurdiva
def calcular_potencia(base:int,exponente:int)->int:
        if base == 0:
                return 1
        else:
            return base * calcular_potencia(base,exponente - 1) 
pass

#Funcion que calcula el promedio de una lista
def calcular_promedio(lista:list):
    if len(lista) == 0:  # Verifica si la lista está vacía
        return 0 
    
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    
    promedio = float(total/len(lista))

    return promedio
pass