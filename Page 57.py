#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[8]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList,
 columns=['Names','Grades','BS Degrees','MS Degrees','PHD Degrees'])
df


# In[9]:


df['Grades'].count() # number of values
df['Grades'].mean() # arithmetic average
df['Grades'].std() # standard deviation
df['Grades'].min() # minimum
df['Grades'].max() # maximum
df['Grades'].quantile(.25) # first quartile
df['Grades'].quantile(.5) # second quartile
df['Grades'].quantile(.75) # third quartile


# In[10]:


# computes the arithmetic average of a column
# mean = dividing the sum by the number of values
df['Grades'].mean()
# finds the median of the values in a column
# median = the middle value if they are sorted in order
df['Grades'].median()
# finds the mode of the values in a column
# mode = the most common single value
df['Grades'].mode()


# In[11]:


# computes the variance of the values in a column
df['Grades'].var()


# In[12]:


df.var()


# In[ ]:




