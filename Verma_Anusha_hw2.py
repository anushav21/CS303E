import turtle
tom = turtle.Turtle()

#Circle One
tom.pen(pencolor = "light green", fillcolor = "light blue", pensize = 4)
tom.penup()
tom.begin_fill()
tom.goto(0,100)
tom.pendown()
tom.circle(50)
tom.end_fill()
tom.penup()

#Dots
tom.pen(pencolor = "grey", pensize = 3)
dot_x = 0 - 25 
dot_y = 100 + 50
tom.goto(dot_x,dot_y)
tom.pendown()
tom.dot(20)
tom.penup()
dot_x = -25 + 50
tom.goto(dot_x,dot_y)
tom.pendown()
tom.dot(20)

#Circle Two
tom.pen(pencolor = "light green", fillcolor = "light pink", pensize = 4)
tom.penup()
tom.goto(0,-40)
tom.pendown()
tom.begin_fill()
tom.circle(70)
tom.end_fill()

#Square One
tom.pen(pencolor = "purple", fillcolor = "red")
tom.penup()
tom.goto(-12,60)
tom.pendown()
tom.begin_fill()
tom.forward(25)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(25)
tom.end_fill()

#Square Two
tom.penup()
tom.goto(-12,-15)
tom.pendown()
tom.begin_fill()
tom.forward(25)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(25)
tom.right(90)
tom.forward(25)
tom.end_fill()

#Snowman Right Hand 
tom.penup()
tom.goto(125,20)
tom.pendown()
tom.forward(50)
tom.pendown()

#Snowman Left Hand
tom.penup()
tom.goto(-125,20)
tom.pendown()
tom.backward(50)
tom.pendown()

#Circle Three
tom.pen(pencolor = "light green", fillcolor = "beige")
tom.penup()
tom.goto(0,-40)
tom.pendown()
tom.begin_fill()
tom.circle(100)
tom.end_fill()

#Triangle One
tom.pen(pencolor = "orange", fillcolor = "sky blue")
tom.penup()
tom.goto(15,-100)
tom.pendown()
tom.begin_fill()
tom.forward(30)
tom.left(120)
tom.forward(30)
tom.left(120)
tom.forward(30)
tom.end_fill()

#Triangle Two
tom.penup()
tom.goto(3,-200)
tom.pendown()
tom.begin_fill()
tom.forward(30)
tom.left(120)
tom.forward(30)
tom.left(120)
tom.forward(30)
tom.end_fill()

#First Letter of Last Name (V)
tom.penup()
tom.goto(-200,0)
tom.pendown()
tom.right(60)
tom.forward(70)
tom.left(60)
tom.backward(70)







