#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. program to print the fabinocci series in the reverse order
def fabinoccirev(x):
    while x-2!=0:
        a=0
        b=1
        c=0
        for i in range(x-2):
            c=a+b
            a=b
            b=c
        print(c,end=" ")
        x-=1
    print('1 0')
    return
fabinoccirev(int(input("enter number"))) 


# In[4]:


# 2.Sum of non repeated integers
def sum(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:
                if a[i]==a[j]:
                    c+=1
        if c==0:
            s=s+a[i]
    return s
sum(int(input("no of values")))


# In[6]:


#3.
def Pattern(a,b):
    if len(a)<=len(b):
        n=len(a)
        k=len(b)
    else:
        n=len(b)
        k=len(a)
    for i in range(n):
        print(a[i],b[i])
    for j in range(n,k):
        if(len(a)<=len(b)):
            print(b[j],'*')
        else:
            print(a[j],'*')
    return
x=str(input("enter string:"))
x=x.split()
Pattern(x[0],x[1])


# In[11]:


#4.
def longeststring(a,b):
    if len(a)>=len(b):
            print(a.upper())
    else:
            print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
longeststring(x[0],x[1])


# In[15]:


#5a.
def alpha(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
x=str(input("enter str:"))
alpha(x)


# In[14]:


#6
def findNthTerm(n): 
    if  n % 2 == 0: 
        n //= 2
        print(3 ** (n - 1)) 
    else: 
        n = (n // 2) + 1
        print(2 ** (n - 1)) 
if __name__=='__main__': 
    N = 3
    findNthTerm(N) 
    N = 21
findNthTerm(N) 


# In[13]:


#7
def no(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end="")
            print("")
    return
x=input("enter num")
no(list(x))


# In[ ]:


#8. Program to read one string as well as one character and you need to remove the all the occurance of the character.
def delete(n,target):
    c=0
    for i in range(len(n)):
        if n[i]==target:
            c+=1
    print(n.replace(target,"",c))
n=str(input("enter a string"))
target=str(input("enter a char"))
delete(n,target)


# In[ ]:


# 9.Program need to accept two strings and generate the output in merging of both strings.
def merge(a,b):
    c=a+b
    return c 
a=str(input("enter a string "))
b=str(input("enter a string "))
merge(a,b)


# In[1]:


# 10. Series Generations:-  1, 3, 9, 27, 81, ...
def square(n):
    for i in range(n):
        print(3**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[2]:


# 11. Series Generations:-  1, 2, 4, 8, 16, 32, 64, 128, 256, ...
def square(n):
    for i in range(n):
        print(2**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[3]:


# 12. Series Generations:-  1 3 4 8 15 27 50 92 169 311
def series(n):
    a=1
    b=3
    c=a+b
    print(a,b,c,end=" ")
    for i in range (4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(d,end=" ")
    return
n=int(input("enter a number"))
series(n)


# In[5]:


# 13. Series Generations:-  2 15 41 80 132 197 275 366 470 587
def series(n):
    a=2
    print(a,end=" ")
    for i in range (1,n+1):
        b=a+(13*i)
        print(b,end=" ")
        a=b
    return
n=int(input("enter a number"))
series(n)


# In[4]:


# 14. Series Generations:-  1! + 2! + 3! + 4! + 5! + ... + n!
def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[11]:


# 15.Series Generations:-  1,9,17, 33,49,73,97
import math
def seriesgeneration(n):
    s=1
    i=2
    while i<=n+1:
        a=math.ceil(i/2)
        s=s+8*(a-1)
        print(s,end=" ")
        i=i+1
    return 
seriesgeneration(10)
    


# In[ ]:




