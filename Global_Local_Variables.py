#!/usr/bin/env python
# coding: utf-8

#  A variable outside of the function or in a global scope is called "global"

# In[76]:


x = "ahmet"

def first_function(x):
    
    print('before function:',x)
    x = x.replace(x, "caliskan")
    print ('after function:',x)
    
first_function(x)

print('x:',x)


# * We could not replace the global variable 'x'. Even we used the global variable 'x' inside a function, global variable is still same after the function.

# * What if we use a variable only inside a function?

# In[45]:


def second_function():

    y = "umit"
    print('before function:',y)
    y = y.replace(y, "caliskan")
    print ('after function:',y)
    
second_function()

print('y',y)


# * As you see above, we got a NameError: "y" is  not defined. Because "y" is a local variable. This means we can only use local variable inside a function

# * How can we change a global variable?

# In[72]:


z = "caliskan"


# In[73]:


def third_function():
    global z
    print('before function:',z)
    z = x + z
    print('after function:',z)
    
third_function()

print('z:',z)


# * z is a global variable. If we want to change a global variable we have to indicate it as "global" variable to the python. 

# In[ ]:




