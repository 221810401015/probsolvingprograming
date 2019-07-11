#!/usr/bin/env python
# coding: utf-8

# ### Standard Libraries
# * File I/O
# * Regular Expression
# * Datatime
# * Math (numerical and mathematical)

# ### Write,Read,Analysis --Data Sciences ansd Analysis

# ### File Handling in Python
# * File:-Document containing information resides on the permanent storage
# * Different types of files :- txt,doc,pdf,csv and etc...
# * Input -- Keyword
# * Output -- File
# ### Modules of the file I/O
# * 'w' -- This mode is used to file writing
#     
#     -- If the file is not present first it creates the file and write so me data to it
#     -- If the file is already present it rewrites the previous content 

# In[1]:


#Function to create a file and write to a file
def createFile(filename):
    f = open(filename,'w')
    for i in range (10):
        f.write('This is %d Line\n' % i)
        print("File is created and data has written")
        return
createFile('file1.txt')


# In[2]:


ls


# In[3]:


import os
cat file1.txt


# In[ ]:


def createFile(filename):
    f = open(filename,'w')
    f.write('Testing...\n')
    print("File is created and data has written")
    return
createFile('file1.txt')


# In[ ]:


def appendData(filename):
    f = open(filename,'a')
    for i in range (10):
        f.write('This is %d Line\n' % i)
    print("File is created and data has written")
    return
appendData('file2.txt')
    


# In[ ]:


def appendData(filename):
    f = open(filename,'a')
    f.write("New line 1 \n")
    f.write("New line 1 \n")
    print("File is created and data has written")
    return
appendData('file2.txt')
    


# In[ ]:


# Function to ead of the file
def readFileData(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close()
    return
readFileData('file2.txt')


# In[ ]:


#Function to read the file
def fileOperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode == 'a':
            f.write('Data to the file')
            print('the data successfully written')
    f.close()
    return
filename = input('Enter the filename')
mode = input('Enter the mode of the file')
fileOperations(filename,mode)


# In[ ]:


# Data Analysis
# Word count Program
def wordCount(filename,word):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split()    #it Splits the string with whitespace
    cnt = li.count(word)
    return cnt
filename = input('Enter the filename')
word = input('Enter the word : ')
wordCount(filename,word)


# In[ ]:


# Character count from the given file
def wordCharacter(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    return len(li)
filename = input('Enter the filename : ')
wordCharacter(filename)


# In[ ]:


# Function to find the no of lines in the input list
# Input -- filename(file2.txt)
# output -- 12
def nooflines(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = x.split("\n")
            return len(li)
filename = input('Enter the filename : ')
nooflines(filename)


# In[ ]:


# Function to print the upper and lower case characters
def caseCount(filename):
    cntUpper = 0
    cntLower = 0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    for i in li:
        if i.isupper():
            cntUpper += 1
        elif i.islower():
            cntLower += 1
    output = 'Upper Case = {0} , Lower Case = {1}'.format(cntUpper,cntLower)
    return output
filename = input('Enter the filename : ')
caseCount(filename)
    


# ### math,random,os
# * os package it contains the certain methods which work with OS

# In[18]:


ls


# In[20]:


cd mpilab


# In[21]:


cd desktop


# In[22]:


cd probsolvingprograming


# In[23]:


import os 
os.listdir('Git/')


# In[24]:


li = os.listdir('Git/')
for i in li:
    print(i)


# ### 
# * Older version python -- os.listdir
# * New Version Python -- os.scandir() and pathlib.Path()

# In[25]:


li = os.scandir('Git/')
for i in li:
    print(i)


# In[26]:


from pathlib import Path
li = Path('Git/')
for i in li.iterdir():
    print(i.name)


# ### Listing all files in a dictionary
# 

# In[27]:


import os
dirPath = "git/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)


# ## Listing SubDirectories
# 

# In[34]:


dirPath = 'git/'
for i in os.listdir(dirPath):
    if os.path.isdir(os.path.join(dirPath,i)):
        print(i)
    


# In[35]:


from pathlib import Path
dirPath=Path('git/')
for i in dirPath.iterdir():
    if i.is_dir():
        print(i.name)


# In[41]:


dirPath = 'git/'
with os.scandir(dirPath) as f:
     for i in f:
            if i.is_dir():
                print(i.name)


# ### Creating a Single Directory

# In[42]:


import os
os.mkdir('single directory')


# In[43]:


import pathlib
p=pathlib.Path('TestFolder')


# In[44]:


ls


# ## Creating multiple Directories

# In[45]:


import os
os.makedirs('2019/july/11')


# In[46]:


ls


# ## Filename Pattern Matching

# In[53]:


cd probsolvingprograming


# In[54]:


import os
dirPath = 'git/'
for f_name in os.listdir(dirPath):
    if f_name.endswith('.ipynb'):
        print(f_name)


# In[55]:


import os
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.startswith('da'):
        print(f_name)


# ## Deleting files and Directories

# In[56]:


ls


# In[57]:


cd git


# In[58]:


import os
data_file = 'file1.txt'
os.remove(data_file)


# In[61]:


data_dir = 'TestFolder'
os.rmdir(data.dir)


# In[60]:


cd ..


# ###  Regular Expressions
# * Used to specific pattern matching
# * Symbolic notations of Pattern

# In[ ]:




