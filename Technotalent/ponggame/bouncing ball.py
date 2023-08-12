import turtle
import winsound
win=turtle.Screen()
win.title("bouncing ball")
win.bgcolor("red")
win.setup(width=800,height=600)
win.tracer(0)
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=1,stretch_len=5)
paddle1.penup()
paddle1.goto(0,-200)
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.changex=1
ball.changey=-1
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
def paddle1_left():
    x=paddle1.xcor()
    x-=40
    paddle1.setx(x)
def paddle1_right():
    x=paddle1.xcor()
    x+=40
    paddle1.setx(x)
win.listen()
win.onkeypress(paddle1_left,"Left")
win.onkeypress(paddle1_right,"Right")
while True:
    win.update()
    win.update()
    ball.setx(ball.xcor()+ ball.changex)
    ball.sety(ball.ycor()+ ball.changey)
    if ball.ycor()>290:
        ball.sety(290)
        ball.changey*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.changey*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.changex*=-1
      
        pen.clear()
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.changex*=-1
        
        pen.clear()
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (ball.xcor()< -340 and ball.ycor() >-350)and ball.ycor()< paddle1.ycor() +40 and ball.ycor()>paddle1.ycor() -40:
        ball.setx(-340)
        ball.changex*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
