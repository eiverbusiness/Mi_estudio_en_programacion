import os
os.system('cls')


lista_1 = [1, "Eiver", "fomo", "pickme"]
lista_2 = [1,"fomo", "parangaricutirimicuaro", "esternomascloideo"]


set_1 = set(lista_1)
set_2 = set(lista_2)

interseccion = set_1 & set_2

resultado = list(interseccion)

print(resultado)