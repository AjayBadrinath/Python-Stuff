import pickle
import os
def del_student():
   load_students()
   printstud()
   f=open("student.dat","rb")
   f1=open("temp1.dat","wb")
   res=input("Do you Want to Delete Records?")
   while res=="y":
      a=input("Enter The Name Of The Student To Be removed: ")
      for i in linkedlist1:
         for j in i:
            if j==a:
               linkedlist1.remove(i)
      res=input("Do You Want to continue Deleting Records?")
   for i in linkedlist1:
      pickle.dump(i,f1)
   f.close()
   f1.close()
   os.remove("student.dat")
   os.rename("temp1.dat","student.dat")
   student_menu()


def liststudbook():
   load_students()
   load_book()
   tag=["Name","Book ID"]
   p=[]
   a=input("Enter student's name")
   for i in tag:
       print(i.ljust(25," "),end=" ")
   print("\n")
   print("--------------------------------------------------------------------")
   print("\n")
   for i in linkedlist1:
      
      if i[1]==a and i[-1]!=0:
         p.append(i[1])
         p.append(i[-1])


   for j in p:
      
      print(str(j).ljust(25," "),end=" ")

   print("\n")
   print("-----------------------------------------------------------------")
              
                  
   print("\n")
            
   student_menu()



   
def liststud():
   printstud()
   student_menu()



 
def book_return():
   load_students()
   printstud()
   load_book()
   printbook()
   try:
        f=open("student.dat","rb")
        f1=open("temp1.dat","wb")
        f2=open("books1.dat","rb")
        f3=open("temp2.dat","wb")
        a=int(input("Enter RollNo Of Student to return book"))
        
        x=[]#student
        y=[]#issuedbook
        #stud=pickle.load(f)
        for i in linkedlist1:
           if i[0]==a:
              x=i
        for j in linkedlist:
           if j[0]==x[-1]:
              j[-1]="Available"
        for i in linkedlist1:
           if i[0]==a:
              
              i[-1]=0
              
         
        print(x)
        
              
         
        
        for i in linkedlist:
           pickle.dump(i,f3)
        for j in linkedlist1:
           pickle.dump(j,f1)
           
        f.close()
        f1.close()
        f2.close()
        f3.close()
        os.remove("student.dat")
        os.rename("temp1.dat","student.dat")
        os.remove("books1.dat")
        os.rename("temp2.dat","books1.dat")
        student_menu()
        
           
           
   except FileNotFoundError:
      f=open("student.dat","wb")
   

def issue():
   global x
   global y
   load_students()
   printstud()
   load_book()
   printbook()
   x=[]#student[r,n,b]
   y=[]
   #book[b,n,a,avl]
   k=""
   m=""

   
   try:
        f=open("student.dat","rb")
        f1=open("temp1.dat","wb")
        f2=open("books1.dat","rb")
        f3=open("temp2.dat","wb")
        a=input("Enter RollNo ")
        b=input("Enter Book/ID To be issued")
        #stud=pickle.load(f)
        for i in linkedlist1:
           if i[1]==a or i[0]==int(a):
              
              x=i
              k=i[1]
        for j in linkedlist:
           if j[0]==int(b):
              y=j

        for i in linkedlist:
           if y[-1]!="Issued":
              res="y"
              print(y,x)
              #print(y[3],x[2])
              while res=="y":
                 y.pop(-1)
                 y.append("Issued")
                 x.pop(-1)
                 x.append(y[0])
                 
                 print("Issued")
                 break
              print(y,x)
              
              for i in linkedlist:
                 if i[0]==b and i[-1]=="Available":
                         linkedlist.remove(i)
                         linkedlist.append(y)
              for i in linkedlist1:
                 if i[0]==a :
                         linkedlist1.remove(i)
                         linkedlist.append(x)
              for i in linkedlist:
                 pickle.dump(i,f3)
              for j in linkedlist1:
                 pickle.dump(j,f1)
                 
              f.close()
              f1.close()
              f2.close()
              f3.close()
              os.remove("student.dat")
              os.rename("temp1.dat","student.dat")
              os.remove("books1.dat")
              os.rename("temp2.dat","books1.dat")
           else:
              print("You Cannot issue a already issued book")
              f.close()
              f1.close()
              f2.close()
              f3.close()
           student_menu()
           
           
   except FileNotFoundError:
      f=open("student.dat","wb")
        
   
def add_student():
   load_students()
   printstud()
   try:
        f=open("student.dat","rb")
        f1=open("temp1.dat","wb")
        res="y"
        
                
                
        while res=="y":
            a=list(eval(input("Enter Your Student Details as Roll NO,Name,Book ID ")))
            if len(a)==3:
               pickle.dump(a,f1)
            res=input("Do you Want To continue Entering Records? Enter y/n")
    
   except FileNotFoundError:
      f=open("student.dat","wb")
        
   f.close()
   f1.close()
   os.remove("student.dat")
   os.rename("temp1.dat","student.dat")
   student_menu()
   
def printstud():
    
    load_students()
    
    tag=["Roll NO","Name","Book ID"]
    for i in tag:
        print(i.ljust(25," "),end=" ")
    print("\n")
    print("--------------------------------------------------------------------")
    print("\n")
    print(linkedlist1)
    for i in linkedlist1:
        #print(i)
        for j in i:
            print(str(j).ljust(25," "),end=" ")

        print("\n")
        print("-----------------------------------------------------------------")
        
            
        print("\n")

   
def load_students():
   global linkedlist1
   try:
        f=open("student.dat","rb")
        f1=open("temp1.dat","wb")
        data1=[]
        linkedlist1=[]
   except FileNotFoundError:
        f=open("student.dat","wb")
        load_students()
        #add_book()
        
   while True:
       try:
           data1=pickle.load(f)
           pickle.dump(data1,f1)
           linkedlist1.append(data1)
          
           
       except EOFError:
           break

   f.close()
   f1.close()
   os.remove("student.dat")
   os.rename("temp1.dat","student.dat")
   
def list_author():
   load_book()
   printbook()
   res=input("Do you Want To Search Books?y/n")
   x=""
   y=[]
   while res=="y":
      a=input("Enter Author Name To Search Book")
      for i in linkedlist:
         for j in linkedlist:
            if j[2]==a:
               x=i
               
                  
      break
   x.pop(0)
   x.pop(-1)
   lst=["BOOK","AUTHOR"]

   for j in lst:
      print(str(j).ljust(25," "),end=" ")
   print("\n")
   print("----------------------------------------")
   print("\n")
   for i in x:
      print(str(i).ljust(25," "),end=" ")
   print("\n")
   print("-----------------------------------------")
   
   print("\n")
   x=input("Do you want to continue Search?y/n")
   if x=="y":
      list_author()
   else:
      exit()
   book_menu()

   
def search():
   load_book()
   printbook()
   res=input("Do you Want To Search Books?y/n")
   x=""
   
   while res=="y":
      a=int(input("Enter Book ID To Search Book"))
      for i in linkedlist:
         for j in i:
            if j==a:
               x=i
      res=input("Do you want to continue?y/n")
   tag=["BOOK ID","Title","Author","Status"]
   for i in tag:
       print(i.ljust(25," "),end=" ")
   print("\n")
   print("------------------------------------------------------------------------------------------")
   print("\n")
   for j in x:
      print(str(j).ljust(25," "),end=" ")
   print("\n")
   print("------------------------------------------------------------------------------------------")
        
            
   print("\n")
   print(x)
   book_menu()

def del_book():
   load_book()
   printbook()
   f=open("books1.dat","rb")
   f1=open("temp1.dat","wb")
   res=input("Do you Want to Delete Records?")
   while res=="y":
      a=input("Enter The Name Of The Book To Be Discarded: ")
      for i in linkedlist:
         for j in i:
            if j==a:
               linkedlist.remove(i)
      res=input("Do You Want to continue Deleting Records?")
   for i in linkedlist:
      pickle.dump(i,f1)
   f.close()
   f1.close()
   os.remove("books1.dat")
   os.rename("temp1.dat","books1.dat")
   book_menu()
   
def editbookstat():
   load_book()
   printbook()
   print(linkedlist)
   res=input("Do you Want To Edit Book Stat?y/n")
   f=open("books1.dat","rb")
   f1=open("temp1.dat","wb")
         
   while res=="y":
       
       x=input("Enter the Book ID to Edit status")
       y=input("Enter the Status to be edited")
       for i in linkedlist:
           if i[0]==x:
               i.pop(-1)
               i.append(y)
       res=input("Do you want to continue?y/n")
   for j in linkedlist:
           pickle.dump(j,f1)
           
   f.close()
   f1.close()
   os.remove("books1.dat")
   os.rename("temp1.dat","books1.dat")
   book_menu()     
               
       
