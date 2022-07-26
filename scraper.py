#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
import pandas as pd


# In[2]:


from bs4 import BeautifulSoup


# In[4]:


response = requests.get("https://www.bbc.com")
doc = BeautifulSoup(response.text)


# In[12]:


# select links inside class of .media__title
titles = doc.select(".media__title a")
titles


# In[19]:


rows = []

for title in titles:
    row = {}
    row['title'] = title.text.strip()
    row['url'] = title['href']
    rows.append(row)
    
df = pd.DataFrame(rows)


# In[20]:


df.to_csv("bbc.csv", index=False)


# In[21]:





# In[ ]:




