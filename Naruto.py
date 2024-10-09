# Autor: Jonathan Hernández
# Fecha: 9/10/24
# Descripción: Código para usar turtle.
# GitHub: https://github.com/Jona163

from turtle import *
pencolor("red")
pensize(8)
hideturtle()

pencolor('black')


left(13)
speed(8)
fillcolor("yellow")
begin_fill()
penup()
forward(190)
pendown()

#Hair
right(25)
forward(60)
left(135)
forward(100)
right(95)
forward(95)
left(135)
forward(110)
right(105)
forward(115)
left(135)

forward(145)
right(112)
forward(115)
left(137)
forward(163)
right(110)
forward(115)
left(130)
forward(142)
right(85)
forward(120)
left(130)
forward(128)
right(100)
forward(110)
left(126)
forward(115)
right(73)
forward(82)
left(136)
forward(60)

pensize(3)
left(70)
forward(15)
right(59)
def curve01(a,d):
 for i in range(d):
  right(a)
  forward(1)

def curve02(a,d):
 for i in range(d):
  left(a)
  forward(1)

curve01(0.1,260)
curve01(0.2,80)
left(6)
curve01(0.1,90)
right(60)
forward(11)
end_fill()
