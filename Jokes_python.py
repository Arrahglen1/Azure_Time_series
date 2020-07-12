#!/usr/bin/env python
# coding: utf-8

# In[3]:


from random import randint

jokes = ["I'm so pretty", "Nice game", "OMG", "LOL", "White Elephant", "Check this sequence", 
         "Safe journey", "holala", "I'm so cute", "All star game","Hey Baldy","Not so fuuny"]
for i in range(10):
    
  print(jokes[randint(0,11)])

#print(jokes[randint(0, len(jokes)-1)])

  


# In[2]:


jokes = ["I'm so pretty", "Nice game", "OMG", "LOL", "White Elephant", "Check this sequence", 
         "Safe journey", "holala", "I'm so cute", "All star game","Hey Baldy","Not so fuuny"]

 

from random import randint

# the length of the list is given by len and the list has 10 elements indexed from 0 to 9
length_of_the_jokes_list = len(jokes) 

# randint generates random integer from the start to the end inclusive that is randint(start, end)
random_from_0_to_10 = randint(0, 10)

# to get an index that will fall within the range of the list that can be indexed
random_list_index = randint(0, len(jokes)- 1)

# to get an element of a list l at index i ==> l[i]
random_joke = jokes[random_list_index]

# loop ten times to print 10 random jokes here range generates int from 0 to 10 exlusive 
    
# in one shot it gives
for i in range(10):
    print(jokes[randint(0, len(jokes)-1)])


# In[4]:


# main fidonacci number
def fibonacci(n):
    if(n < 2):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


# In[10]:


# fibonacci number as a sequence 
def listFibo(n):
    if(n < 1):
        return [n]
    else:
        return listFibo(n-1) + [fibonacci(n)]

 

print("recursive fibonacci sequence")
print(listFibo(11))
print("------------------------------------------------------\n")

 

print("iterative fibonacci sequence")


# In[12]:


# display fibo number through loup (recommended for beginner)
for i in range(12):
    print(fibonacci(i))


# In[ ]:




