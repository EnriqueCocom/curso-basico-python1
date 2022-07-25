#En este programa te enseño las condicionales de Python.
#Autor: Enrique Cocom Canul
#Fecha: 24-07/2022

#Declaramos una variable. son String.
calificacion = input("Introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion) #calificación se convierte a entero.

#Preguntamos si la calificación es menor a 700, muestra esto.
if calificacion < 700 :
    print("Veeeez, por no estudiar.") #Si la calificacion es menor a 700, muestra esto.

elif calificacion == 700 :
    print("PANZAZOOO !!!")

elif calificacion > 1000 :
    print("MIENTEEES !!!, No puedes sacar mas de mil.") #Si la calificacion es más a 1000, muestra esto.

else : #Si no se cumple el if anterior, pasa a esta linea.
    print("Felicidades, pasa por tu certificado.") #Se ejecuta si ninguno de los if se cumple.


#Verificador de mayoria de edad.
edad = input("Introduce tu edad: ")
edad = int(edad) #Convertir a entero

if edad >= 18 and edad <= 100 : #Si la edad es igual o mayor a 18 y la edad es menor o igual a 100.
    print("Bienvenid@ al Mamitas.")

elif edad > 100 : #Si la edad es mayor que 100
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar.")

elif edad < 0 : # Si la edad es menor que 0
    print("Ni que fueras viajer@ del tiempo.")

elif edad : #Si eres menor de edad.
    print("No puedes llevarte esos cigarros.")

#EN PYTHON NO HAY SWITCH CASE DE MOMENTO!.
#switch(edad)
#case 18:
#print()