from tkinter import *
import os
import winsound
winsound.PlaySound("kalimba.mp3",winsound.SND_ASYNC)
import webbrowser

def user_reg():
    username_info=username.get()
    password_info=password.get()
    file=open("user"+".txt","a")
    file.write(username_info)
    file.write("\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    info=Label(screen1,text="Registration Successful").pack()
def command1():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
def login_ver():
    username1 = chkuser.get()
    password1 = chkpassword.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
   
    datafile = open('user.txt')
    found=0
    for line in datafile:
        if password1 in line:
            found=1
            break
    if found == 1:
        Label(screen2,text=" ").pack()
        Button(screen2,text="Click here to play",width="20",height="2",bg="red",command=command1).pack()
        
    else:
        print("login failed")          
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register ")
    screen1.geometry("300x300")
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    Label(screen1,text="Enter your details below").pack()
    Label(screen1,text=" ").pack()
    Label(screen1,text="Username").pack()
    username_entry = Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text=" ").pack()
    Button(screen1,text="Register",width="10",height="1",bg="orange",command= user_reg).pack()   
def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Register ")
    screen2.geometry("300x300")
    Label(screen2,text="Enter your details below").pack()
    Label(screen2,text=" ").pack()
    global username_entry1
    global password_entry1
    global chkuser
    global chkpassword
    chkuser=StringVar()
    chkpassword=StringVar()
    Label(screen2,text="Username").pack()
    username_entry1 = Entry(screen2,textvariable=chkuser)
    username_entry1.pack()
    Label(screen2,text="Password").pack()
    password_entry1 = Entry(screen2,textvariable=chkpassword)
    password_entry1.pack()
    Label(screen2,text=" ").pack()
    Button(screen2,text="Login",height="1",width="10",bg="purple",command=login_ver).pack()
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x300")
    
    
    Button(text="Login",width="20",height="2",bg="red",command=login).pack()
    Label(text=" ").pack()
    Button(text="Register",width="20",height="2",bg="magenta",command=register).pack()
    screen.mainloop()
main_screen()
