#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')


# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas as pd 
import re


# In[11]:



url = 'https://www.imdb.com/find?q=2021%20movies&s=tt&ref_=fn_al_tt_mr'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


# In[5]:



titles = [] 
for h3 in soup.find_all('h3'):
  titles.append(h3.string.strip())

ratings = []
for rating in soup.select('span.rating'):
  ratings.append(rating.string.strip())

lengths = []
for length in soup.select('span.length'):
  lengths.append(length.string.strip())

years = []
for year in soup.select('span.year'):
  years.append(year.string.strip())

 
with open('top100', 'w') as file:
    writer = csv.writer(file, delimiter=',')


# In[6]:


import pandas as pd 
pd.DataFrame({})
  writer.writerow(["title", "ratings",  "year"])
    for i in range(100):
    writer.writerow([
      titles[i], 
      ratings[i], 
      lengths[i], 
      years[i], 
      
    ])


# In[ ]:




