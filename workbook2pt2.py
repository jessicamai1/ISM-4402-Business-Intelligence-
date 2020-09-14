#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine


# In[6]:


db_file = r'datasets/weekly_call_data.db'
engine = create_engine(r"sqlite:///{}"
                       .format(db_file))


# In[8]:


sql = 'SELECT * from test'
    'where DayOfWeek in ("mon","tues","wed")'
weekly_call_data_df = pd.read_sql(sql, engine)
weekly_call_data_df


# In[12]:


sql = "select name from sqlite_master"
"where type = 'table';"


# In[ ]:




