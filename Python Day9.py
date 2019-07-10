#!/usr/bin/env python
# coding: utf-8

# ### Data Structures
# * Dctionaries

# ### Dictionaries
# * It works on the concept of Set Unique Data
# * Keys,Values is the unique identifier for a value
# * Each key is separated from its value with colon(:)
# * Each key and value is separated by comma(,)
# * Dictionaries enclosed with Curly braces({})
# 

# In[1]:


d1 = {"Name":"Gitam","Emailid":"gitam@gmail.com","Address":"Hyderabad"}
print(d1)


# In[2]:


d1["Name"] # Access the specific key


# In[3]:


d1["Emailid"] = "Gitam-Python@gmail.com"


# In[4]:


d1


# In[5]:


del d1["Emailid"] # Delete the specific key value


# In[6]:


d1 # del d1 will delete the entire dict object


# In[7]:


d1.keys() #Returns the list of keys


# In[8]:


d1.values()


# In[9]:


d1.items() #returns the list of tuples of keys and values 


# ### Tuples
# * t1 paranthesis() li square brackets[]
# * Difference between list and tuples
#   * lists are mutable - can be changed/modified
#      - used to access modify , Add , delete data
#   * Tuples are immutable - cannot be changed 
#      - used to access data only

# In[10]:


t1 = (1,2,3,4,5,6)
t1
type(t1)


# ### Contact Application
# * Add Contact
# * search the contact
# * List all contacts
#     - name1 : phone1
#     - name2 : phone2
# * Modify the contact
# * Remove the contact
# * Import the Contact

# In[16]:


#Add contact
contacts = {} # Creating a dict object
def addContact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("Contact details are added")
    else:
        print("Contact details are alredy exists")
    return
addContact('Ferrari','123456')
addContact('Audi','789456')
addContact('Bugatti','456789')
addContact('Bugatti','456789')


# In[18]:


# Search for Contact details
def searchContact(name):
    if name in contacts:
        print(name," : " , contacts[name])
    else:

        print("%s does not exists" % name)
    return
searchContact('Ferrari')
searchContact('Vinay')


# In[19]:


# Import some Contacts
# Merge Contacts with existing ones
def importContact(newContacts):
    contacts.update(newContacts)
    print(len(newContacts.keys()),"Contacts added successfully")
    return
newContacts = {'Vinay':556699 , 'Vignesh':778899}
importContact(newContacts)


# In[22]:


#Delete a Contact 
def deleteContact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted Successfuly")
    else:
            print(name,"not exists")
    return
deleteContact('Audi')


# In[23]:


# Update the contact details
def deleteContact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"Updated successfully")
    else:
        print(name,"Not exits")
    return
deleteContact('Audi',789456)
deleteContact('Bugatti',456789)


# ### Strings

# In[2]:


# Classical Version
li = ["python","Programming"]
print("%s %s "% (li[0],li[1]))


# In[7]:


print("{0} {1}".format(li[0] , li[1]))


# In[6]:


li1 = [1,2,3,4]
print("%d %d %d %d " % (li1[0],li1[1],li1[2],li1[3]))


# In[10]:


print("{0} {1} {2} {3}".format(li1[0],li1[1],li1[2],li1[3]))


# ### Boolean Function (True and False)
# * islower() -- True if the string is lowercase/False if the string not in lowercase
# * isUpper() -- True if the string in uppercase/False if the string not in upper case
# * istitle() -- True if the string follows title case/False
# * isalpha() -- True if the string contains only alphabets / False
# * isnumeric() -- True if the string contains only numbers / False
# * isspace() --  True if the string contains only spaces / False

# In[11]:


s1 = 'GITAM'
print(s1.islower())
print(s1.isupper())


# In[13]:


s2 = "Python Programming"
s3 = "python programming"
print(s2.istitle())
print(s3.istitle())


# In[15]:


s2 = "Application45612"
s3 = 'PythonProgramming'
print(s2.isalpha())
print(s3.isalpha())


# In[16]:


s1 = "12345"
s2 = "123Aplicaton"
print(s1.isnumeric())
print(s2.isnumeric())


# In[18]:


s1 = " "
s2 = "Py th on"
print(s1.isspace())
print(s2.isspace())


# ### String methods
# * 1.join() -- Method will concatenates two strings
# * 2.split() -- returns list of strings separated by whitespaces
# * 3.replace() -- replaces the specific word/character with a new word/character 
# 

# In[21]:


s1 = 'Python'
print(" ".join(s1))


# In[23]:


s2 = "Python Programming Easy to learn"
print(",".join(s2))


# In[25]:


li = ['Python','Programming','Learn']
print(",".join(li))


# In[28]:


s2 = "Python Programming Easy to learn"
print(s2.split())


# In[30]:


s2 = "Python Programming Easy to learn"
print(s2.split('a'))


# In[31]:


s2 = "Python Programming Easy to learn"
li = s2.split()
print(li)
print(len(li))


# In[32]:


s2 = "Python Programming Easy to learn"
li=list(s2)
print(li)


# In[33]:


s2 = "Python Programming Easy to learn"
print(s2.replace("gra","Application"))


# ### Packages and Modules
# 
# * Packages
#     - A collection of Modules(Single Python file .py) and subpackages
# * Module
#     - A single Python c=file containing set functions
#  
# Packages --> Sub Packages -->Modules -->Functions -->Statements
# 
# 

# In[1]:


# Import the externals packages to python file
import math
math.floor(123.45)


# In[2]:


from math import factorial as fact
fact(7)


# In[ ]:




