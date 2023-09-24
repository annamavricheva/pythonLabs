from random import randint
import turtle


number_of_turtles = 40
steps_of_time_number = 1000


massive = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in massive:
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.shapesize(0.3)
while 1:
    for unit in massive:
          unit.forward(20)
          unit.right(randint(0,360))
