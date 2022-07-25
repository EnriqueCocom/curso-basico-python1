#En este programa te enseño las pilas de Python.
#Autor: Enrique Cocom Canul
#Fecha: 24-07/2022

#Pila en Python
#EL ULTIMO ELEMENTO QUE ENTRA, ES EL PRIMER ELEMENTO QUE SALE.

stack = [1, 2, 3, 4, 5] #Crear una pila.
stack.append(6) #Agregar un elemento a la pila.
stack.append(7)

print(stack)

stack.pop()
print(stack) #Sacar el último elemento de la pila.

stack.pop()
print(stack)

stack.pop()
print(stack)