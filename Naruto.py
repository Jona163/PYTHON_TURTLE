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

begin_fill()
fillcolor('#373737')
pensize(8)
curve01(0.2,72)
pensize(5)
right(80)
curve01(0.01,240)
right(2)
curve01(0.01,100)
right(2)
curve01(0.02,77)
right(75)
pensize(8)
curve01(0.2,65)
pensize(3)
forward(18)
right(63.5)
curve01(0.1,250)

right(5)
curve01(0.1,100)
left(3)
curve01(0.1,83)
right(70)
forward(10)
pensize(5)
forward(73)
end_fill()
fillcolor('#E8BEAC')
begin_fill()
pensize(8)
left(40)
curve01(1,60)
forward(60)
right(60)
curve01(0.3,27)
left(85)
curve01(0.2,85)

right(30)
forward(133)
right(40)
forward(80)
right(37)
forward(150)
right(35)
curve01(0.1,67)
left(80)
forward(32)
right(50)
curve01(0.5,63)
right(10)
curve01(0.1,40)
right(10)
curve01(0.3,20)

right(70)
forward(7)
pensize(5)
curve02(0.01,418)
end_fill()

backward(10)

fillcolor('yellow')
begin_fill()
right(118)
forward(70)
right(150)
forward(64.5)
right(91)
forward(45)
end_fill()

penup()
backward(100)
pendown()
fillcolor('yellow')
begin_fill()
right(155)
forward(90)
right(155)
forward(50)
right(54)
forward(50)
end_fill()

penup()
backward(180)
pendown()

fillcolor('yellow')
begin_fill()
right(41)
forward(65)
right(165)
forward(91)
right(153)
forward(40)
end_fill()

penup()
backward(110)
pendown()

fillcolor('yellow')
begin_fill()
right(90)
forward(62)
right(158)
forward(72)
right(120)
forward(40)
end_fill()

penup()
left(40)
forward(40)
right(34)
pendown()


fillcolor('grey')
begin_fill()
curve02(0.01,247)
left(85)
curve02(0.02,50)
left(3)
curve02(0.1,35)
left(82)
curve02(0.01,140)
left(2)
curve02(0.1,110)

left(77)
curve02(0.1,86)
end_fill()

penup()
left(138)
forward(20)
dot(10)
left(35)
forward(25)
dot(10)
forward(25)
dot(10)

penup()
right(85)
forward(155)
pendown()
right(135)
forward(22)
right(100)
forward(2)
curve02(2.2,110)
curve02(3,45)
curve02(5,30)
penup()
right(130)
forward(25)
left(85)
pendown()
forward(30)
left(112)
forward(35)
penup()
left(25)
forward(120)
pendown()

dot(10)
right(120)
penup()
forward(30)
pendown()
dot(10)
penup()
forward(30)
pendown()
dot(10)
penup()
left(60)
forward(118)
left(120)
pendown()
pensize(4)
forward(20)
curve02(11,15)
forward(35)
curve02(7,8)
right(15)
forward(15)
right(70)
forward(23)
left(40)
forward(15)

curve02(15,10)
forward(20)
penup()
left(20)
forward(43)
pendown()
left(80)
forward(20)

penup()
left(28)
forward(403)
right(95)
pendown()
forward(28)
curve01(10,15)
right(3)
forward(45)
curve01(8,10)
forward(8)
left(3)

curve02(7,12)
left(10)
forward(15)
curve01(12,13)
right(5)
forward(15)
penup()
right(195)
forward(60)
left(90)
pendown()
curve01(1,45)
penup()
right(119)
forward(65)
right(180)
pendown()
curve01(1,50)
penup()
right(110)
forward(55)
right(190)
pendown()

curve01(1,38)
penup()
right(53)
forward(35)
pendown()
left(20)
forward(70)
curve02(0.2,70)
left(30)
forward(20)
penup()
left(130)
forward(109)
right(35)
pendown()
forward(15)
right(90)
curve02(1,30)
penup()
right(76.5)
forward(143)
pendown()
curve01(1,47)
penup()
right(120)
forward(55)
pendown()
right(192)
curve01(1,47)
penup()
right(120)
forward(45)
pendown()
right(220)
curve01(1,41)
penup()
right(170)
forward(153)
right(138)
forward(5)
pendown()
curve02(0.5,65)
penup()
right(5)

backward(35)
left(80)
forward(5)
pendown()
right(75)
forward(10)
fillcolor('white')
begin_fill()
circle(22)
end_fill()
curve02(3,20)
pendown()
fillcolor('white')
begin_fill()
curve02(6,85)
end_fill()
dot(15)
penup()
left(121)
forward(32)
left(80)
pendown()
pensize(10)
forward(30)
left(95)
pensize(8)
forward(20)
pensize(7)
curve02(1,80)
#second eye
right(54)
penup()
forward(115)
pendown()
pensize(4)
backward(4)
curve01(0.5,60)
penup()
backward(27)
right(90)
forward(8)
pendown()
right(90)
fillcolor('white')
begin_fill()
circle(22)
curve02(3,30)
end_fill()
curve02(6,85)
dot(15)
penup()
right(30)
forward(43)
pendown()
right(85)
pensize(10)
forward(27)
pensize(8)
right(85)
forward(20)
pensize(7)
curve01(1,80)
end_fill()
done()   
