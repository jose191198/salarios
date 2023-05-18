
#Actividad Básica
#Obtener la diferencia entre el salario más alto y el más bajo dentro de los datos. Para esto, 
#se debe encontrar el valor máximo y restarle el valor mínimo de los datos (la respuesta a esta 
#operación se llama rango de los datos).

#Actividad Avanzada
#Obtener los estadísticos descriptivos de los salarios. (media, mediana, desviación estándar, etc.) 
#Mostrar los resultados de una manera sencilla de leer para el usuario.
import pandas as pd
import numpy as np
salarios={
    "Nombre":["Ringo","John","Paul","Geroge","Yoko"],
    "Edad":[45,34,42,38,47],
    "Salario":[12000,14000,13000,11000,10000],
    "Genero":["M","M","M","M","F"]
}
datos = pd.DataFrame(salarios)

maximo = max(salarios["Salario"])
minimo = min(salarios["Salario"])
rango = maximo - minimo
print(rango)

datos.describe()