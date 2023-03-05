def NumeroBinario(numero):
    '''
    Esta funcion recibe como parametro un numero entero mayor o igual a cero y lo devuelve en su 
    representacion binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parametro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if(type(numero) != int):
        print("Debe ingresar un numero entero")
        return None
    elif(numero < 0):
        print("Debe ingresar un numero mayor que cero")
        return None
    elif(numero == 0):
        return 0
    else:
        arregloValorBinario = []
        while(numero > 0):
            arregloValorBinario.insert(0,numero % 2)
            numero = numero // 2
    return arregloValorBinario

def binarioToDecimal(numero):
    if(type(numero) != int):
        print("Debe ingresar un numero entero")
        return None
    elif(numero < 0):
        print("Debe ingresar un numero mayor que cero")
        return None
    elif(numero == 0):
        return 0
    else:
        # Se transforma el numero en un arreglo de caracteres
        arregloNumStr = tuple(str(numero))
        arregloNum = []
        # Se transforma el arreglo de caracteres en arreglo de numeros
        for elemento in arregloNumStr:
            if(int(elemento) > 1 or int(elemento) < 0):
                print("No es un numero en formato binario")
                return None
            arregloNum.append(int(elemento))
        numeroDecimal = 0
        # for i, e in enumerate(arregloNum):
        i =  0
        fin = len(arregloNum) - 1
        while(i < len(arregloNum)):
            # print('i: ', i, '->', 'e: ', arregloNum[fin])
            numeroDecimal = numeroDecimal + (arregloNum[fin] * (2 ** i))
            i += 1
            fin -= 1
        # print(arregloNum)
        return numeroDecimal

# 2) Convertir fracciones decimales a binario las fracciones 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9. 
# Luego analizar los resultados y observar que particularidad se encuentra en los mismos. 
# Se puede usar Python o una calculadora, lo importante es ver si hay algo que podemos notar...
# Salida esperada:
# * Fraccion 1 / 2 :  0.5  y En binario:  0.1
# * Fraccion 1 / 3 :  0.3333333333333333  y En binario:  0.010101010101010101010101
# * Fraccion 1 / 4 :  0.25  y En binario:  0.01
# * Fraccion 1 / 5 :  0.2  y En binario:  0.001100110011001100110011
# * Fraccion 1 / 6 :  0.16666666666666666  y En binario:  0.001010101010101010101010
# * Fraccion 1 / 7 :  0.14285714285714285  y En binario:  0.001001001001001001001001
# * Fraccion 1 / 8 :  0.125  y En binario:  0.001
# * Fraccion 1 / 9 :  0.1111111111111111  y En binario:  0.000111000111000111000111
def fracionToBinario(numero):

    print(numero)
    if(type(numero) != float):
        print("Debe ingresar un numero con decimales")
        return None
    elif(numero < 0):
        print("Debe ingresar un numero mayor que cero")
        return None
    elif(numero == 0):
        return 0
    else:
        binario = "0."
        continuar = True
        while(continuar):
            # temporal = numero * 2
            numero = numero * 2
            if(numero < 1):
                binario = binario + str(0)
            elif(numero > 1):
                binario = binario + str(1)
                numero = numero - 1
            else:
                binario = binario + str(1)
                continuar = False
    print(binario)
    return None    

# print(format(44,"b"))
# print(44, "en binario es:", NumeroBinario(44))
# print(format(101100,"d"))
# print(101100, "en decimal es: ", binarioToDecimal(101100))
# float num

fracionToBinario(1.0 / 3.0)