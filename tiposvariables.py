#En este programa te enseño los tipos de variables en Python.
#Autor: Enrique Cocom Canul
#Fecha: 24-07/2022

#String o str -- Son cadenas de textos, palabras, frases, hola, jose,innovacción, wizards.
nombre = "Enrique 😎🧙‍♂️❤️"
print (nombre) #Imprime el nombre.

#Enteros (int) - Son números sin punto decimal.
edad = 23 #Cuando se usara las operaciones matematicas: suma, resta, multiplicación, dividición.
edads = "23"  #Cuando no haremos operaciones matematicas str.

#Ejemplo de diferencia
print(edad + edad) #Se suman los dos.
print(edads + edads) #Apila la palabra.


#Flotante (float) - Números con punto decimal.
pi = 3.1416  #Las veces que el radio del circulo cabe en su perimetro.
print(pi)

edad = float(edad)  #Casteo - Transformación de un tipo de variable a otro.
#edad se convierte a flotante - fuertemente tipado.
print(edad)

# Usa type para saber de que tipo es la variable es.
print(type(nombre), type(edad))

# Bool - Booleano - SI O NO, True - False.
legustas = False
legustas = True

print(legustas)

#Como crear un ejecutable .exe, se usa una libreria llamada pytoexe.