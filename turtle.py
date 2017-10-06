#!/bin/python3

from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)

for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)


ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

bg = Turtle()
bg.color('purple')
bg.shape('turtle')
bg.penup()
bg.goto(-160,70)
bg.pendown()

we = Turtle()
we.color('blue')
we.shape('turtle')
we.penup()
we.goto(-160,40)
we.pendown()

er = Turtle()
er.color('yellow')
er.shape('turtle')
er.penup()
er.goto(-160,10)
er.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bg.forward(randint(1,5))
  we.forward(randint(1,5))
  er.forward(randint(1,5))
