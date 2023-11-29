from turtle import Turtle
import random

pipis = Turtle()
pipis.shape("turtle")
pipis.color(0.1,0.4,0.4)
pipis.pencolor(0.1,0.4,0.4)
pipis.penup()
pipis.setpos(-400, -300)
pipis.pendown()


tigris = Turtle()
tigris.shape("turtle")
tigris.color(1,0.4,0.1)
tigris.pencolor(1,0.4,0.1)
tigris.penup()
tigris.setpos(-400, -100)
tigris.pendown()

timmi = Turtle()
timmi.shape("turtle")
timmi.color(0.1,0.4,1)
timmi.pencolor(0.1,0.4,1)
timmi.penup()
timmi.setpos(-400, 100)
timmi.pendown()

jimi = Turtle()
jimi.shape("turtle")
jimi.color(0.1,1,0.4)
jimi.pencolor(0.1,1,0.4)
jimi.penup()
jimi.setpos(-400, 300)
jimi.pendown()

winner_line = Turtle()
winner_line.shape(None)
winner_line.penup()
winner_line.setpos(350, 400)
winner_line.pendown()
winner_line.right(90)
winner_line.forward(800)

winner = 0
while winner == 0:
    pipis.forward(round(random.random() * 40))
    tigris.forward(round(random.random() * 40))
    timmi.forward(round(random.random() * 40))
    jimi.forward(round(random.random() * 40))

    if pipis.position()[0]>=350: winner=1
    elif tigris.position()[0]>=350: winner=1
    elif timmi.position()[0] >= 350: winner = 1
    elif jimi.position()[0] >= 350: winner = 1


pipis.screen.mainloop()
