#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv" 


# In[2]:


df = pd.read_csv(Location) 
df.head()


# In[3]:


import statsmodels.formula.api as sm


# In[5]:


result = sm.ols(
    formula='grade ~ age + exercise + hours',
    data=df).fit()
result.summary()


# In[6]:


import statsmodels.formula.api as sm


# In[7]:


result = sm.ols(
    formula='grade ~ exercise + hours',
    data=df).fit() 
result.summary()


# In[8]:


import statsmodels.formula.api as sm


# In[11]:


result = sm.ols(
    formula='female'= 1,'male'=0
    data=df).fit() 
result.summary()


# In[ ]:




