#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Location = "datasets/gradedata.csv"


# In[4]:


df = pd.read_csv(Location)


# In[5]:


df.head()


# In[6]:


import numpy as np


# In[8]:


df['timemgmt'] = np.where(df['excercise']<3,'yes', 'no')


# In[9]:


df.tail(10)


# In[10]:


df['timemgmt'] = np.where((df['excersise']<3)
     & (df['studyhours'] == '17'),'yes', 'no')


# In[11]:


df.tail(10)


# In[ ]:




