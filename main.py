import turtle

screen = turtle.Screen()
screen.screensize(500, 500)
head = turtle.Turtle()
head.shape("square")
head.color("red")

food = turtle.Turtle()

food.goto(random.randrange(0, 500, 20), random.randrange(0, 500, 20))

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
for i in range(segment):
	if segment - 1 == i:
		exec('"' + str(i) + '" = turtle.Turtle()')

if head.pos() == food.pos():
	food.goto(random.randrange(0, 500, 20), random.randrange(0, 500, 20))
	segment += 1

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.mainloop()
