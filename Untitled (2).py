#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Location = "datasets/gradedata.csv" 


# In[3]:


df = pd.read_csv(Location)
df.head()


# In[4]:


bins = [0, 60, 70, 80, 90, 100]
group_names = ['Fail', 'Fail', 'Fail', 'Pass', 'Pass']


# In[5]:


df['PassOFail'] = pd.cut(df['Pass'], bins,labels=group_names)
df


# In[ ]:


pd.value_counts(df['PassOrFail'])

