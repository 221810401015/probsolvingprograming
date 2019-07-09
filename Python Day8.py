#!/usr/bin/env python
# coding: utf-8

# ### Day Objectives
# * Python data structures
#     -Lists
#     -Tuples
#     -Dictionaries
# * Basic program sets on Data Sructures
# * Advanced Problem Set
# * Contact Application(Dictionary object)
#  
#  Data strucures :
#  
#  .To store , Search and Sort the Data

# ### Python Data Structures
# ### Lists
#  -  It's one of the common data structures supported by python , separated by comma operator and enclosed in square brackets.
#    ex:
#     .list1=[1,8,9,10]
#     .list2=["Gitam",12,30.5,"Hyderabad"]

# In[3]:


lst=[2,5,7,8,9]
print(lst)      #Access the entire list
print(lst[0])  #Access the first list
print(lst[1])  #Access the second item list
print(lst[-1]) 
print(lst[-2]) 
print(lst[-1:])
print(lst[1:4])


# In[5]:


#Update the list item values index (Direct Referening)
li = ["Gitam","Python",1989,2002]
print(li)
li[2]
print(li)


# In[9]:


#delete the specific item in the list
print(li)
del li[2]
print(li)


# In[16]:


# Basic list Operations
lst1 = [1,2,3,4,5,6]
print(len(lst1))  #Len of the list
print(lst*2)      #Repetation
print(9 in lst1)  #list item is present or not
print(5 in lst1)
for x in range (len(lst1)):  #Accessing list item using iteration
    print(lst1[x],end='  ')


# In[23]:


#Function of the list
lst1
print(min(lst1))  # min item/ele in the list
print(max(lst1))  # Max item/ele in the list
print(sum(lst1))  # Sum of all ele in the list
print(sum(lst1)/len(lst1)) # Avg of list ele
print(sum(lst[1::2])/len(lst1[1::2])) # Avg of alternate nos


# In[8]:


lst1
lst1.append(24) # Adding a new element at the end of the list
lst1
lst1.insert(2,56) # Adding an ele at particular index 
lst1
lst1.count(5)  # Return the value how many times the object repeated
lst1.index(56)
lst1.sort()  # Sorts the list in ascending order
lst1
lst1.pop()  #Remove the last ele from the list
lst1
lst1.pop(1)  #Remove an ele from a particular index
lst2 = [123,23,45]
lst1.extend(lst2) # Merge list 2 into list 1
lst1


# In[19]:


lst1 = [3,5,7,9,1]
lst1.reverse()
lst1
lst2 = [11,12,13]
lst1.extend(lst2)
lst1
lst1.remove(11)
lst1


# In[22]:


# Function to find the Second Large item from the list
# Input : [1,19,6,2,8,18,3]
# Output: 18
def SecondLarge(li):
    li.sort()
    return li[-2]
li = [1,19,6,2,8,18,3]
SecondLarge(li)


# In[28]:


# Function to find least item from the list
# Input : [1,19,6,2,8,18,3]
# Output : 2
def secondleast(li):
     li.sort()
     return li[1]
def genericLeast()
li = [1,19,6,2,8,18,3]
secondleast(li)


# ### Searching Agorithm
#  * Linear Search
#  * Binary Search

# ### Linear Search
# - Linear Search algorithm can be applied on Duplicate and Unique List
# - Unique List : All items of the list is appeared only once
# - Duplicate List : The items of the list can be appeared more than once 

# In[38]:


# Function to search the data in a list
# Search is found then return the index if not return -1
def linearSearch1(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            return x
        return -1
li = [1,19,6,2,8,18,3]
linearSearch1(li,100)


# In[43]:


#Function 
#Input : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
#OUTPUT : 1 4 8 
def linearSearch(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            print(x,end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearSearch(li,5)


# In[51]:


#Function
# Input : List
# Output sequence of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 -- !! !!!!!  !!!!!!!!
def linearSearch(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            k = 0
            while k!= x+1:
                print("!",end="")
                k=k+1
            print(end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearSearch(li,5)
            
            


# In[59]:


# Function
# Input : List
# output : Formatted
# Test Case:
# [12,2,45,9,18,15,36] -- 60
# A List item which is perfectly multiple of 3 and 5
def multipleno(li):
    sum=0
    for x in range(len(li)):
        if li[x]%3==0 and li[x]%5==0:
            
            sum=sum+li[x]
    return sum
li = [12,2,45,9,18,15,36]
multipleno(li)
                


# In[3]:


# Function
# Input : List
# Output : Formatted Output
# Test case:
# [1,2,3,4,5] -- [1,3,8,15,5]
# [6,5,2,8,2] -- [6,12,40,4,2]
def linearSearch(li):
    for x in range(len(li)):
        if x==0  or x==len(li)-1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li=[1,2,3,4,5]
linearSearch(li)


# In[10]:


# function
# Input : List
# Output : Formatted Output
# Test Series :
# [1,6,9,4,16,19,22]  == 1 9 19 22
def linearSearch(li):
    for x in range(len(li)):
        if x==0 or x==len(li)-1:
            print(li[x],end=" ")
        elif li[x-1]%2==0 and li[x+1]%2==0:
             print(li[x],end=" ")
    return
li = [1,6,9,4,16,19,22]
linearSearch(li)       


# ### Number to list
# * Input as number
# * Expected ouput will be list

# In[11]:


#Function for Conversuion - Number to list
# Input -- list
# Output -- list
#Test Cases :-
#14569 -- [1,4,5,6,9]
def Conversion(n):
    li = []
    while n!= 0:
        r=n%10
        li.append(r) 
        n=n//10
    li.reverse()
    return li
Conversion(14569)


# # Function to count the occurences of a character in a string
# # "Python Programming", p-->2
# # "Python Programming", m-->2
# def countCharOccurances(s,c):
#     cnt=0
#     for ch in s:
#         if ch == c:
#             cnt+=1
#     return cnt
# def countCharOccurances1(s,c): #both functions gives the same output
#     return s.count(c)
# countCharOccurances("Python Programming",'m')

# ## String To list conversion
# * Input will be string
# * Expected output will be list

# In[17]:


#Functio to convert the string to list
# Test case
# "1 2 3 4 5 6" -- [1,2,3,4,5,6]
def stringtolistconversion(s):
    li = s.split()
    numberslist = []
    for i in li:
        numberslist.append(int(i))
    return numberslist
s = "1 2 3 4 5 6"
stringtolistconversion(s)


# ### Sorting Algorithms:
# * Bubble Sort
# * selection Sort
# * Insertion Sort

# ### Bubble Sort:
# * this algorithm compares the adj elements,if the first element is       greater
# * than second element then its required to swap the elements
# 

# In[19]:


#Function to represent the bubble sort
def bubbleSort(li):
     for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
        return li
li = [19,1,25,6,18,3]
bubbleSort(li)

