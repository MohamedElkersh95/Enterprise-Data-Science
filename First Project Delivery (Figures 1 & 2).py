#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')

import missingno as msno

import plotly.express as px

pd.set_option('display.max_rows', 5000)


# # 1-Total COVID-19 Cases (per Population Size) over Time

# ## Loading the Data Set for Visualization 

# ### Data Source:
# 
# Our World in Data: https://ourworldindata.org/ 

# In[2]:


url="https://covid.ourworldindata.org/data/owid-covid-data.csv"


# In[3]:


country_info=pd.read_csv(url,sep=',')


# In[4]:


country_info


# In[5]:


country_info.columns


# In[6]:


country_info.head(6)


# In[7]:


country_info['location']


# In[8]:


country_info['location'].unique()


# In[9]:


country_info['location']=='Germany'  #False Here


# In[10]:


country_info[country_info['location']=='Germany']     #True Here


# In[11]:


DE=country_info[country_info['location']=='Germany']  


# In[12]:


DE


# In[13]:


DE.reset_index()


# In[14]:


DE.reset_index(drop=True)


# In[15]:


DE=DE.reset_index(drop=True)


# In[16]:


DE.columns     


# In[17]:


msno.matrix(DE)


# In[18]:


msno.matrix(DE[['iso_code', 'continent', 'location', 'date', 'total_cases', 'new_cases',
       'new_cases_smoothed', 'total_deaths', 'new_deaths',
       'new_deaths_smoothed', 'total_cases_per_million',
       'new_cases_per_million', 'new_cases_smoothed_per_million',
       'total_deaths_per_million', 'new_deaths_per_million',
       'new_deaths_smoothed_per_million', 'reproduction_rate']])


# # Focus is on Total COVID-19 Cases

# ## Visualization: Line Chart Plotting

# In[19]:


DE.head(6)


# In[20]:


fig = px.line(DE, x="date", y="total_cases", title='Total COVID-19 Cases')
fig.show()


# In[21]:


DE.columns      #Data includes Total Cases and Population Number


# In[22]:


DE['total_cases']


# In[23]:


DE['population']


# In[24]:


DE['total_cases']/DE['population'] 


# In[25]:


DE['total_cases']/83900471    #As scalar division


# In[26]:


b_DE=country_info['location']=='Germany'


# ## Visualization for 3 Countries
# 
# * United States
# * Germany
# * Egypt

# In[27]:


b_US=country_info['location']=='United States'
b_DE=country_info['location']=='Germany'
b_UK=country_info['location']=='United Kingdom'


# In[28]:


sum(b_DE) #Rows


# In[29]:


sum(b_US&b_DE&b_UK) # AND operator - Multiplication of 1s & 0s, Since they are in different rows, always=0


# In[30]:


sum(b_US|b_DE|b_UK) #OR operator


# In[31]:


b_all=b_US|b_DE|b_UK


# In[32]:


my_list=country_info[b_all]


# In[33]:


my_list


# In[34]:


fig = px.line(my_list, x="date", y="total_cases", color='location', title='Total COVID-19 Cases')
fig.show()


# ### Including the Population Number

# In[35]:


my_list['total_cases_norm']=my_list['total_cases']/my_list['population']


# In[36]:


fig = px.line(my_list, x="date", y="total_cases_norm", color='location', title='Total COVID-19 Cases per Population Size')
fig.show()


# # 2-Vaccination Rates (Percentage of Population) over Time 

# ## Loading the Data Set for Visualization 

# ### Data Source:
# 
# GitHub Data

# In[37]:


data_path='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'


# In[38]:


vacc_info=pd.read_csv(data_path,sep=',')


# In[39]:


vacc_info


# In[40]:


vacc_info.columns


# In[41]:


vacc_info.head(6)


# In[42]:


vacc_info['location']


# In[43]:


vacc_info['location'].unique()


# In[44]:


DE=vacc_info[vacc_info['location']=='Germany']


# In[45]:


DE


# In[46]:


DE.reset_index(drop=True)


# In[47]:


DE=DE.reset_index(drop=True)


# In[48]:


DE.columns  


# In[49]:


msno.matrix(DE)      #Perfect


# # Focus is on People Fully-Vaccinated

# ## Visualization: Line Chart Plotting

# In[50]:


DE.head(6)


# In[51]:


DE.columns    # Information on People Fully-Vaccinated as Percentage of Population is available


# In[52]:


DE['people_fully_vaccinated'].tail(6)     #Population in Germany: 83900471


# In[53]:


DE['people_fully_vaccinated_per_hundred'].tail(6)


# In[54]:


fig = px.line(DE, x="date", y="people_fully_vaccinated_per_hundred", title='Total People Fully-Vaccinated as Percentage of Total Population')
fig.show()


# ### Another Method

# In[55]:


DEP=DE['people_fully_vaccinated']/83900471*100    #As scalar division


# In[56]:


DEP.tail(6)


# ## Visualization for 3 Countries
# 
# * United States
# * Germany
# * Egypt

# In[57]:


b_US=vacc_info['location']=='United States'
b_DE=vacc_info['location']=='Germany'
b_UK=vacc_info['location']=='United Kingdom'


# In[58]:


sum(b_DE) #Rows


# In[59]:


sum(b_US|b_DE|b_UK) #OR operator


# In[60]:


b_all_vacc=b_US|b_DE|b_UK


# In[61]:


my_vacc_list=vacc_info[b_all_vacc]


# In[62]:


my_vacc_list


# In[63]:


fig = px.line(my_vacc_list, x="date", y="people_fully_vaccinated_per_hundred", color='location', title='Total People Fully-Vaccinated as Percentage of Total Population')
fig.show()


# # DONE !!
