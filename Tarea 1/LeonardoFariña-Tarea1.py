#Creado por Leonardo Fariña - 2020045272
#Tarea 1 - Analisis De Algoritmos
#Fecha de creación 02/03/2021 11:12am
#Última modificación 02/03/2021 11:12am
#Versión 3.9.1

import random
import time
import sys

#Para crear graficas
try:
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
except:
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n!! Necesita instalar matplotlib, puede hacerlo con el siguiente comando: \'pip install matplotlib\'!!\n")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    sys.exit()
#--- Variables globales para promedios
global prom_ms
prom_ms = []
global prom_bs
prom_bs = []
global prom_is
prom_is = []
#------------------- Merge Sort

def merge_sort(lista): 
    """
    Entrada: lista(una lista desordenada)
    Desarrollo: Vamos a ordenar lista, nos fijamos que su tamaño sea menor a 2(que significa que esta ordenada) si no dividimos
                nuestra lista en 2 (right y left que aplicamos recursividad) y la pasamos por la función merge(der y izq).
    Salida: lista( una lista ya ordenada)
    """
    if len(lista) < 2:
          return lista
    else:
        medio = len(lista) // 2
        der = merge_sort(lista[:medio])
        izq = merge_sort(lista[medio:])
        return merge(der, izq)

    
def merge(lista0, lista1):
    """
    Entrada: lista0(lista desordenada),lista1(lista desordenada)
    Desarrollo: Intercalamos los elementos ordenadamente en resultado 
    Salida: resultado(la lista con los elementos de lista0 y lista1 ordenados)
    """
    inc, inc1 = 0, 0 
    resultado = []    
   # Intercalamos los elementos de las listas
    while(inc < len(lista0) and inc1 < len(lista1)):
        if (lista0[inc] < lista1[inc1]):
            resultado.append(lista0[inc])
            inc += 1
        else:
            resultado.append(lista1[inc1])
            inc1 += 1 
    resultado += lista0[inc:]
    resultado += lista1[inc1:]    
    return resultado

#------------------- Bubble Sort

def bubble_sort(lista):
    """
    Entrada: lista(lista desordenada)
    Desarrollo: Intercalamos los elementos ordenadamente en lista(los vamos
                cambiando de lugar)
    Salida: lista(la lista con los elementos ordenados)
    """
    elem = len(lista)
    for inc0 in range(elem):
        for inc1 in range(0, elem-1):
            if lista[inc1] > lista[inc1+1]:
                lista[inc1], lista[inc1+1] = lista[inc1+1], lista[inc1]
    return lista

#------------------- Insertion Sort

def insertion_sort(lista): 
    """
    Entrada: lista(lista desordenada)
    Desarrollo: Intercalamos los elementos ordenadamente en lista(los vamos
                cambiando de lugar)
    Salida: lista(la lista con los elementos ordenados)
    """
    for inc0 in range(1, len(lista)):   
        llave = lista[inc0] 
        inc1 = inc0-1
        while inc1 >=0 and llave < lista[inc1] : 
                lista[inc1+1] = lista[inc1] 
                inc1 -= 1
        lista[inc1+1] = llave
    return lista         

#------------------- Corrida de listas

