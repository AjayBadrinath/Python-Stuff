import sys
#"splchar":["!","@","#","$",".",",",":","%","^","*"]

splchar=[chr(i) for i in range(33,48)]#ASCII spl charecter range from 33-48 and58-65#and i here is the mapping expression ie the thing thet is executed evry iteration
splchar1=[chr(i) for i in range(58,65)]#Instead of explicit declaration of for loop this is better for assigning number and converting to charecter then make it a list

splchar+=splchar1#making all spl char in one list

letter={"cap":"ABCDEFGHIJKLMNOPQRSTUVWXYZ","alpha":"abcdefghijklmnopqrstuvwxyz","digit":"0123456789","white_space":[" ","\t","\n"],
        "splchar":splchar}#Dictionary to be used
print("Enter your string with multiple lines\n")
print("Ctrl+D to Terminate input\n")
a=sys.stdin.read()#ctrl+d to finish input#this is for multiline input
x=list(letter.items())#return Datatype dict_item so convert to list which return tuples in list
lineno=[j for j in a if j=="\n"]#list of \n
cap,small,digit,whitespace,spl=0,0,0,0,0#Assign all values to be 0

'''Implementation of switch case(sort of)'''

d1={"cap":"if i in x[j][-1] and x[j][0]=='cap':cap+=1",
    "alpha":"if i in x[j][-1] and x[j][0]=='alpha':small+=1",
    "digit":"if i in x[j][-1] and x[j][0]=='digit':digit+=1",
    "white_space":"if i in x[j][-1] and x[j][0]=='white_space':whitespace+=1",
    "splchar":"if i in x[j][-1] and x[j][0]=='splchar':spl+=1"
    }
#here to be specific the switch case here uses executable command with shared key with dictionary letter
for i in a:#Check the each charecter of input a
    for j in range(0,len(x)):#Accessing the list of key value pair from letter 
        exec(str(d1.get(x[j][0])))#exec execute string and this access the switch statement
        
print("\nThe total number of caps",cap,"\nSmall:",small,"\ndigit:",digit,"\nwhitespaces",whitespace,"\nSpecialCharecters",spl,"\nTotal Alphabets",cap+small,
      "\nTotal lines", len(lineno))

            
            
            




