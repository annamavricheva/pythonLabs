import turtle
turtle.shape('turtle')
side_width=20
padding=10
for x in range(6):
    for i in range(4):
        turtle.forward(side_width)
        turtle.left(90)
            
    turtle.penup()
    turtle.right(90)
    turtle.forward(padding)
    turtle.left(90)
    turtle.backward(padding)
    turtle.pendown()
    side_width+=2*padding
