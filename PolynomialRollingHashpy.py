'''
Polynomial rolling hash
H(s)=s[0]*P**(0)+s[1]*P**(1)+...s[n-1]*P**(n-1)

'''
prime=31
modulo=100000000
s= input("Enter a string")
def hash(s):
    k=0
    i=0
    while(i<len(s)):
        x=ord(s[i])-97
        k+=(x*(prime**i))%modulo
        i+=1
    return k
print("Hash: ",hash(s))
