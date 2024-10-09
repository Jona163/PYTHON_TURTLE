# Autor: Jonathan Hernández
# Fecha: 9/10/24
# Descripción: Código para usar turtle.
# GitHub: https://github.com/Jona163

from turtle import *
begin_poly()
pencolor('red')
dot(750)
pencolor('black')
dot(500)
pencolor('red')
dot(475)
#Funcion curva01
def curve01(a,d):
 for i in range(d):
  right(a)
  forward(1)
def curve02(a,d):
 for i in range(d):
  left(a)
  forward(1)
pencolor('black')
#Funcion para el sharingan
def shr(n,p):
 right(n)
 penup()
 forward(230)
 pendown()
 right(p)
 fillcolor("black")
 begin_fill()
 curve02(1.3,200)
 right(125)
 curve01(1,60)
 left(160)
 curve02(0.85,180)
 end_fill()
 #Llamado del shard.
shr(200,200)
penup()
home()
pendown()
#Llamado del shard.
shr(-15,200)
penup()
home()
pendown()
#Llamado del shard.
shr(90,200)
done()              