def corrida(lista):
    """
    Entrada: lista(lista desordenada de enteros)
    Desarrollo: Llamaremos los algortimos de ordenamiento y tomaremos el tiempo que tardan en ejecutarse.Guardaremos el timpo
                que tardan con cada corrida en listas para luego mostrarlas en la gráfica.
    Salida: NULL
    """
    lista1 = lista.copy()
    lista2 = lista.copy()
    lista3 = lista.copy()
    print("             Probamos con ", len(lista)," elementos a ordenar")
    #Camptamos el tiempo que tarda merge sort
    inicio_de_tiempo1 = time.time()    
    prueba0 = merge_sort(lista1)
    tiempo_final1 = time.time() 
    tiempo_transcurrido1 = tiempo_final1 - inicio_de_tiempo1    

    #Camptamos el tiempo que bubble sort
    inicio_de_tiempo2 = time.time()
    prueba1 = bubble_sort(lista2)
    tiempo_final2 = time.time() 
    tiempo_transcurrido2 = tiempo_final2 - inicio_de_tiempo2

    #Camptamos el tiempo que tarda insertion sort
    inicio_de_tiempo3 = time.time()
    prueba2 = insertion_sort(lista3)
    tiempo_final3 = time.time() 
    tiempo_transcurrido3 = tiempo_final3 - inicio_de_tiempo3

    print("     Merge Sort     ","-     Bubble Sort     ","-    Insertion Sort")
    print(str(tiempo_transcurrido1).zfill(20),"-",str(tiempo_transcurrido2).zfill(20),"-",str(tiempo_transcurrido3).zfill(20))

    global prom_ms
    global prom_bs
    global prom_is
    prom_ms.append(round(tiempo_transcurrido1,3))
    prom_bs.append(round(tiempo_transcurrido2,3))
    prom_is.append(round(tiempo_transcurrido3,3))
    
    
#---------------------------------------------------------    Main

print("\nLeonardo Fariña - 2020045272 - Tarea 1 - Analisis De Algoritmos")
print("\n 1-) ")


#-------Creamos nuestras listas con los numeros desordenados
elemento = 0
list10 = []
list100 = []
list1000 = []
list10000 = []
list20000 = []
list30000 = []
while (elemento < 30000):
    aux = ((elemento+1) * random.randint(1, 20))//random.randint(1, 9)
    if elemento < 10:
        list10.append(aux)
    if elemento < 100:
        list100.append(aux)
    if elemento < 1000:
        list1000.append(aux)
    if elemento < 10000:
        list10000.append(aux)
    if elemento < 20000:
        list20000.append(aux)
    if elemento < 30000:
        list30000.append(aux)
    elemento += 1


#---- Corremos las listas en los algoritmos
corrida(list10)
corrida(list100)
corrida(list1000)
corrida(list10000)
corrida(list20000)
corrida(list30000)



#---- Creamos la grafica a mostrar
elementos = ['10', '100', '1000', '10000', '20000','30000']
merg = prom_ms
bubl = prom_bs
inse = prom_is
x = np.arange(len(elementos))
width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, merg, width, label='Merge Sort')
rects2 = ax.bar(x + width/2, bubl, width, label='Bubble Sort')
rects3 = ax.bar(x + (width/2)+0.25, inse, width, label='Insertion Sort')
ax.set_ylabel('Tiempo en Segundos')
ax.set_title('Tiempo de ejecución de los Algoritmos')
ax.set_xticks(x)
ax.set_xticklabels(elementos)
ax.legend()
def autolabel(rects):
    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()
plt.savefig('tiempo_de_ejecucion_Alg.png')
plt.show()

#--------- Respondemos a las preguntas 2 y 3
print("\n 2-) ")
print("Concluimos que: \n  Merge Sort tienen orden de crecimiento O(n) el más rapido \n  Bubble Sort tienen orden de crecimiento O(n^3) el más lento \n  Insertion Sort tienen orden de crecimiento O(n^2)")

print("\n 3-) ")
print("\nMerge Sort de los tres es el que menos tiempo tarda en procesar las entradas y su tiempo aumenta linealmente. \nCreo que esto es por que vamos trabajando la lista como por partes y ordenandola de a pedazos.")
print("\nBubble Sort de los tres es el más lento ya que el tiempo que tarda aumenta cubicamente, con entradas grandes tarda mucho en procesarlas.\n Creo que esto puede ser por que recorre la lista de elementos 1 a 1 para compararlos.")
print("\nInsertion Sort es más rapido que el Bubble Sort pero mucho más lento que el Merge Sort, diria que el tiempo que tarda aumenta cuadraticamente.\n Creo que se debe a que tambien va recorriendo toda la lista 1 a 1 pero va ordenando la lista comparando solo con los \n elementos adyacentes.")









