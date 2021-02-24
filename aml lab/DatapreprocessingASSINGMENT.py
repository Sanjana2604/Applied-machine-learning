#!/usr/bin/env python
# coding: utf-8

# import libraries

# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset

# In[20]:


dataset=pd.read_csv('bestsellers.csv')


# show dataset

# In[21]:


dataset


# In[22]:


np.shape(dataset)


# independent data

# In[23]:


X = dataset.iloc[:, :-1].values
X


# dependent data

# In[24]:


y = dataset.iloc[:,6].values


# In[25]:


y


# Filling the missing data

# In[26]:


from sklearn.impute import SimpleImputer
imputer=SimpleImputer (missing_values=np.nan,strategy='mean')
imputer=imputer.fit(X[:,2:4])
X[:,2:4]=imputer.transform(X[:,2:4])


# In[27]:


X


# In[28]:


from sklearn.impute import SimpleImputer
imputer=SimpleImputer (missing_values=np.nan,strategy='median')
imputer=imputer.fit(X[:,2:4])
X[:,2:4]=imputer.transform(X[:,2:4])
X


# In[29]:


from sklearn.impute import SimpleImputer
imputer=SimpleImputer (missing_values=np.nan,strategy='constant')
imputer=imputer.fit(X[:,2:4])
X[:,2:4]=imputer.transform(X[:,2:4])


# In[30]:


X


# In[31]:


from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])


# In[32]:


X


# In[33]:


labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# In[34]:


y


# In[ ]:




