
from prettytable import PrettyTable as p

def freq():
    global a,l1,l
    a=input("Enter a string")
    m=p(["Word","Freq"])
    l=a.split(sep=" ")
    l1=[]
    a=""
    for i in l:
        if i[-1].isalnum()==False:
            a+=i[0:len(i)-1]
            l1.append(a)
            a=""
        else:
            a+=i
            l1.append(a)
            a=""
    q=set(l1)
    for i in q:
        m.add_row([i,l1.count(i)])
    print(m)


def encrypt():
    l3=[]
    for i in l:
        x=""
        if len(i)>4:
            if len(i)%2==0:
                x+=i[-2:]+i[0:2]
                l3.append(x)
                x=""
            else:
                x+=i[-2:]+i[int((len(i)-1)/2)].upper()+i[0:2]
                l3.append(x)
                x=""
        else:
            for j in i:
                if j in ['a','A','e','E','i','I','o','O','u','U']:
                    a=ord(j)+2
                    x+=chr(a)
                    l3.append(x)
                    x=""


            else:
                b=ord(j)-2
                x+=chr(b)
                l3.append(x)
                x=""
    print(l3)
                


def replace():
    global l0
    b=input("Enter replacing word")
    p=input("enter a word to be replaced")
    l0=[]
    
    for i in l:
        if i==b:
            
            o=l.index(i)
            l.remove(i)
            l.insert(o,p)
    for i in l:
        print(i,end=" ")
        




while True:
    a=int(input("1.Find/n2.Encrypt/n3.Replace"))
    if a==1:
        find()
    elif a==2:
        encrypt()
    elif a==3:
        replace()
    else:
        print("Error")














        









