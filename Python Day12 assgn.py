#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 2. Draw a Spiraling Square with Pen color as 'Red'
import turtle as t
a = t.Turtle()
a.pencolor('red')
for i in range (100):
    a.forward(i)
    a.left(91)
t.done()


# In[5]:


# 3. To print large digit from given no
def printLarge(num):
    large = 0
    while num != 0:
        r = num % 10
        if large < r:
            large = r
        num = num // 10
    return large
printLarge(195263)


# In[1]:


# 1. To draw a circle 
import turtle
turtle.color("green")
turtle.begin_fill()
turtle.circle(130,360)
turtle.end_fill()
turtle.hideturtle()
turtle.color("orange")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.done()


# In[7]:


# 4. To print Palindrome count between 2 limits
def isPalindrome(n):
    rev = 0
    buffer = n
    while n!= 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if rev == buffer:
        return True
    else:
        return False
    return
def countPalindrome(lb,ub):
    cnt = 0
    while lb != ub:
        # Implement
        if isPalindrome(lb) == True:
            cnt = cnt + 1
        lb = lb + 1
    return cnt
countPalindrome(100,500)


# In[ ]:


#5. Write a python programming to create and find the word count from given input file
# If the file is contains same word then you need to print the output count

def createfile(filename):
    f=open(filename,'w')
    f.write(data)
    print("File is created and data is written\n To search a word")
    return
filename=str(input("enter file name "))
data=str(input("enter data to store "))
createfile(filename)
def wordcount(filename,word):
    with open(filename,'r')as f:
        if f.mode=='r':
            x=f.read()
            li=x.split() # It splits the string with white spaces
    cnt=li.count(word)
    return cnt
a=str(input("enter file name "))
b=str(input("enter a word "))
wordcount(m,n)


# In[ ]:




