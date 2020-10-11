#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


Location = "datasets/gradedata.csv"


# In[4]:


df = pd.read_csv(Location)
df.tail()


# In[6]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:




