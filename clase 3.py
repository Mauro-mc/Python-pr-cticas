# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:35:57 2021

@author: Usuario
"""

nombre=input("Ingrese su nombre: ")
print("Hola", nombre)

datos =1
nativa=100

if datos== nativa:
    print("Las variables son iguales")
else:
    print("las variables son diferentes")
print ("fin")

########### IF, ELIF, ELSE###################

acl=int(input("Ingrese el valor de ACL: "))
if acl>=1 and acl<=99:
    print("la ACL es estandar")
elif acl>=100 and acl<= 199:
    print ("la ACL es extendida")
else:
    print("el # ingresado no es de ACL")
   
#####FOR######

lista=["R1","R2","R3","R4"]
for item in lista:
    print(item)
    
lista=["R1","R2","R3","R4", "S1", "S2"]
for item in lista:
    if "R" in item:
        print (item)
        
#Llenar una lista vacia con append
lista1=[]
lista2=[]
lista=["R1","R2","R3","R4", "S1", "S2"]
for item in lista:
    if "S" in item:
    lista1.append(item)
    
for item in lista:
    if "R" in lista:
    lista2.append(item)
    


