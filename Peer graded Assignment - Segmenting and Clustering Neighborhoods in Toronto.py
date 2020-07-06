#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

get_ipython().system('conda install -c conda-forge geopy --yes ')
# uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library


# In[13]:


# import the library we use to open URLs
import urllib.request


# In[14]:


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'


# In[15]:


# open the url using urllib.request and put the HTML into the page variable
page = urllib.request.urlopen(url)


# In[16]:


# import the BeautifulSoup library so we can parse HTML and XML documents
from bs4 import BeautifulSoup

# parse the HTML from our URL into the BeautifulSoup parse tree format
soup = BeautifulSoup(page, "lxml")


# In[17]:


print(soup.prettify())


# In[18]:


# use the 'find_all' function to bring back all instances of the 'table' tag in the HTML and store in 'all_tables' variable
all_tables=soup.find_all("table")
all_tables


# In[19]:


right_table=soup.find('table', class_='wikitable sortable')
right_table


# In[20]:


#we will set up 3 empty lists to store our data in 

A=[]
B=[]
C=[]

#To start with, we want to use the Beautiful Soup ‘find_all’ function 
#again and set it to look for the string ‘tr’. We will then set up a FOR 
#loop for each row within that array and set Python to loop through the rows,
#one by one.

##Within the loop we are going to use find_all again to search each row for
#<td> tags with the ‘td’ string. We will add all of these to a variable
#called ‘cells’ and then check to make sure that there are 5 items in our 
#‘cells’ array (i.e. one for each column).

#If there are then we use the find(text=True)) option to extract the content
#string from within each <td> element in that row and add them to the A-c
#lists we created at the start of this step. Let’s have a look at the code


     
for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==3:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        
       


# In[44]:


#let's now convert into a Pandas datframe.We will assign each of the lists 
#A-C into a column with the name of our source table columns.

df=pd.DataFrame()
df['Postal Code']=A
df['Borough']=B
df['Neighborhood']=C

df



# In[45]:


#Let's get rid of the \n into each value

df = df.replace(r'\n',  ' ', regex=True)
df


# In[55]:


# replace "Not aSSIGNED VALUES WITH NaN"
df = df.replace('Not assigned',np.nan, regex=True)
df.head()

# Drop Rows in which there are na for borough
df.dropna(subset=["Borough"], axis=0, inplace=True)
df = df.reset_index(drop=True)
df.head(11)


# In[54]:


#number of rows and columns of the dataframe

df.shape


# In[ ]:





# In[ ]:





# In[ ]:




