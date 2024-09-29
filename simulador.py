import pandas as pd
import scipy.stats as stats

#INICIO PRIMER SIMULADOR ----------------------------------------------------------------------------------------------------------------------------------
x0 = int(input("Introduce el valor de la semilla: "))
a = int(input("Introduce el valor de la constante multiplicativa (a): "))
#c = int(input("Introduce el valor de la constante aditiva (c): "))
m = int(input("Introduce el valor del módulo de m: "))

while m <= 0 or m <= a or m <= x0:
    print(f"El valor de m debe ser mayor que 0, mayor que a ({a}), y mayor que X0 ({x0}). Inténtalo de nuevo.")
    m = int(input("Introduce un valor válido para el módulo de m: "))

c = 0 
xn = []
xn.append(x0)
rr = []
xnplusone = []
cont = 0


# Se genera un ciclo infinito para poder realizar la relacion de recurrencia y a su vez los numeros pseudoaleatorios

while True:
    dato1 = (a * xn[-1] + c) 
    dato2 = dato1 % m
    rr.append(dato1)
    xnplusone.append(dato2)

    if dato2 in xn:
        break #Si el dato de Xn+1 aparece entonces se corta el ciclo debido a que la semilla ya se estaria repitiendo
    xn.append(dato2) #Se le van agregando los valores de la semilla consecutivamente

    cont += 1 #Se cuentan cuantos valores totales se generaron

datos = {
    '  Xn': xn[:100],  
    '  Relación de recurrencia': [f"({i} / {m}) = {i//m}" for i in rr[:100]],
    '  Xn+1(Modulo)': xnplusone[:100], 
    '  # aleatorio': [f"   {i} / {m} = {round((i/m),3)}" for i in xnplusone[:100]] #Se realizan las operaciones para generar el numero pseudoaleatorio
    #Solamente se pide que se impriman los primeros 100 numeros de cada columna
} #Se genera una tabla a travez de pandas

tabla = pd.DataFrame(datos) #Se genera la tabla
pd.set_option('display.max_rows', None) #Se pide que no tenga limite de filas, para que se puedan imprimir las 100

#Se imprimen los valores generados
print("\n------------------------------------------------------------------------------------")
print("\nTenemos la fórmula Xn+1 = (aXn + c) mod m")
print("Donde X0 = Semilla")
print("a = Constante multiplicativa")
print("c = Constante aditiva")
print("m = módulo de m\n")
print(f"\nNumeros pseudoaleatorios del generador Xn+1 = ({a}Xn + {c}) mod {m} (solo los primeros 100):\n")
print(tabla)
print(f"\nSe generaron un total de {cont + 1} números pseudoaleatorios.")
print("\n------------------------------------------------------------------------------------")
#FIN PRIMER SIMULADOR ----------------------------------------------------------------------------------------------------------------------------------

#INICIO SEGUNDO SIMULADOR (UNIFORMIDAD)----------------------------------------------------------------------------------------------------------------------------------
nums = [round(x/m, 3) for x in xnplusone[:100]] #Generacion de un array que contenga solamente los primeros 100 numeros generados anteriormente
tamanioMuestra = 100 
numClass = 5  #Se inician con 5 clases 
frecEspInicial = tamanioMuestra / numClass  #La frecuencia esperada en un principio sera el tamaño de la muestra entre el numero de clases
chiObs = 0

frecEsp = [frecEspInicial] * numClass #Se multiplican los espacios en el array por el numero de clases, en este caso inicialmente sera = [5,5,5,5,5]
frecObs = [0] * numClass #Aqui sera = [0,0,0,0,0]

for num in nums:
    if 0.0 <= num < 0.2:
        frecObs[0] += 1 #Cuando el valor de nums se encuentre en el rango de 0 y 2 entonces el contador de la frecuencia se incrementa con 1
    elif 0.2 <= num < 0.4:
        frecObs[1] += 1
    elif 0.4 <= num < 0.6:
        frecObs[2] += 1
    elif 0.6 <= num < 0.8:
        frecObs[3] += 1
    elif 0.8 <= num < 1.0:
        frecObs[4] += 1

preTabla = pd.DataFrame({
    "[0.0, 0.199]": [frecEsp[0], frecObs[0]],
    "[0.2, 0.399]": [frecEsp[1], frecObs[1]],
    "[0.4, 0.599]": [frecEsp[2], frecObs[2]],
    "[0.6, 0.799]": [frecEsp[3], frecObs[3]],
    "[0.8, 0.999]": [frecEsp[4], frecObs[4]]
}, index=["Frec Esp", "Frec Obs"]) #Se acomodan los index para darle nombre a las filas

#Detallitos (no hacer caso)
"""
NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO :c
for i in range(len(frecObs) - 1, 0, -1):
    if frecObs[i] < frecEsp[i]:
        frecObs[i - 1] += frecObs[i]
        frecEsp[i - 1] += frecEsp[i]
        
        frecObs[i] = 0
        frecEsp[i] = 0
"""
#Se genera un ciclo para sumar el valor de la frecuencia esperada y observada a la anterior en dado caso de que la observada sea menor a 5, todo esto por el metodo violento
for i in range(len(frecObs) - 1, 0, -1): #Se comienzan a contar desde el ultimo hasta el primer valor de la frec
    if frecObs[i] < 5:
        frecObs[i - 1] += frecObs[i] #Se suma el valor actual con el anterior
        frecEsp[i - 1] += frecEsp[i]
        
        frecObs[i] = 0 #Se acomoda el valor actual en 0s
        frecEsp[i] = 0


chicuadrado = []
for i in range(numClass):
    if frecEsp[i] != 0: #Se busca que el la frecuencia esperada tenga un valor
        calculo = ((frecEsp[i] - frecObs[i]) ** 2) / frecEsp[i] #Si hay valor entonces se realiza la operacion de la chi cuadrada
    else:
        calculo = 0 #Si no hay valor entonces automaticamente vale un 0
    chicuadrado.append(calculo)
    chiObs += calculo #Se suma el valor de a chi cuadrada para al final haya una sumatoria de estas (valga la redundancia)

#chi cuadrada teorica
colum = 0.05
clasRestante = len([f for f in frecEsp if f > 0]) #Se cuentan valor por valor para verificar cuantas clases quedan  
chiTeo = stats.chi2.ppf(1 - colum, (clasRestante - 1)) #Se aplica la formula de la chicuadrada teorica mediante la libreria de SCIPY

#Se genera la tabla 
tablaClase = pd.DataFrame({
    "[0.0, 0.199]": [frecEsp[0], frecObs[0], chicuadrado[0]],
    "[0.2, 0.399]": [frecEsp[1], frecObs[1], chicuadrado[1]],
    "[0.4, 0.599]": [frecEsp[2], frecObs[2], chicuadrado[2]],
    "[0.6, 0.799]": [frecEsp[3], frecObs[3], chicuadrado[3]],
    "[0.8, 0.999]": [frecEsp[4], frecObs[4], chicuadrado[4]]
}, index=["Frec Esp", "Frec Obs", "Xi^2"])

#Se imprimen los resultados
print("\n------------------------------------------------------------------------------------")
print("\nSIMULADOR DE UNIFORMIDAD: ")
print("Los numeros son: ")
print("\n",nums)
print("\nTabla de Clases: ")
print(preTabla)
print("\nTabla de clases con la Xi ^ 2")
print(tablaClase)
print(f"\nX^2 Observada = {chiObs}")
print(f"\nX^2 Teorica {(colum, clasRestante)} = {chiTeo}")
#Si la chi Teorica es mayor a la observada entonces si es uniforme
if chiTeo > chiObs:
    print("\nLa muestra SI es uniforme")
else:
    print("\nLa muestra NO es uniforme")
print("\n------------------------------------------------------------------------------------")
#FIN SEGUNDO SIMULADOR (UNIFORMIDAD)----------------------------------------------------------------------------------------------------------------------------------

#INICIO TERCER SIMULADOR (ALEATORIDAD)----------------------------------------------------------------------------------------------------------------------------------
binarios = [1 if num >= 0.5 else 0 for num in nums] #Se convierten todos los numeros del array nums en binarios y se guardan en un nuevo array del mismo nombre
chiObs = 0 #Se reinicia el contador de chiObs para evitar sumas inecesarias 

valorUnos = []
valorCeros = []
cont1 = 0
cont0 = 0
#Se crean variables boleanas para poder ayudar con el conteo
unoAlaVista = False 
ceroAlaVista = False

#Se hace un ciclo for que checara los valores del array de binarios
for num in binarios:
    if num == 1: #Si el valor de binarios es uno
        if unoAlaVista: #Y si la bandera esta activada (True)
            valorUnos.append(cont0)   #Entonces el valor del contador se agregara a el array de valorUnos
        cont0 = 0  #Ahora si la bandera no esta activada (False) entonces el contador vale 0
        unoAlaVista = True  #Se activa la bandera
    elif unoAlaVista:  #Si la bandera esta activada 
        cont0 += 1 #Entonces el contador se suma en 1, para ir contando los 0s entre los 1s
    #Se repite el mismo proceso para calcular los 1s entre los 0s
    if num == 0:
        if ceroAlaVista:
            valorCeros.append(cont1)  
        cont1 = 0  
        ceroAlaVista = True  
    elif ceroAlaVista:  
        cont1 += 1

