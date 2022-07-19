#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler

from scipy import stats
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("C:/Users/arvin/OneDrive/Desktop/COVID19/country_wise_latest.csv")
df.head()


# In[3]:


df2=pd.read_csv("C:/Users/arvin/OneDrive/Desktop/COVID19/full_grouped.csv",parse_dates=["Date"])
df2.head()
df2.sort_values(by=["Confirmed"],ascending=False)


# In[4]:


df1=pd.read_csv("C:/Users/arvin/OneDrive/Desktop/COVID19/covid_19_clean_complete.csv", parse_dates=['Date'])
df1.head()


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.describe(include="all")


# In[9]:


df.isnull().sum()


# In[10]:


grouped=df[["Confirmed","Deaths","Recovered","Country/Region"]]
grouped.head()


# In[11]:


import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px


# In[12]:


fig=px.bar(grouped,y="Confirmed",x="Country/Region",title="Country having Highest CASES")

fig.show()


# In[13]:



fig=px.bar(grouped,x="Country/Region",y="Deaths",title="Countries Having Highest Deaths", color_continuous_scale="Brand")
fig.show()


# In[14]:


x=grouped.sort_values(by="Confirmed",ascending=False)

px.bar(x[0:11],x="Country/Region",y="Confirmed",title="Top Countries")


# In[15]:


px.bar(x[0:11],x="Country/Region",y="Deaths",title="Top Countries with Deaths")


# In[16]:


grouped["Date"]=df2.Date
grouped.head()


# In[17]:


grouped.set_index("Date")
grouped.head()


# In[18]:


grouped["TOTAL"]=grouped["Confirmed"]+grouped['Deaths']+grouped["Recovered"]
grouped.head()


# In[19]:


px.pie(x[0:11],values="Confirmed",names="Country/Region")


# In[20]:


date_c = df1.groupby('Date')['Date', 'Confirmed', 'Deaths',"Lat","Long","Country/Region"].sum().reset_index()
date_c.head()


# In[21]:


px.scatter(date_c,x="Date",y="Confirmed",title="WORLD WIDE Confirmed Cases ")


# In[22]:


px.line(date_c,x="Date",y="Deaths",title="WORLD WIDE DEATHS")


# In[23]:


px.line(df1,x="Date",y="Recovered",title="Wolrd Wide Recovered")


# In[ ]:





# In[ ]:




