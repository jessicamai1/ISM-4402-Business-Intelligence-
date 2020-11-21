#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


Location = "axisdata.csv"


# In[3]:


df = pd.read_csv(Location)


# In[4]:


df.head()


# In[6]:


#average cars sold
df['Cars Sold'].mean()


# In[7]:


#max cars sold 
df['Cars Sold'].max()


# In[8]:


#min cars sold 
df['Cars Sold'].min()


# In[9]:


#Average cars sold per month by gender 
pd.pivot_table(df, 
        values=['Cars Sold'],
        index=['Gender'])


# In[15]:


#Average hours worked by people selling more than three cars per month 
df2 = df.loc[df['Cars Sold'] > 3]
pd.pivot_table(df2,
               index=['Fname'],
               aggfunc='mean',
               values=['Cars Sold','Hours Worked'])


# In[17]:


#Average years of experience 
df['Years Experience'].mean()


# In[18]:


#Average years of experience for people selling more than three cars per month 
df2 = df.loc[df['Cars Sold'] > 3]
pd.pivot_table(df2,
               index=['Fname'],
               aggfunc='mean',
               values=['Cars Sold','Years Experience'])


# In[27]:


#Average cars sold per month sorted by whether they have had sales training
df = df.sort_values(by=['Cars Sold', 'SalesTraining'], 
        ascending=[False, False])
df.head()


# In[ ]:




