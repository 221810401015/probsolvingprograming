#!/usr/bin/env python
# coding: utf-8

# ###  Regular Expressions
# * pattern matching
# * Patterns package[re]
# * [0-9] any digit matching
#         > Two digit number (^[0-9]{2}$)
#         > Five digit number (^[0-9]{5}$)

# ### Regular Expressions for Characters
# - [a-z] : Any Lower case characters
# - [A-Z] : Any Upper Case characters
# -^[a-z]{5}$ : It accepts 5 lower case characters
# -^[a-zA-Z]{8} : Accepts 8 characters can be upper or lower case
# -^[a-zA-Z0-9]{8}$ : Accepts 8 characters can be anything upper,lower,digits
# 

# In[1]:


#Function to test two digit no matching
import re
def twoDigitMatching(n):
    pattern = '^[0-9]{3}$'
    n = str(n)
    if re.match(pattern,n):
        return True
    return False
print(twoDigitMatching(15))
print(twoDigitMatching(999))


# In[2]:


# Function to define to test usename having 8 chaeacters
# Uppercase and lower
import re
def testUsername(s):
    pattern = '^[a-zA-Z0-9]{9}$'
    if re.match(pattern,s):
        return True
    return False
print(testUsername('gItAmHyD6'))
print(testUsername('Gitam118'))


# ### Regular Expression to match the Indian Mobile No
# - 10 Digits
# - (First digit will be [6-9] and remaining 9 digits will be [0-9]
# - Example : 6303722875
# - Re : ^[6-9][0-9]{9}$
# - Example : 08899774455 (Re - ^[0][6-9][0-9]$)
# - Re : ^[+][9][1][6-9][0-9]{9}

# In[3]:


#Functio to Validate the Indian Mobile No
def phoneNumberValidation(phone):
    pattern = '^[6-9][0-9]{9}$|^[0][6-9][0=9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone = str(phone)
    if re.match(pattern,phone):
        return True
    return False
phoneNumberValidation('+919988774455')


# -- Regular Expression to validate the Roll number
#    * Example : 1521A0501
#    * Example : 1521A0109
#    * Example : 1521A0499
#  -- Regular Expression to validate the password
#    * Parameters : Len of min 6characters and Max of 15 characters
#    * Accept Lowercase , Uppercase , digits

# In[4]:


def validateRollnumber(rollno):
    pattern = '^[0-6]{4}[A-Z]{1}[0-9]{4}$'
    rollno = str(rollno)
    if re.match(pattern,rollno):
        return True
    return False
validateRollnumber('1521A0501')


# In[5]:


def validatePassword(password):
    pattern = '^[a-zA-Z0-9!-~]{6,15}$'
    password = str(password)
    if re.match(pattern,password):
        return True
    return False
validatePassword('DeEp123456789')


# ### Email id validation using Regular expression
# - Example : Username@DomainName.extension
# - Username :
#          - Length will be [6-15]
#          - No Spls characters apart from Underscore(_)
#          - Should not end and begin with Underscore(_)
#          - Characters Set : All digits and lowercase
# - DomainName :
#          - Length will be [3-18]
#          - No spcl characters
#          - characters Set: All digits and lowercase
# - Extension :
#          - - Length will be [2-4]
#          - No spcl characters
#          - characters Set:  lowercase

# In[6]:


import re
def emailValidation(email):
    pattern = '^[0-9a-z][0-9a-z_.]{5,16}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
emailValidation('ganjianudeep123@gmail.com')


# ### Python Turtle
# * Turtle Graphics

# In[7]:


# Step 1: Make all the turtle package to be imported
import turtle
# Turtle method creates and returns a new object
a1 = turtle.Turtle()
#Forward( ) method moves 100 pixels
turtle.forward(500)
# We are done
turtle.done()


# In[8]:


#line drawn in reverse
import turtle as tt
a1 = tt.Turtle()
a1.backward(100)
tt.done()


# In[ ]:


# Draw square
import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[ ]:


# Draw triangle
import turtle as tt
a1 = tt.Turtle()
a1.forward(100)
a1.right(120)
a1.forward(100)
a1.right(120)
a1.forward(100)
a1.right(120)
tt.done()


# In[ ]:


# Loop Statement
import turtle as t
aa = t.Turtle()
for i in range(4):
    aa.backward(150)
    aa.left(90)
t.done()


# In[ ]:


#Star
import turtle as t
a1 = t.Turtle()
for i in range(6):
    a1.forward(50)
    a1.left(144)
t.done()


# In[1]:


# Spirling Star
import turtle as t
a1 = t.Turtle()
a1.pencolor('red')
for i in range(100):
    a1.forward(i * 10)
    a1.left(144)
t.done()


# In[2]:


# Square  Spiral help of turtle
import turtle as t
a1 = t.Turtle()
a1.pencolor('red')
for i in range(250):
    a1.forward(i)
    a1.left(91)
t.done()


# In[1]:


# Hexagon with Multi color
from turtle import *
colors = ['blue','green','red','blue','orange','black']
for x in range(360):
          pencolor(colors[x%6])
          width(x/100 + 1)
          forward(x)
          left(59)


# In[1]:


# Goto function
from turtle import *
goto(50,50)
goto(-50,50)
goto(100,-50)
goto(-50,-50)


# In[1]:


# Setheading(Heading)
# will change the current direction to the heading angle
from turtle import *
colors = ['blue','green','red','blue','orange','black']
for angle in range(0,360,15):
    pencolor(colors[angle%6])
    setheading(angle)
    forward(100)
    write(str(angle)+ 'o')
    backward(100)            


# In[1]:


from turtle import *
pencolor('blue')
for i in range(15):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolor('red')
for i in range(90):
    undo()

