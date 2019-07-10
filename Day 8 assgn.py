#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 1) [1,4,5,6,9] - 14569
def convert(s):
    x=0
    for i in range(len(s)):
        x=x*10+s[i]
    return x
s=[1,4,5,6,9]
convert(s)


# In[9]:


# 2) [1,4,5,6,9]  - 46 (Consider only even numbers from list)
def even(s):
   x=0
   for i in range(len(s)):
       if s[i]%2==0:
           x=x*10+s[i]
   return x
s=[1,4,5,6,9]
even(s)


# In[1]:


# 3. [1,2,3,4,5] - [1,4,3,16,5] (Consider only even number and square of it)
def square(s):
    for i in range (len(s)):
        if s[i]%2==0:
            s[i]=s[i]**2
    return s
s=[1,2,3,4,5]
square(s)


# In[1]:


#4)

def linearSearch5(li):
    print("[ ",end="")
    for x in range(len(li)-1):
        if x ==0 or x == len(li) -1:
            print(li[x],end=",")
        else:
            print(li[x-1]+li[x],end=",")
    print(li[(len(li)-1)],"]")
    return
li = [15,19,12,16,4]
linearSearch5(li)

