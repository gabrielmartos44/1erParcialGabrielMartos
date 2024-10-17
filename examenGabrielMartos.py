from my_funciones import *

#GABRIEL ANDRES MARTOS ZAMBRANO // DNI: 95748328 

cantidad_filas = 6
cantidad_columnas = 15

num = 50
menu = 1

caso1 = 0
contNumerosRango = 0



while menu == 1:
    caso2 = 0
    print("1- Generar lista de numeros aleatorios")
    print("2- Ordenar lista de numeros")
    print("3- Buscar numero por un rango en especifico")
    print("4- Buscar maximos y minimos")
    print("5- Generar matriz de caracteres alfanumericos")
    print("6- Salir")
    option = get_int("ingrese la opcion: ","error opcion equivocada",1,10)

    match option:
        case 1:
            listaAleatoria = generar_lista_aleatoria(num)
            caso1 = 1
            print("SE CREO LA LISTA ALEATORIA EXITOSAMENTE :)")
        case 2:
            if caso1 == 1:
                while caso2 == 0:
                    ordenamiento = get_string("ingese ordenamiento ascendente(ASC) o decendente(DESC): ","Error... ingreso un dato invalido ",3,4)
                    ordenamiento = ordenamiento.upper()
                    print(ordenamiento)
                    if ordenamiento == "ASC" or ordenamiento == "DESC":
                        listaOrdenada = ordenar_lista_selecion(listaAleatoria,ordenamiento)
                        print(listaOrdenada)
                        caso2 = 1
                    else:
                        print("Usted ingreso el valor erroneas opciones correctas son: (ASC) o (DESC) ")
            else:
                print("por favor cree la lista primero antes de ordenarla ")
        case 3:
            if caso1 == 1:
                rango1 = get_int("ingrese el rago mas pequeño que desee buscar: ","numero muy grande o pequeño ",0,100)
                rango2 = get_int("ingrese el rago mas grande que desee buscar: ","numero muy grande o pequeño ",0,100) 

                if rango1 < rango2:   
                    for i in range(len(listaAleatoria)):
                        if listaAleatoria[i] >= rango1 and listaAleatoria[i] <= rango2:
                            contNumerosRango += 1

                    print(f"CANTIDAD DE NÚMEROS EN EL RANGO [{rango1}-{rango2}]: {contNumerosRango} ") 
                else:
                    print("error ingreso el rangos equivocados... intentelo nuevamente")   
            else:
                print("por favor cree la lista primero antes de ordenarla")
            
        case 4:
            if caso1 == 1:
                maximo = calcular_maximo(listaAleatoria)
                minimo = calcular_minimo(listaAleatoria)
                print(f"el maximo de la lista es: {maximo} y el minimo es: {minimo}")
            else:
                print("por favor cree la lista primero antes de ordenarla")
        case 5:
            matrizAleatoria = inicializar_matriz_aleatoria(cantidad_filas,cantidad_columnas)

            opcion5 = get_int("Desea imprimir la matriz? si(1) no(2)","numero muy grande o pequeño ",1,2)
            if opcion5 == 1:
                imprimir_matriz(matrizAleatoria)
            else:
                print("La Matriz fue creada pero no mostrada")

        case 6:
            menu = 0
            print("USTED SALIO DEL SISTEMA")
