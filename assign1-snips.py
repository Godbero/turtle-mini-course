# Joy of Coding Assignment 1
# March 10, 2024

# print("Hello, World!")

turtle.color("blue")

size = 100
turtle.forward(size)
turtle.right(120)
turtle.forward(size)
turtle.right(120)
turtle.forward(size)

for i in range(3):
  turtle.forward(size)
  turtle.right(120)

for i in range(3):
  turtle.forward(size)
  turtle.left(120)

turtle.Screen().exitonclick()

 ----------------------------------------
def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.right(120)

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

turtle.color("blue")

triangle(100)
back(75)
triangle(50)
back(50)
triangle(25)

turtle.Screen().exitonclick()
