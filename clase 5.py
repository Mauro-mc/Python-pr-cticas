# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:30:14 2021

@author: Usuario
"""

def uno(a,b):
    return (a*b)
print (uno(5,2))
w=uno(5,2)
suma=w+5

print(suma)

#practica 5 funciones

def multiply(a,b):
    return(a*b)
print(multiply(5,4))
x=multiply(5, 4)
nuevax=x*100
print(nuevax)

def resta(a,b):
    return(a-b)
print(resta(10,8))
y=resta(10,8)
nuevay=y*100
print(nuevay)

def suma(a,b):
    return(a+b)
print(suma(5,12))
z=suma(5,12)
nuevaz=z*100
print(nuevaz)

def division(a,b):
    return(a/b)
print(division(40,8))
u=division(40,8)
nuevau=u*100
print(nuevau)

def exponencial(a,b):
    return(a**b)
print(exponencial(5,9))
o=exponencial(5,9)
nuevao=o*100
print(nuevao)

#def en LISTA
def saludos(lista):
    for i in lista:
        print("Hola", i)

saludos(["Juan"])
saludos(["luis"",carlos"])

#ejercicio

def crealista(n):
    lista=[]
    for i in range(n):
        lista.append(i)
    return lista
print(crealista(5))
resultado=crealista(20)


