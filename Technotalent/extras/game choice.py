from tkinter import *
import os
def command1():
    exec(open(r"C:\Users\Admin\Desktop\pong\handcricket\technotalent.py").read(), globals())
def command2():
    exec(open(r"C:\Users\Admin\Desktop\pong\ponggame\pong1.py").read(), globals())
def command3():
    exec(open(r"C:\Users\Admin\Desktop\pong\space invader\space invader.py").read(), globals())

screen=Tk()
screen.geometry("300x300")
screen.title("Python Game ")
Label(text="Python Game ",bg="green",width ="300",height="1",font=("Ariel",15)).pack()
Label(text=" ").pack()
Button(text="HandCricket - text based",width="20",height="2",bg="red",command=command1).pack()
Label(text=" ").pack()
Button(text="PingPong",width="20",height="2",bg="magenta",command=command2).pack()
Label(text=" ").pack()
Button(text="Space Invaders",width="20",height="2",bg="orange",command=command3).pack()
Label(text=" ").pack()
