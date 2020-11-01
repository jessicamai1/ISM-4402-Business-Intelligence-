#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 


# In[2]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/gradedata.csv"


# In[3]:


df = pd.read_csv(Location) 
df.head()


# In[4]:


df.hist()


# In[5]:


df.hist(column="age")


# In[6]:


df.hist(column="hours", by="gender")


# In[ ]:




