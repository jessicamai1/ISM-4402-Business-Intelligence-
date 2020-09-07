#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


pwd


# In[6]:


pd.read_excel("AGE01.xls")


# In[11]:


df.columns = ["Areaname",'STCOU','AGE010180F']
df.head()


# In[12]:


import pandas as pd


# In[7]:


Areanames = ['Autauga', 'Balwin','Barbour', 'Bibb']
STCOU = [00000, 01000, 01003, 01005, 01007, 01009]
StateList = zip(Areanames,STCOU)


# In[3]:


df = pd.DataFrame(data =StateList, columns=['Areaname', 'STCUO'])


# In[4]:


df.to_csv('alabamacounties.csv', index=False,header=False)


# In[ ]:




