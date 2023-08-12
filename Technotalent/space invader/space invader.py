#space invaders
import turtle
import winsound
import math
import random
window=turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.setup(width=800,height=700)
window.bgpic("bgspace.gif")
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
border=turtle.Turtle()
border.speed(0)
border.color("White")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(2)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()
score=0
scorepen=turtle.Turtle()
scorepen.speed(0)
scorepen.color("white")
scorepen.penup()
scorepen.setposition(-290,280)
scorepen.write("Score:0",align=  "left",font=("Arial",14,"normal"))
scorepen.hideturtle()
pawn=turtle.Turtle()
pawn.color("green")
pawn.shape("player.gif")
pawn.penup()
pawn.speed(0)
pawn.setposition(0,-250)
pawn.setheading(90)



no=6
invaders=[]
for j in range(no):
    invaders.append(turtle.Turtle())
for invader in invaders:   
    invader.color("red")
    invader.shape("invader.gif")
    invader.penup()
    invader.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    invader.setposition(x,y)
invaderspeed=2
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.penup()
bulletspeed=20
bulletstate="ready"
bullet.hideturtle()
def pawnleft():
    x=pawn.xcor()
    x-=40
    if x<-280:
        x=-280
    pawn.setx(x)
def pawnright():
    x=pawn.xcor()
    x+=40
    if x>280:
        x=280
    pawn.setx(x)
def fire():
    global bulletstate
    if bulletstate =="ready":
        winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
        bulletstate="fire"
        x=pawn.xcor()
        y=pawn.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()
def collision(t1,t2):
    dist=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if dist <15:
        return True
    else:
        return False
        
window.listen()
window.onkeypress(pawnleft,"Left")
window.onkeypress(pawnright,"Right")
window.onkeypress(fire,"space")

while True:
    for invader in invaders:
        x=invader.xcor()
        x += invaderspeed
        invader.setx(x)
        if invader.xcor()>280:
            for i in invaders:
                y=i.ycor()
                y-=40
                i.sety(y)
            invaderspeed *= -1
        if invader.xcor()<-280:
            for i in invaders:
                y=i.ycor()
                y-=40
                i.sety(y)
            invaderspeed*=-1
        if collision(bullet,invader):
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            x=random.randint(-200,200)
            y=random.randint(100,250)
            invader.setposition(x,y)
            score+=10
            scorepen.clear()
            scorepen.write("Score:{}".format(score),align=  "left",font=("Arial",14,"normal"))
            
        if collision(pawn,invader):
            winsound.PlaySound("fail.wav",winsound.SND_ASYNC)
            pawn.hideturtle()
            invader.hideturtle()
            print("Game over")
            break
    if bulletstate =="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
    if bullet.ycor()>280:
        bullet.hideturtle()
        bulletstate="ready"

       

