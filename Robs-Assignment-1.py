# Joy of Coding Assignment 1
# by Robert Godbey
# March 10, 2024

print("Hello, World! My name is Rob")

import turtle

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def move(len):
# To move backwards use negative length, e.g. -50
  turtle.penup()
  turtle.forward(len)
  turtle.pendown()

def triangle(size):
  # Equalatial triangle has 120-degree turns
  for i in range(3):
    turtle.forward(size)
    turtle.right(120)

def square(size):
  # A rectangle (square) has 90-degree turns
  for i in range(4):
    turtle.forward(size)
    turtle.right(90)

def polygon1(sides, length):
  # To make a regular polygon divided 360 degrees by the number of sides
  angle = 360/sides
  for i in range(sides):
    turtle.forward(length)
    turtle.right(angle)

def polygon2(sides, length, color):
  # Add in the ability to set the color
  turtle.color(color)
  angle = 360/sides
  for i in range(sides):
    turtle.forward(length)
    turtle.right(angle)

def polygon3(sides, length, color="black"):
  # Error checking
  if sides < 3:
    print("Error, a polygon needs at least 3 sides")
    return
  turtle.color(color)
  angle = 360/sides
  for i in range(sides):
    turtle.forward(length)
    turtle.right(angle)

def polygon4(sides, length, up, color="black"):
  # Error checking
  if sides < 3:
    print("Error, a polygon needs at least 3 sides")
    return
  turtle.color(color)
  angle = 360/sides
  # Add in the ability to draw up or down (think triangle point)
  for i in range(sides):
    turtle.forward(length)
    if up == 1:
      turtle.left(angle)
    else:
      turtle.right(angle)

def spiral(length, angle):
  for i in range(20):
    turtle.forward(length)
    turtle.right(angle)
    length = length - 5

def spiral2(length, angle):
  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  for i in range(20):
    turtle.color(colors[i])
    turtle.forward(length)
    turtle.right(angle)
    length = length - 5

def spiral3(length, angle):
  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  n = 0
  for i in range(length, 5, -5):
    turtle.color(colors[n])
    turtle.forward(i)
    turtle.right(angle)
    n += 1

turtle.color("blue")

# Draw 3 blue triangles
triangle(100)
back(75)
triangle(50)
back(50)
triangle(25)
turtle.goto(0,0)
turtle.clear()

# Draw 2 blue squares
square(100)
back(125)
square(50)
turtle.goto(0,0)
turtle.clear()

# Draw a 6-sided blue polygon
polygon1(6, 100)
turtle.goto(0,0)
turtle.clear()

# Draw a 8-sided red polygon
polygon2(8, 100, "red")
turtle.goto(0,0)
turtle.clear()

# Draw 7 green assorted color polygons
for i in range(7):
  polygon3(i+3, 50, "green")
turtle.goto(0,0)
turtle.clear()

# Draw 7 different color different sided polygons
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(7):
  polygon4(i+3, 50, i%2, colors[i])
turtle.goto(0,0)
turtle.clear()

spiral(100, 60)
turtle.goto(0,0)
turtle.clear()

spiral2(100, 60)
turtle.goto(0,0)
turtle.clear()

spiral3(75, 45)  
move(150)
spiral3(100, 90)

turtle.Screen().exitonclick()
