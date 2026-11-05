import turtle

def draw_maze(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fd(300)
    t.rt(90)
    t.fd(300)
    t.lt(90)
    t.fd(300)

def turn_left():
    t.lt(10)
    t.fd(10)

def turn_right():
    t.rt(10)
    t.fd(10)

t=turtle.Turtle()
screen=turtle.Screen()
t.shape("turtle")
t.speed(0)

draw_maze(-300,100)
draw_maze(-200,200)
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")

t.penup()
t.goto(-300,150)
t.speed(1)
t.pendown()
screen.listen()
screen.mainloop()
