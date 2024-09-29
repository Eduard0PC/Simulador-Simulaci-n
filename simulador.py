import pandas as pd
import scipy.stats as stats

#INICIO PRIMER SIMULADOR ----------------------------------------------------------------------------------------------------------------------------------
x0 = int(input("Introduce el valor de la semilla: "))
a = int(input("Introduce el valor de la constante multiplicativa (a): "))
#c = int(input("Introduce el valor de la constante aditiva (c): "))
m = int(input("Introduce el valor del módulo de m: "))

c = 0
xn = []
xn.append(x0)
rr = []
xnplusone = []
cont = 0

while True:
    dato1 = (a * xn[-1] + c)
    dato2 = dato1 % m
    rr.append(dato1)
    xnplusone.append(dato2)

    if dato2 in xn:
        break
    xn.append(dato2)

    cont += 1

datos = {
    '  Xn': xn[:100],  
    '  Relación de recurrencia': [f"({i} / {m}) = {i//m}" for i in rr[:100]],
    '  Xn+1(Modulo)': xnplusone[:100],
    '  # aleatorio': [f"   {i} / {m} = {round((i/m),3)}" for i in xnplusone[:100]]
}

tabla = pd.DataFrame(datos)
pd.set_option('display.max_rows', None)

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
nums = [round(x/m, 3) for x in xnplusone[:100]]
tamanioMuestra = 100
numClass = 5
frecEspInicial = tamanioMuestra / numClass  
chiObs = 0

frecEsp = [frecEspInicial] * numClass
frecObs = [0] * numClass

for num in nums:
    if 0.0 <= num < 0.2:
        frecObs[0] += 1
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
}, index=["Frec Esp", "Frec Obs"])

"""
NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO :c
for i in range(len(frecObs) - 1, 0, -1):
    if frecObs[i] < frecEsp[i]:
        frecObs[i - 1] += frecObs[i]
        frecEsp[i - 1] += frecEsp[i]
        
        frecObs[i] = 0
        frecEsp[i] = 0
"""
for i in range(len(frecObs) - 1, 0, -1):
    if frecObs[i] < 5:
        frecObs[i - 1] += frecObs[i]
        frecEsp[i - 1] += frecEsp[i]
        
        frecObs[i] = 0
        frecEsp[i] = 0


chicuadrado = []
for i in range(numClass):
    if frecEsp[i] != 0: 
        calculo = ((frecEsp[i] - frecObs[i]) ** 2) / frecEsp[i]
    else:
        calculo = 0
    chicuadrado.append(calculo)
    chiObs += calculo

#chi cuadrada teorica
colum = 0.05
clasRestante = len([f for f in frecEsp if f > 0])  
chiTeo = stats.chi2.ppf(1 - colum, (clasRestante - 1))


tablaClase = pd.DataFrame({
    "[0.0, 0.199]": [frecEsp[0], frecObs[0], chicuadrado[0]],
    "[0.2, 0.399]": [frecEsp[1], frecObs[1], chicuadrado[1]],
    "[0.4, 0.599]": [frecEsp[2], frecObs[2], chicuadrado[2]],
    "[0.6, 0.799]": [frecEsp[3], frecObs[3], chicuadrado[3]],
    "[0.8, 0.999]": [frecEsp[4], frecObs[4], chicuadrado[4]]
}, index=["Frec Esp", "Frec Obs", "Xi^2"])

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
if chiTeo > chiObs:
    print("\nLa muestra SI es uniforme")
else:
    print("\nLa muestra NO es uniforme")
print("\n------------------------------------------------------------------------------------")
#FIN SEGUNDO SIMULADOR (UNIFORMIDAD)----------------------------------------------------------------------------------------------------------------------------------

#INICIO TERCER SIMULADOR (ALEATORIDAD)----------------------------------------------------------------------------------------------------------------------------------
binarios = [1 if num >= 0.5 else 0 for num in nums]
chiObs = 0

valorUnos = []
valorCeros = []
cont1 = 0
cont0 = 0
unoAlaVista = False
ceroAlaVista = False

for num in binarios:
    if num == 1:
        if unoAlaVista:
            valorUnos.append(cont0)  
        cont0 = 0  
        unoAlaVista = True  
    elif unoAlaVista:  
        cont0 += 1
    if num == 0:
        if ceroAlaVista:
            valorCeros.append(cont1)  
        cont1 = 0  
        ceroAlaVista = True  
    elif ceroAlaVista:  
        cont1 += 1

mayorNum = max(max(valorUnos), max(valorCeros))
clases = [i for i in range(mayorNum + 1)]

unos = [0] * (mayorNum + 1)#Multiplicamos los ceros por el numero de clases
ceros = [0] * (mayorNum + 1)

for i in valorUnos:
    unos[i] += 1
for i in valorCeros:
    ceros[i] += 1

binFrecObs = []
for i in range(len(clases)):
    binFrecObs.append(unos[i]+ceros[i])

binFrecEsp = []
for valorC in clases:
    res = (tamanioMuestra - valorC + 3) / (2 ** (valorC + 1))
    binFrecEsp.append(res)

chicuadrado = []
for i in range((mayorNum+1)):
    if binFrecEsp[i] != 0: 
        calculo = ((binFrecEsp[i] - binFrecObs[i]) ** 2) / binFrecEsp[i]
    else:
        calculo = 0
    chicuadrado.append(calculo)
    chiObs += calculo

pretablaSim3 = pd.DataFrame({
    "Unos": unos,
    "Ceros": ceros,
    "Frec Obs": binFrecObs,
    "Frec Esp": binFrecEsp,
    "X ^ 2": chicuadrado
}, index=clases)

for i in range(len(binFrecObs) - 1, 0, -1):
    if binFrecObs[i] < 5:
        binFrecObs[i - 1] += binFrecObs[i]
        binFrecEsp[i - 1] += binFrecEsp[i]
        chicuadrado[i - 1] += chicuadrado[i]

        binFrecObs[i] = 0
        binFrecEsp[i] = 0
        chicuadrado[i] = 0

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
chiTeo = stats.chi2.ppf(1 - colum, (clasRestante - 1))

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