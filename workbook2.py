#!/usr/bin/env python
# coding: utf-8

# In[2]:


path_to_zip_file = "datasets.zip"
directory_to_extract_to = ""

import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[54]:


import pandas as pd
DayOfWeek = ["mon","tues","wed","thurs"] 
TimeOfDay = ["10:30","11:24","15:43","13:44"]
CallDuration = ["20","10","17","2"]
CallList = zip(DayOfWeek,TimeOfDay)
df = pd.DataFrame(data = CallList,
                  columns=['DayOfWeek','TimeOfDay'])
writer = pd.ExcelWriter('dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[47]:


import pandas as pd
import numpy as np
import glob


# In[59]:


all_data = pd.DataFrame()
for f in glob.glob("Desktop/datasets/weekly_call_data/weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()


# In[ ]:




