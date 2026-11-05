import turtle

def drawBar(height):
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.write(str(height),font=('Times New Roman',16,'bold'))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

data=[100,120,270,80,90,130,250]

t=turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)

for d in data:
    drawBar(d)
