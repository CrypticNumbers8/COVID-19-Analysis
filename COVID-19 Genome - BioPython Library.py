#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np # linear algebra
import pandas as pd # pd.read_csv

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
import matplotlib.pyplot as plt


# In[33]:


from Bio.Seq import Seq


# In[35]:


with open ("C:/Users/arvin/OneDrive/Desktop/COVID19-Genomes/MZ359839.txt", "r") as myfile:
    MZ359839=myfile.read().replace('\n', '').replace('\ufeff', '').replace("ï»¿","")


# In[ ]:





# In[36]:


MZ359839
#Complete Genomic Sequence of file MZ359839


# In[39]:


my_seq = MZ359839


# In[40]:


len(my_seq)
#Total length of the sequence


# In[41]:


my_seq.count("A")
#Occurence of Adenine


# In[ ]:





# In[42]:


my_seq.count("C")
#Occurence of Cytosine


# In[25]:


my_seq.count("T")
#Occurence of Thymine


# In[43]:


from Bio.SeqUtils import GC
GC(my_seq)


# In[44]:


from Bio import SeqIO
import pylab


# In[ ]:





# In[45]:


max(my_seq) 


# In[46]:


min(my_seq)


# In[48]:


x = ['A','T','C','G']
y = [my_seq.count("A")
,my_seq.count("T")
,my_seq.count("C")
,my_seq.count("G")]
plt.bar(x,y, color = 'green')
plt.show()

