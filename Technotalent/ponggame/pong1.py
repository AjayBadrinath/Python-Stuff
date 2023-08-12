#ping pong
import turtle
import winsound
win=turtle.Screen()
win.title("Pong Game")
win.bgcolor("green")
win.setup(width=800,height=600)
win.tracer(0)
paddle1=turtle.Turtle()
paddle1.speed(-1)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-400,0)

paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5,stretch_len=2)
paddle2.penup()
paddle2.goto(400,0)
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
pen.write("Player1:0 Player 2:0",align=  "center",font=("Arial",24,"normal"))
def paddle1up():
    y = paddle1.ycor()
    y+=40
    if y>260:
        y=260
    paddle1.sety(y)
def paddle1down():
    y = paddle1.ycor()
    y-=40
    if y<-260:
        y=-260
    paddle1.sety(y)
def paddle2up():
    y = paddle2.ycor()
    y+=40
    if y>260:
        y=260
    paddle2.sety(y)
def paddle2down():
    y = paddle2.ycor()
    y-=40
    if y<-260:
        y=-260
    paddle2.sety(y)
win.listen()
win.onkeypress(paddle1up,"w")
win.onkeypress(paddle1down,"s")
win.onkeypress(paddle2up,"Up")
win.onkeypress(paddle2down,"Down")
score1=0
score2=0
while True:
    win.update()
    ball.setx(ball.xcor()+ ball.changex)
    ball.sety(ball.ycor()+ ball.changey)
    if ball.ycor()>290:
        ball.sety(290)
        ball.changey*=-0.7
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.changey*=-0.7
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.changex*=-0.7
        score1+=1
        pen.clear()
        pen.write("Player1:{} Player 2:{}".format(score1,score2),align=  "center",font=("Arial",24,"normal"))
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()<-400:
        ball.goto(0,0)
        ball.changex*=-0.9
        score2+=1
        pen.clear()
        pen.write("Player1:{} Player 2:{}".format(score1,score2),align=  "center",font=("Arial",24,"normal"))
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (ball.xcor()> 340 and ball.ycor() <350)and ball.ycor()< paddle2.ycor() +40 and ball.ycor()>paddle2.ycor() -40:
        ball.setx(340)
        ball.changex*=-0.9
        winsound.PlaySound("HIT.wav",winsound.SND_ASYNC)
    if (ball.xcor()< -340 and ball.ycor() >-350)and ball.ycor()< paddle1.ycor() +40 and ball.ycor()>paddle1.ycor() -40:
        ball.setx(-340)
        ball.changex*=-0.9
        winsound.PlaySound("HIT.wav",winsound.SND_ASYNC)
        
                                                      
