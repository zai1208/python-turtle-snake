import turtle

screen = turtle.Screen()
head = turtle.Turtle()
head.shape("square")
head.color("red")

screen.listen()

def up():
    direction = 90
def down():
    direction = 270
def right():
    direction = 180
def left():
    direction = 0
	
head.setheading(direction)
head.forward(20)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.mainloop()
