#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


Location = "datasets/gradedata.csv"


# In[4]:


df = pd.read.csv(Location)
df.head()


# In[6]:


df = df.sort_values(by= 'name', ascending=a )
df.head()


# In[ ]:


df.=df.sort_values(by=['name','age', 'grade'])
        ascending=[True, True, True]
df=head()

