import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',160)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id )
engine.runAndWait()#Change the index value to change the voice Disclaimer:only voices that are available in the system will be run
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
engine.say("Welcome to Hand Cricket")
engine.runAndWait()
engine.say("We'll have the toss now")
engine.runAndWait()
engine.say("Choose odd or even. Type 1 if you choose odd and 2 if you choose even")
engine.runAndWait()
a=int(input("Choose odd or even. Type 1 if you choose odd and 2 if you choose even"))
engine.say("Enter a number between 1 and 6")
engine.runAndWait()
x=int(input("Enter a number between 1 and 6"))
import random
b=random.randint(1,6)
print(b)
engine.say(b)
engine.runAndWait()
count1=0
if a==1:
     if (x+b)%2==1:
          engine.say("You won the toss!")                                                                                                  
          engine.runAndWait()#
          c=int(input("Choose to bat or bowl. Enter 3 if you want to bat and 4 if you want to bowl"))
     else:
          count1=1
          c=0
          engine.say("I won the toss. I am going to bat, you will bowl first")                                        
          engine.runAndWait()#
elif a==2:
     if (x+b)%2==0:
          engine.say("You won the toss!")                                                                                           
          engine.runAndWait()#
          c=int(input("Choose to bat or bowl. Enter 3 if you want to bat and 4 if you want to bowl"))
     else:
          count1=1
          c=0
          engine.say("I won the toss. I am going to bat. you will bowl first")                         
          engine.runAndWait()#
if c==3:
     score=0
     score1=0
     engine.say("Let's start the first innings.You are going to bat now I will bowl")                  
     engine.runAndWait()#
     while True:
          d=int(input("Enter a number from 1 to 6"))
          e=random.randint(1,6)
          engine.say(e)
          print(e)
          if d!=e:
               score+=d
               engine.say("Your score is")
               engine.say(score)
               engine.runAndWait()
               print("Your score is",score)
          if d==e:
               engine.say("Out!1st innings is over")
               engine.runAndWait()
               print("Out!1st innings is over")
               engine.say("Your score is")
               engine.say(score)
               engine.runAndWait()
               print("Your score is",score)
               engine.say("My target is")
               engine.say(score+1)
               engine.runAndWait()
               print("My target is",score+1)
               break
     engine.say("Let's start the second innings. I am going chase your target, you will bowl")        
     engine.runAndWait()#
     engine.say("Target:")
     engine.say(score+1)                                                                                                        
     engine.runAndWait()#
     while True:
          f=random.randint(1,6)
          g=int(input("Enter a number from 1 to 6"))
          engine.say(f)
          engine.runAndWait()#
          if f!=g:
               score1+=f
               if score1>=score+1:
                    engine.say("I won! Reached the target. Better luck next time")                       
                    engine.runAndWait()#
                    break
               else:
                    engine.say("My score is")
                    engine.say(score1)                                                                                
                    engine.runAndWait()#
                    engine.say("I need")
                    engine.say(score+1-score1)
                    engine.say("runs to win")               
                    engine.runAndWait()#
          elif f==g:
               if score1==score:
                    engine.say("Match tied")
                    engine.runAndWait()#
                    break
               else:
                    engine.say("I am out! Congratulations! You won the game by")
                    engine.say(score+1-score1)
                    engine.say("runs") 
                    engine.runAndWait()#
                    break
elif c==4 or count1==1:
     score=0
     score1=0
     engine.say("Let's start the first innings.You are going to bowl now, I will bat")                
     engine.runAndWait()#
     while True:
          d=int(input("Enter a number from 1 to 6"))
          e=random.randint(1,6)
          engine.say(e)
          engine.runAndWait()#
          if d!=e:
               score+=e
               engine.say("My score is")
               engine.say(score)
               engine.runAndWait()#
          if d==e:
               engine.say("I am Out!1st innings is over")              
               engine.runAndWait()#
               engine.say("Your target is")
               engine.say(score+1)
               engine.runAndWait()#
               break
     engine.say("Let's start the second innings. You are going to chase my target, I will bowl")
     engine.runAndWait()#
     engine.say("Target:")
     engine.say(score+1)
     engine.runAndWait()#
     while True:
          f=random.randint(1,6)
          g=int(input("Enter a number from 1 to 6"))
          engine.say(f)
          if f!=g:
               score1+=g
               if score1>=score+1:
                    engine.say("You won! Reached the target. Congratualations")
                    engine.runAndWait()#
                    break               
               else:
                    engine.say("Your score is")
                    engine.say(score1)
                    engine.runAndWait()#
                    engine.say("You need")
                    engine.say(score+1-score1)
                    engine.say("runs to win")
                    engine.runAndWait()#
          elif f==g:
               if score1==score:
                    engine.say("Match tied")
                    engine.runAndWait()#
                    break
               else:
                    engine.say("You are out! Sorry! Better luck next time! I won the game by")
                    engine.say(score+1-score1)
                    engine.say("runs")
                    engine.runAndWait()#
                    break
          
               
          
          

     
