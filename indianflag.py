import turtle

def rectangle():
  flag.forward(150)
  flag.right(90)
  flag.forward(40)
  flag.right(90)
  flag.forward(150)
  flag.right(90)
  flag.forward(40)
  
flag = turtle.Turtle()
flag.speed(1)
flag.penup()
flag.goto(-200,200)
flag.pendown()
flag.begin_fill()
flag.color("orange")
rectangle()
flag.end_fill()
flag.right(90)
flag.right(90)
flag.forward(40)
flag.left(90)

flag.begin_fill()
flag.color("white")
rectangle()
flag.end_fill()

flag.right(90)
flag.right(90)
flag.forward(40)
flag.left(90)

flag.begin_fill()
flag.color("green")
rectangle()
flag.end_fill()

flag.right(90)
flag.forward(75)
flag.color("black")
flag.circle(20)

flag.left(90)
flag.penup()
flag.forward(20)
flag.pendown()

for i in range(0,24):
  flag.right(15)
  flag.forward(20)
  flag.backward(20)
flag.end_fill()
turtle.done()