def load_book():
    global data
    global linkedlist
    global tag
    try:
        f=open("books1.dat","rb")
        f1=open("temp1.dat","wb")
        data=[]
        linkedlist=[]
    except FileNotFoundError:
        f=open("books1.dat","wb")
        #add_book()
        
    while True:
       try:
           data=pickle.load(f)
           pickle.dump(data,f1)
           linkedlist.append(data)
          
           #print("The Books Available : ",data)
       except EOFError:
           break

    f.close()
    f1.close()
    os.remove("books1.dat")
    os.rename("temp1.dat","books1.dat")
    
def add_book():
    load_book()
    printbook()
    
    try:
        f=open("books1.dat","rb")
        f1=open("temp1.dat","wb")
        res="y"
        for i in linkedlist:
            pickle.dump(i,f1)
                
                
        while res=="y":
            a=list(eval(input("Enter Your Book Datails BookID,Title,Author,Status")))
            pickle.dump(a,f1)
            res=input("Do you Want To continue Entering Records? Enter y/n")
    
    except FileNotFoundError:
        f=open("books1.dat","wb")
        
    f.close()
    f1.close()
    os.remove("books1.dat")
    os.rename("temp1.dat","books1.dat")
    book_menu()   
def printbook():
    
    load_book()
    print(linkedlist)
    tag=["BOOK ID","Title","Author","Status"]
    for i in tag:
        print(i.ljust(25," "),end=" ")
    print("\n")
    print("------------------------------------------------------------------------------------------")
    print("\n")
    
    for i in linkedlist:
        #print(i)
        for j in i:
            print(str(j).ljust(25," "),end=" ")

        print("\n")
        print("------------------------------------------------------------------------------------------")
        
            
        print("\n")



def student_menu():
    print("------------------------------------ Book Menu --------------------------------------------")
    print("1.Add new Student ")
    print("2.Issue a book to a student")
    print("3.Book Return  ")
    print("4.List all Students")
    print("5.List Students withholding books")
    print("6.Delete Student Record")
    print("7.Go back to main menu")
    x=int(input("Enter your Choice"))
    if x==1:
        add_student()
    elif x==2:
        issue()
    elif x==3:
        book_return()
    elif x==4:
        liststud()
    elif x==5:
        liststudbook()
    elif x==6:
       del_student()
       
        
        
    elif x==7:
        Main_menu()
def book_menu():
    print("------------------------------------ Book Menu --------------------------------------------")
    print("1.Add New Books ")
    print("2.Edit Book status")
    print("3.Discard Book  ")
    print("4.Search based on bookid")
    print("5.List books by author")
    print("6.Go back to main menu")
    x=int(input("Enter your Choice"))
    if x==1:
        add_book()
    elif x==2:
        editbookstat()
    elif x==3:
        del_book()
    elif x==4:
        search()
    elif x==5:
        list_author()
        
        
    elif x==6:
        Main_menu()


def Main_menu():
    print("                                  __                                                             ")
    print("                                 /  \              -----------------   (--------)      -------)  ")                                  
    print("                                /    \                    |            |        |            /   ")
    print("                               /      \                   |            |        |           /    ")
    print("                              /--------\                  |            |        |          /     ")
    print("                             /          \                 |            |        |         /      ")
    print("                            /            \                |            |        |        /       ")
    print("                           /              \               |            0--------0       (------- ")

    print("Welcome To Atoz Library !")
    print("Please Choose From the options Below")
    print("-----------------------------------------------MAIN MENU----------------------------------------")
    print("1.Books Menu ")
    print("2.Students' Menu")
    print("3.Exit")
    print("Please Choose 1,2 or 3")
    print("Please note rollno bookid are intergers and bookname studentname status and author are strings failure  to comply may  result in an error:)")
    a=int(input("Enter your Option:"))
    while a!=4:
        if a==1:
            book_menu()
        elif a==2:
            student_menu()
        elif a==3:
            exit()
        else:
           print("INVALIDINPUT")

Main_menu()











            
      