#Una vez teniendo los dos arrays llenos, entonces se compara cual es el valor mas grande para asi definir el valor maximo de la clase
mayorNum = max(max(valorUnos), max(valorCeros))
clases = [i for i in range(mayorNum + 1)] #Se genera un array con los valores de la clase de manera descendente, es decir si el mayorNum es 5, entonces clases sera = [0,1,2,3,4,5]

unos = [0] * (mayorNum + 1)#Multiplicamos los ceros por el numero de mayorNum + 1 (para igualar al valor maximo de la clase)
ceros = [0] * (mayorNum + 1)

#Se crea un ciclo para contabilizar los valores de unos
for i in valorUnos:
    unos[i] += 1 #Si el valorUnos = 3, entonces el valor de 3 en Unos se incrementa en 1
for i in valorCeros:
    ceros[i] += 1

binFrecObs = []
for i in range(len(clases)):
    binFrecObs.append(unos[i]+ceros[i]) #La frecuencia observada se genera sumando los valores de los unos y ceros por cada clase

binFrecEsp = []
for valorC in clases:
    res = (tamanioMuestra - valorC + 3) / (2 ** (valorC + 1)) #Se aplica la formula para sacar la frecuencia esperada
    binFrecEsp.append(res)

#Se repite el mismo proceso para calcular el valor de chi cuadrado
chicuadrado = []
for i in range((mayorNum+1)):
    if binFrecEsp[i] != 0: 
        calculo = ((binFrecEsp[i] - binFrecObs[i]) ** 2) / binFrecEsp[i]
    else:
        calculo = 0
    chicuadrado.append(calculo)
    chiObs += calculo

#Se imprime una pretabla el cual aun no ha sumado si la frecuencia observada es menor a 5
pretablaSim3 = pd.DataFrame({
    "Unos": unos,
    "Ceros": ceros,
    "Frec Obs": binFrecObs,
    "Frec Esp": binFrecEsp,
    "X ^ 2": chicuadrado
}, index=clases)

#Al igual que el simulador de uniformidad, se verifica que la frec Observada sea mayor a 5, en dado que no, entonces su valor se suma al anterior por el metodo violento
for i in range(len(binFrecObs) - 1, 0, -1):
    if binFrecObs[i] < 5:
        binFrecObs[i - 1] += binFrecObs[i]
        binFrecEsp[i - 1] += binFrecEsp[i]
        chicuadrado[i - 1] += chicuadrado[i]

        binFrecObs[i] = 0
        binFrecEsp[i] = 0
        chicuadrado[i] = 0

#Se imrpime la tabla, ahora con las frecuencias observadas sumadas (si es que se dio el caso)
tablaSim3 = pd.DataFrame({
    "Unos": unos,
    "Ceros": ceros,
    "Frec Obs": binFrecObs,
    "Frec Esp": binFrecEsp,
    "X ^ 2": chicuadrado
}, index=clases)

#chi cuadrada teorica
colum = 0.05
clasRestante = len([f for f in binFrecEsp if f > 0])  
chiTeo = stats.chi2.ppf(1 - colum, (clasRestante - 1)) #De igual manera se aplica la formula del chi Teorico mediante la libreria de Scipy

#Y fuaaaaaaaaaaa, se imprime todo 
print("\n------------------------------------------------------------------------------------")
print("\nSIMULADOR DE ALEATORIDAD: ")
print("\nLos numeros binarios son (siempre y cuando num >= 0.5 = 0 / num <= 0.5 = 1): ")
print("\n", binarios)
print("\nLa tabla: ")
print(pretablaSim3)
print("\nLa tabla con las cuando la frecuencia observada minima a 5: ")
print(tablaSim3)
print(f"\nX^2 Observada = {chiObs}")
print(f"\nX^2 Teorica {(colum, clasRestante)} = {chiTeo}")
if chiTeo > chiObs:
    print("\nLa muestra SI es aleatoria")
else:
    print("\nLa muestra NO es aleatoria")
print("\n------------------------------------------------------------------------------------")
#FIN TERCER SIMULADOR (ALEATORIDAD)----------------------------------------------------------------------------------------------------------------------------------