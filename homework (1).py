#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_csv("datasets/gradedatamissing.csv")
df.head()


# In[2]:


names = ['Marcia','Kadeem','Nash','Noelani','Noelani']
grades =[-1,78.2,-1,83.2,87.4]


# In[3]:


Gradelist = zip(names,grades)
df = pd.DataFrame(data = GradeList,
    columns=['Names', 'Grades'])
df


# In[5]:


df.loc[df['Grades'] <= 100]


# In[6]:


df.loc[(df['Grades'] >= 100,'Grades')] = 0


# In[ ]:




