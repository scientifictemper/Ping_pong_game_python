import turtle
import os
wn=turtle.Screen()
wn.title('pong develop by bg')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)
# padel A
padel_a=turtle.Turtle()
padel_a.speed(0)
padel_a.color('white')
padel_a.shape('square')
padel_a.shapesize(stretch_wid=5,stretch_len=1)
padel_a.penup()
padel_a.goto(-350,0)
#padel B
padel_b=turtle.Turtle()
padel_b.speed(0)
padel_b.color('white')
padel_b.shape('square')
padel_b.shapesize(stretch_wid=5,stretch_len=1)
padel_b.penup()
padel_b.goto(350,0)
#BALL
ball=turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('circle')
ball.penup()
ball.goto(0,0)
#speed of the ball
ball.dx=.1
ball.dy=.1
#PEN
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0,260)
pen.hideturtle()
# FUNCTION
def padel_a_up():
    y=padel_a.ycor()
    y+=20
    padel_a.sety(y)
def padel_a_down():
    y=padel_a.ycor()
    y-=20
    padel_a.sety(y)
def padel_b_up():
    y=padel_b.ycor()
    y+=20
    padel_b.sety(y)
def padel_b_down():
    y=padel_b.ycor()
    y-=20
    padel_b.sety(y)

#score
score_a=0
score_b=0

#keyboard
wn.listen()
wn.onkeypress(padel_a_up,'w')
wn.onkeypress(padel_a_down,'s')
wn.onkeypress(padel_b_up,'i')
wn.onkeypress(padel_b_down,'j')

# MAIN LOOP
while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #checking border
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy*=-1
        os.system('aplay pop.wav&')
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy*=-1
        os.system('aplay pop.wav&')
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write('Player A:{} Player B:{}'.format(score_a,score_b), align='center', font=('courier', 24, 'normal'))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write('Player A:{} Player B:{}'.format(score_a,score_b), align='center', font=('courier', 24, 'normal'))

    #paddle and ball collision
    if (ball.xcor()>340 and ball.xcor()<350)and(ball.ycor()<padel_b.ycor()+50 and ball.ycor()>padel_b.ycor()-50):
        ball.setx(340)
        ball.dx*=-1
        os.system('aplay pop.wav&')
    if (ball.xcor()<-340 and ball.xcor()>-350)and(ball.ycor()<padel_a.ycor()+50 and ball.ycor()>padel_a.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1
        os.system('aplay pop.wav&')
