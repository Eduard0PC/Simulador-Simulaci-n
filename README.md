# Simulador-Simulacion
Simulador de la materia simulación, el cual incluye los simuladores de:
- Generador de numeros PseudoAleatorios
- Simulador de Uniformidad
<<<<<<< HEAD
- Simuador de Aleatoridad

**Ejemplos:**

### SIMULADOR DE UNIFORMIDAD 
Pruebe la uniformidad de la siguiente muestra con 5 clases y α = 5%

|       |       |       |       |       |       |
|-------|-------|-------|-------|-------|-------|
| 0.715 | 0.965 | 0.318 | 0.495 | 0.107 | 0.661 |
| 0.253 | 0.539 | 0.161 | 0.134 | 0.161 | 0.868 |
| 0.837 | 0.580 | 0.186 | 0.158 | 0.105 | 0.742 |
| 0.844 | 0.098 | 0.288 | 0.285 | 0.209 | 0.264 |
| 0.609 | 0.460 | 0.600 | 0.739 | 0.466 | 0.484 |

*(En el contexto del simulador la muestra serian los numeros pseudoaleatorios generados)*

La frecuencia esperada del ejercicio se obtendria con la siguiente formula:

$$ 
\text{Frecuencia esperada} = \frac{\text{Tamaño\ de\ la\ muestra}}{\text{número\ de\ clases}} 
$$

Por lo que en este caso nos quedaria:

$$
\text{Frecuencia esperada} = \frac{30}{5} = 6
$$

Ahora como nos pide que sea en 5 clases clasificamos los datos dentro de las siguientes clases:

`[0.0, 0.199], [0.2, 0.399], [0.4, 0.599], [0.6, 0.799], [0.8, 0.999]`

por lo que distribuimos cada uno de los valores dentro de esos rangos para asi obtener la frecuencia observada (que en otras palabras se traduce a contar los numeros) y nos queda de la siguiente manera:

|       |0.0, 0.199|0.2, 0.399|0.4, 0.599|0.6, 0.799|0.8, 0.999|
|-------|-------|-------|-------|-------|-------|
|Frec Esp|6|6|6|6|6|
|Frec Obs|8|6|6|6|4|

**Regla: La frecuencia observada no debe ser menor a 5**

Y como se puede apreciar la frecuencia observada del rango 0.8, 0.999 es 4, por lo que se hace es sumar lo valores de la frecuencia esperada y observada a la columna anterior, quedandonos de la siguiente manera:

|       |0.0, 0.199|0.2, 0.399|0.4, 0.599|0.6, 0.799|0.8, 0.999|
|-------|-------|-------|-------|-------|-------|
|Frec Esp|6|6|6|12|0|
|Frec Obs|8|6|6|10|0|

Una vez teniendo todo esto hay que sacar la $Xi^2$ por cada columna, la cual tiene la siguiente formula:

$$
\chi^2 = \frac{(\text{Frecuencia esperada} - \text{Frecuencia observada})^2}{\text{Frecuencia esperada}}
$$

Asi que la tabla nos queda de la siguiente manera:

|       | 0.0, 0.199 | 0.2, 0.399 | 0.4, 0.599 | 0.6, 0.799 | 0.8, 0.999 |
|-------|------------|------------|------------|------------|------------|
| Frec Esp |6|6|6|12|0|
| Frec Obs |8|6|6|10|0|
| Xi<sup>2</sup>|2/3|0|0|1/3|0|

Teniendo lista la tabla entonces se procede a calcular la $ Xi^2$ observada, la cual tiene la siguiente formula:

$$
\chi^2 Observada= \sum \chi^2
$$

Quedandonos:

$$
\chi^2 Observada= \frac{3}{3} = 1.0
$$

Y entonces se pasa a comparar con la $\chi^2$ Teórica la cual tiene la segunda formula:

$$
\chi^2 Teórica= (0.05, \text{Clases restantes}-1)
$$

Y a clases restantes se refiere a las columnas en donde haya informacion, por lo que en nuestro caso nos queda:

$$
\chi^2 Teórica= (0.05, 4-1)
$$

**El 0.05 es el 5% que nos indica el ejercicio**

Y una vez teniendo eso, se procede a buscar los valores en una [tabla de distribución de $\chi ^2 $](Tablas.pdf) (En el simulador se usa la libreria de **Scipy** para la consulta de los valores de las tablas), 

Donde:

$$
\chi^2 Teórica= (\text{Columna, Fila})
$$

Y una vez encontrado el valor en la tabla nos dice que este es:

$$
\chi^2 Teórica= 7.81
$$

Teniendo toda esta informacion, si la frecuencia observada es mayor que la teórica, entonces la muestra **NO** es uniforme, pero si la observada es menor a la teórica, entonces **SI** es uniforme. 

Volviendo con el ejercicio se puede decir que:

#### LA MUESTRA SI ES UNIFORME

*(Ya que el 1.0 de la frecuencia observada es menor que el 7.81 de la frecuencia teórica)*
***
=======
- Simulador de Aleatoridad
- Simulador de Independencia (Proximamente) 
>>>>>>> 3dd8d50fc1d56bb473fded2070366d33b4b186a9
