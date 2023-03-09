# import os
# archivo = open('Clase02/Emisiones_CO2.csv', 'r')

# for linea in archivo:
#     print(linea)

# Check the versions of libraries
# Python version
# import sys
# print('Python: {}'.format(sys.version))
# # scipy
# import scipy
# print('scipy: {}'.format(scipy.__version__))
# # numpy
# import numpy
# print('numpy: {}'.format(numpy.__version__))
# # matplotlib
# import matplotlib
# print('matplotlib: {}'.format(matplotlib.__version__))
# # pandas
# import pandas
# print('pandas: {}'.format(pandas.__version__))
# # scikit-learn
# import sklearn
# print('sklearn: {}'.format(sklearn.__version__))

# Python program to explain os.getcwd() method
		
# importing os module
# import os
	
# Get the current working
# directory (CWD)
# cwd = os.getcwd() + '/Clase02'
# dir_list = os.listdir(cwd)
	
# Print the current working
# directory (CWD)
# print("Current working directory:", cwd)
# print("Files and directories in ", cwd, " :") 
  
# print the list 
# print(dir_list)
# dicc_emisiones = {  'cod_pais' : [],
#                     'nom_pais' : [],
#                     'region' : [],
#                     'anio' : [],
#                     'co2' : [],
#                     'co2_percapita' : []}
# archivo = open('Clase02/Emisiones_CO2.csv', 'r')

import os

dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}
arregloDicc = []
arregloDeLineas = []
nombre_archivo = "Clase02/Emisiones_CO2.csv"
with open(nombre_archivo, "r") as archivo:
    # Omitir el encabezado
   next(archivo, None)
   for linea in archivo:
      # Remover salto de linea
      linea = linea.rstrip()
      # Ahora convertimos la linea a arreglo con split
      lista = linea.split("|")
      # Usando un arreglo de lineas
      # Se adiciona el arreglo de la linea en el arreglo de todas las lineas
      # arregloDeLineas.append(lista)

      # Usando un arreglo de diccionario
      # Se adiciona el arreglo de linea en cada uno de las claves del diccionario

      dicc_emisiones = {'cod_pais' : lista[0],
                        'nom_pais' : lista[1],
                        'region' : lista[2],
                        'anio' : lista[3],
                        'co2' : lista[4],
                        'co2_percapita' : lista[5]}
      arregloDicc.append(dicc_emisiones)
   
   # for diccionario in arregloDicc:
   #    print(diccionario)
   
   para = 'Europa y Asia Central'
   anno = 2010
   totalCO2 = 0.0
   # Usando arreglo de lineas
   # for linea in arregloDeLineas:
   #    if (linea[2] == para):
   #       if (int(linea[3]) == anno):
   #          if(linea[4] != ''):
   #             # El valor de CO2 viene en la forma: xx.xxxx,xx
   #             # para que sea un string de un numero flotante se debe pasar a: xxxxx.xx
   #             # por lo que, se quita el punto y se cambia la ',' por el '.'
   #             totalCO2 += float(linea[4].replace('.','').replace(',','.'))

   # Usando arreglo de diccionario
   for dicc in arregloDicc:
      if (dicc['region'] == para):
         if (int(dicc['anio']) == anno):
            if(dicc['co2'] != ''):
               # El valor de CO2 viene en la forma: xx.xxxx,xx
               # para que sea un string de un numero flotante se debe pasar a: xxxxx.xx
               # por lo que, se quita el punto y se cambia la ',' por el '.'
               totalCO2 += float(dicc['co2'].replace('.','').replace(',','.'))
   print("El total de emisiones de CO2 para la region: " + para + " en el anno: " + str(anno) + " fue de: " + str(totalCO2))
   # ('El total de emisiones de CO2 para America Latina y Caribe en el anno 2010 fue: ', 1691634.8009999995)