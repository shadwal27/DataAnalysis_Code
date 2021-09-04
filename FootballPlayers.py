#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df_players=pd.read_csv('C:/Users/shadw/Downloads/archive (1)/football_players.csv')


# In[7]:


df_players.head()


# In[16]:


df_players['From(Country)'].unique()


# In[17]:


sns.countplot('From(Country)',data=df_players)


# In[25]:


df_players[df_players["From(Country)"] == "Spain"]


# In[ ]:




