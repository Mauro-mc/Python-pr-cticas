# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:19:17 2021

@author: Usuario
"""

#while

contar =input("ingrese el # de veces a contar: ")
contar= int(contar)
contador= 1

while contador<= contar:
    print (contador)
    contador+= 1
    
 #OTRO METODO WHILE   
contar =input("ingrese el # de veces a contar: ")
contar= int(contar)
contador= 1

while True:
    print (contador)
    contador+= 1
    if contador > contar:
        break
    
# encontrar el error
while True:
    x=input("enter a number to count to: ")
 
    if x == "q" or x == "quit":
        break
    
x= int (x)(#alinearlo, identacion mal)
y= 1 (#alinearlo, identacion mal)
while True: (#alinearlo, identacion mal)
    print (y)(#alinearlo, identacion mal)
    y=y+1(#alinearlo, identacion mal)
    if y > x:(#alinearlo, identacion mal)
        break(#alinearlo, identacion mal)

#solucion correcta
while True:
    x=input("enter a number to count to: ")
 
    if x == "q" or x == "quit":
        break
    x= int (x)
    y= 1 
    while True: 
        print (y)
        y=y+1
        if y > x:
            break
 # funciones
def saludos (nombre1,nombre2):
    print("hola",nombre1)
    print("hola",nombre2)
    
saludos("Juan","Carlos")
saludos("Ana","Isabel")

#ejercicio

def direccion (provincia,ciudad,barrio): #en este orden se imprime
    print("su direccion es: ")
    print("su provincia es: ", provincia)
    print ("la ciudad de domicilio es: ", ciudad)
    print ("la direccion de referencia es:", barrio)
    
pr=input("ingrese la provincia: ")
br=input("ingrese el barrio: ")
ci=input("ingrese la ciudad: ")

direccion(pr,ci,br)
direccion(barrio=br,ciudad=ci,provincia=pr)

#ejercicio
def resta (a,b):
    print("la resta entre: ",a,"-",b,"es:",a-b)
resta(5,2)
resta(2,5)
resta(a=2,b=5)
resta(b=5,a=2)
resta(5,b=2)


