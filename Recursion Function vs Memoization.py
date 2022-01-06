#!/usr/bin/env python
# coding: utf-8

# Let's write a fibonacci function

# Fibonacci numbers is a special numbers series. Each number is the sum of two previous ones. 
# * 0  1  1  2  3  5  8  13  21  34  55  89 ...
# 
# F(0) = 0, F(1) = 1, F(2) = F(0) + F(1), F(3) = F(2) + F(1), ...
# 
# **Recursion** means defining something in terms of itself

# In[23]:


def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        result = fibo(x-1) + fibo(x-2)
        return result    


# In[6]:


fibo(0)


# In[7]:


fibo(1)


# In[8]:


fibo(2)


# In[9]:


fibo(3)


# In[10]:


fibo(4)


# In[11]:


fibo(5)


# In[12]:


fibo(10)


# In[13]:


fibo(20)


# In[14]:


fibo(30)


# In[21]:


fibo(38)


#  Depends on your computer, after fibo(38) you could need to interupt kernel. Because it will be very though to execute function :)

# How can we solve this problem? The answer is **"memoization"**

# In[28]:


memory = {}

def fibo_mem(x,memory=memory):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    if x-1 not in memory:
        memory[x-1] = fibo_mem(x-1)
    if x-2 not in  memory:
        memory[x-2] = fibo_mem(x-2)
    return memory[x-1] + memory[x-2]


# In[29]:


fibo_mem(3)


# In[30]:


fibo_mem(38)


# In[31]:


fibo_mem(100)


# Let's calculte the number of functions and time between fibo and fibo_mem

# In[39]:


counter_fibo = {'execution_num':0}

def fibo(x):
    counter_fibo['execution_num'] += 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        result = fibo(x-1) + fibo(x-2)
        return result  


# In[40]:


get_ipython().run_cell_magic('time', '', 'print(fibo(38))\nprint(counter_fibo)')


# In[43]:


memory = {}
counter_fibo_mem = {'execution_num':0}

def fibo_mem(x,memory=memory):
    counter_fibo_mem['execution_num'] += 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    if x-1 not in memory:
        memory[x-1] = fibo_mem(x-1)
    if x-2 not in  memory:
        memory[x-2] = fibo_mem(x-2)
    return memory[x-1] + memory[x-2]


# In[44]:


get_ipython().run_cell_magic('time', '', 'print(fibo_mem(38))\nprint(counter_fibo_mem)')


# **Number of execution decreased dramatically and it executes immediately !**
