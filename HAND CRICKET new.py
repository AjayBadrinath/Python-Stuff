import random
import matplotlib.pyplot as plt
import pyttsx3
import tkinter as tk
engine=pyttsx3.init()
engine.setProperty('rate',130)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id )#Change the index value to change the voice Disclaimer:only voices that are available in the system will be run
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
from tkinter import Tk, Message
from tkinter import messagebox
root = Tk()


def write_slogan():
    print("Cool!Close the dialog box to proceed")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
msg = Message(root, text=' HAND CRICKET ')
msg.config(font=('times', 48, 'italic bold underline'))
button = tk.Button(frame, 
                   text="Quit", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Start",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

msg.pack()

root.mainloop()
d={}
d2={}
rep="y"
s_match=0
sum1=0
lost=0
counter=0
c,c2,c7,c6=0,0,0,0
'''further developents to be done on
    1=>getting the total grand total by cpu and player
    2=>total wickets lost
    3=>using statistics module compute mean
    4=>display the output in a separate window
    5=>few minor bug fixes
    6=>improve UI
    7=>better output
    '''

user=input("Enter your name")
engine.say("Hello")
engine.say(user)
engine.runAndWait()

while rep=="y":
    counter+=1
    l2=["head","tail"]
    for i in l2:
        p=l2[random.randint(0,1)]
    engine.say("Choose heads or tails")
    engine.runAndWait()
    cp=input("HEAD/TAIL")
    if cp==p:
        engine.say("You won the toss")
        engine.runAndWait()
        print("You Won the toss")
        engine.say("Do You want to bat or bowl")
        engine.runAndWait()
        choose=input("Do u  want to bat or bowl")
        if choose=="bat":
            c=0
            engine.say("You Chose to bat")
            engine.runAndWait()
            engine.say("The CPU is bowling")
            engine.runAndWait()
            print("CPU Bowling")
            while True:
                q=random.randint(0,6)
                a=int(input("Enter number"))
                if q!=a:
                    c+=a
                else:
                    break
            engine.say("Your first innings score is ")
            engine.say(c)
            engine.runAndWait()
            print("Your first innings batting score is",c)
            engine.say("Now the CPU's turn to bat")
            engine.runAndWait()
            print("Cpu to bat:")
            c1=0
            while True:
                w1=random.randint(0,6)
                b1=int(input("Enter number "))
                if w1!=b1:
                    c1+=w1
                    print("The CPU chose",w1)
                else:
                    break
                print("Thinking.....")
            engine.say("The CPU Scored")
            engine.say(c1)
            engine.runAndWait()
            print("CPU SCORED",c1)
            if c>c1:
                engine.say("You win by ")
                engine.say(c-c1)
                engine.say("Runs")
                engine.runAndWait()
                print("You win by",c-c1,"runs")
                s_match+=1
            else:
                engine.say("You lose by ")
                engine.say(c1-c)
                engine.say("Runs")
                engine.runAndWait()
                print("You lose by",c1-c,"runs")
                lost+=1
        elif choose=="bowl":
            k=0
            engine.say("You chose to bowl ")
            engine.runAndWait()
            engine.say("The CPU Is batting ")
            engine.runAndWait()
            print("CPU BATTING")
            while True:
                w=random.randint(0,6)
                b=int(input("Enter number "))
                if w!=b:
                    k+=w
                    print("The CPU Entered ",w)
                else:
                    break
                print("Thinking.....")
            engine.say("The CPU Scored")
            engine.say(k)
            engine.runAndWait()
            engine.say("Runs")
            engine.runAndWait()
            print("CPU SCORED",k)
            c2=0
            engine.say("Now it is your turn to bat")
            engine.runAndWait()
            print("NOW YOUR TURN TO BAT")
            while True:
                q2=random.randint(0,6)
                a2=int(input("Enter number"))
                if q2!=a2:
                    c2+=a2
                else:
                    break
            if c2>k:
                engine.say("You Scored ")
                engine.say(c2)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You Scored",c2,"runs")
                engine.say("You Win by")
                engine.say(c2-k)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You Win By",c2-k)
                s_match+=1
            else:
                engine.say("You Scored ")
                engine.say(c2)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You Scored",c2,"runs")
                engine.say("You lose by")
                engine.say(k-c2)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You lose by",k-c2,"runs")
                lost+=1
    else:
        engine.say("Oops You Lost The Toss")
        engine.runAndWait()
        print("U lost toss")
        l3=["bat","bowl"]
        for i in l3:
            m=l3[random.randint(0,1)]
        engine.say("The CPU Chose to")
        engine.say(m)
        engine.runAndWait()
        print("CPU Chose to ,",m)
        if m=="bat":
            engine.say("The CPU is batting first")
            engine.runAndWait()
            print("CPU BATTING FIRST")
            c5=0
            while True:
                q3=random.randint(1,6)
                u=int(input("Enter a number"))
                if u!=q3:
                    c5+=q3
                    print("CPU Entered",q3)
                else:
                    break
                print("Thinking.....")
            engine.say("The CPU Scored ")
            engine.say(c5)
            engine.say("Runs")
            engine.runAndWait()
            print("CPU Scored",c5,"Runs")
            engine.say("Now it is your turn to bat")
            engine.runAndWait()
            print("Your turn to bat")
            c7=0
            while True:
                q7=random.randint(0,6)
                a7=int(input("Enter a number "))
                if q7!=a7:
                    c7+=a7
                else:
                    break
            engine.say("You Scored")
            engine.say(c7)
            engine.say("Runs")
            engine.runAndWait()
            print("You Scored",c7,"Runs")
            if c7>c5:
                engine.say("You Win by")
                engine.say(c7-c5)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You Win by",c7-c5,"runs")
                s_match+=1
            else:
                engine.say("You lose by")
                engine.say(c5-c7)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You lost by",c5-c7,"runs")
                lost+=1
        elif m=="bowl":
            engine.say("Your turn to bat")
            engine.runAndWait()
            print("Your turn to bat")
            c6=0
            while True:
                q5=random.randint(0,6)
                a6=int(input("Enter a number "))
                if q5!=a6:
                    c6+=a6
                else:
                    break
            engine.say("You Scored")
            engine.say(c6)
            engine.say("runs")
            engine.runAndWait()
            print("You Scored",c6,"Runs")
            c8=0
            while True:
                engine.say("Now it is the CPU's Turn to bat")
                engine.runAndWait()
                print("Cpu to bat")
                q8=random.randint(1,6)
                a8=int(input("Enter a number"))
                if a8!=q8:
                    c8+=q8
                    print("THE CPU chose",q8)
                else:
                    break
                print("Thinking.....")
            engine.say("The CPU  Scored")
            engine.say(c8)
            engine.say("runs")
            engine.runAndWait()
            print("CPU Scored",c8,"Runs")
            if c6>c8:
                engine.say("You Win by")
                engine.say(c6-c8)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You Win by",c6-c8,"runs")
                s_match+=1
            else:
                engine.say("You lose by")
                engine.say(c8-c6)
                engine.runAndWait()
                engine.say("Runs")
                engine.runAndWait()
                print("You lost by",c8-c6,"runs")
                lost+=1
    engine.say("Do You Want to continue")
    engine.runAndWait()
    rep=input("Do u want 2 con tinue")
sum1=c+c2+c7+c6
d.update({s_match:lost})
engine.say("Overall out of ")
engine.say(counter)
engine.say("Games")
engine.say("you won")
engine.say(s_match)
engine.say("games")
engine.say("lost")
engine.say(lost)
engine.say("games")
engine.runAndWait()
print("your win to loss ratio is",d)
dialog_title = 'HAND CRICKET'
dialog_text = 'Did you like this game?'
answer = messagebox.askquestion(dialog_title, dialog_text)
if answer == 'yes':
    print('THANK YOU FOR YOUR RESPONSE')
else:  # 'no'
    print('You must have clicked the wrong button by accident.')
engine.say("Now Analyze your perforance by inferring in a bar graph")
engine.runAndWait()
engine.say("Do you have any valueble suggestion to improve this game?")
engine.runAndWait()
suggestion=input("Enter suggestion")
d2.update({1:suggestion})
print(d2)
print("Your Average innings score",sum1/counter)
x=[s_match]
y1=[counter]
plt.bar(y1,x,label="Wins",color='b')

plt.legend()
plt.xlabel('NO of matches')
plt.ylabel('Wins')
plt.title('Win to loss ratio')
plt.show()
x=[sum1]
y=[counter]
plt.bar(y,x,label='Runs',color='r')
plt.legend()
plt.xlabel("no of matches ")
plt.ylabel("runs scored")
plt.show()
