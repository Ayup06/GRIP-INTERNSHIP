#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Importing libraries"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


""" Importing the csv file , reading it , cleaning it and analysing it"""
df = pd.read_csv("movies.csv")
print(df.info())
'dataset has 7668 rows'
print(df.head(10))
# Analysis of numerical values
df1 = df.describe().T
print(df1)


# In[3]:


# deleting rows with empty cells
df.dropna(inplace=True)
print(df.info())
'After deleting empty cells , remanining number of rows are 5421'


# In[4]:


# Changing data type of columns
df["score"] = df["score"].astype("int64")
df["votes"] = df["votes"].astype("int64")
df["budget"] = df["budget"].astype("int64")
df["gross"] = df["gross"].astype("int64")
df["runtime"] = df["runtime"].astype("int64")
print(df.info())


# In[5]:


"""Visual representaion of Genre and rating"""
sns.countplot(data=df, x='rating', hue='genre')
plt.legend(loc="upper right")
plt.title("Genre v/s Ratings")
plt.show()
'no. of counts of genre w.r.t ratings'


# In[6]:


"""Visual representaion of Gross and budget"""
plt.scatter(df.budget, df.gross)
plt.title("Budget v/s Gross")
plt.xlabel("Budget")
plt.ylabel("Gross")
plt.show()
'The scatter graph concludes that as budget increases gross also increase'
'low budget movies have low profits'


# In[13]:


"""Visual representation of year and country"""
plt.bar(df.year, df.country)
plt.title("Year v/s Country")
plt.xlabel("Year")
plt.ylabel("Country")
plt.show()
'This graph shows in which countries the movies were released w.r.t Year '


# In[14]:


"Visual representation of country and runtime of movies"
plt.barh(df.country, df.runtime)
plt.xlabel("Country")
plt.ylabel("Runtime")
plt.title("Country v/s Runtime")
plt.show()
'highest runtime of movies is in United states and lowest runtime is in Israel'

