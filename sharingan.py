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
