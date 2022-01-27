order={1:["(",")"],
       2:["**"],
       3:["+x",'-x','~x'],
       4:['*','/','//','%'],
       5:['+','-'],
       6:['<<','>>'],
       7:['&'],
       8:['^'],
       9:['|'],
       10:['=','!=','>','>=','<','<=','is','is not','in','not in'],
       11:['not'],
       12:['and'],
       13:['or']
       }
operator1=['(','**','*','/','//','%','+','-'',<<','>>','&','^','|','=','!=','>','>=','<','<=','is','is not','in','not in','not','and','or']
stack=['(']
top=None
def Push(stack,value):
    stack.append(value)
    top=len(stack)-1
a=input("Enter infix Expression: ")
def Peek(stack):
        top=len(stack)-1
        stack[top]

def Pop(stack):
        elm=stack.pop()
        top=len(stack)-1
postfix=[]
def operand(a):
    return a.isalnum()
def operator(a):
    if a in operator1:
        return True
def value(a):
    x=list(order.items())
    for i in x:
	#print(i)
        if a in i[1]:
            return i[0]
            break
for i in a:
    if operand(i)==True:
        postfix.append(i)
    elif operator(i)==True:
        if value(stack[-1])>=value(i):
            postfix.append(stack[-1])
            stack.pop(-1)
            stack.append(i)
        else:
            stack.append(i)
        
    elif i==")":
        while stack[-1]!='(':
            x=stack.pop(-1)
            postfix.append(x)
            if stack[-1]=='(':
                stack.pop(-1)
                








for i in postfix:
	print(i,end=" ")



            
        
        
