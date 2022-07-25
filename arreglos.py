#En este programa te enseño los arreglos de Python.
#Autor: Enrique Cocom Canul
#Fecha: 24-07/2022

#Arreglos pueden ser listas de valores, enteros de todo tipo.
lista =[1, 2, 3, 4, 5]

lista.append(0) #Poner un elemento al final de la lista.
print(lista)

lista.extend(lista) #Podemos agregar una lista a otra lista.
print(lista)

lista = lista[::-1] #Podemos invertir una lista.
print(lista)

lista.reverse() #Podemos invertir una lista.
print(lista)

lista.insert(0, 10) #Podemos insertar un elemento en una posición específica(0, 10).
lista.insert(5, 11) #En la posición 5, inserta el número 11.
print(lista)

lista.remove(0) #Eliminar un elemento de la lista, en este caso borra el primer cero.
#lista.remove(0)
#lista.remove(0) #Si intentamos eliminar un elemento que no existe, nos arroja un error.
print(lista)

#lista.pop() Quitar el elemento de la lista.
print(lista.pop(1)) #Eliminar el último elemento de la lista y lo devuelve.
print(lista)

print(lista.count(3)) #Cuenta la cantidad de veces que aparece un elemento en la lista.

print(lista.index(10)) #Devuelve la posición del elemento en la lista.
print(lista.index(11))

lista.sort() #Ordena la lista.
print(lista)

#Otra forma de revertir la lista.
lista.sort(reverse = True) #Invertimos la lista.
print(lista)

lista2 = lista.copy() #Copiar una lista, es una copia superficial.
print(lista2)

lista.clear() #Limpiar la lista.
print(lista)

lista2 = [] #Crear una lista vacía.
print(lista2)