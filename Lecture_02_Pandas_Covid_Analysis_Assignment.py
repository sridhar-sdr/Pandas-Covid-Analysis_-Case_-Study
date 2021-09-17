
# coding: utf-8

# # Task: Covid-19 Data Analysis
# ### This notebook is used to understand the comprehension of Data Analysis techniques using Pandas library.

# ### Data Source: 
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
# 
# ### File naming convention
# 
# MM-DD-YYYY.csv in UTC.
# 
# ### Field description
# 
# - Province_State: China - province name; US/Canada/Australia/ - city name, state/province name; Others - name of the event (e.g., "Diamond Princess" cruise ship); other countries - blank.
# 
# - Country_Region: country/region name conforming to WHO (will be updated).
# 
# - Last_Update: MM/DD/YYYY HH:mm (24 hour format, in UTC).
# 
# - Confirmed: the number of confirmed cases. For Hubei Province: from Feb 13 (GMT +8), we report both clinically diagnosed and lab-confirmed cases. For lab-confirmed cases only (Before Feb 17), please refer to who_covid_19_situation_reports. For Italy, diagnosis standard might be changed since Feb 27 to "slow the growth of new case numbers." (Source)
# 
# - Deaths: the number of deaths.
# 
# - Recovered: the number of recovered cases.

# ### Question 1

# #### Read the dataset

# In[95]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# set this so the 
get_ipython().run_line_magic('matplotlib', 'inline')


data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-21-2021.csv')
data


# #### Display the top 5 rows in the data

# In[24]:


data.head(5)


# #### Show the information of the dataset

# In[21]:


data.info()


# #### Show the sum of missing values of features in the dataset

# In[41]:


len(data)
data.count()
count_nan = len(data) - data.count()
count_nan


# ### Question 2

# #### Show the number of Confirmed cases by Country

# In[45]:


data[['Country_Region', 'Confirmed']]


# #### Show the number of Deaths by Country

# In[44]:


data[['Country_Region', 'Deaths']]


# #### Show the number of Recovered cases by Country

# In[47]:


data[['Country_Region', 'Recovered']]


# #### Show the number of Active Cases by Country

# In[48]:


data[['Country_Region', 'Active']]


# #### Show the latest number of Confirmed, Deaths, Recovered and Active cases Country-wise

# In[96]:


data[['Last_Update','Country_Region', 'Confirmed','Deaths','Recovered','Active']]


# ### Question 3

# ### Show the countries with no recovered cases

# In[65]:



data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-21-2021.csv')
data


# In[93]:


output = data[data['Recovered']==0][['Country_Region', 'Recovered']]
output


# #### Show the countries with no confirmed cases

# In[92]:


output = data[data['Confirmed']==0][['Country_Region','Confirmed']]
output


# #### Show the countries with no deaths

# In[91]:


output = data[data['Deaths']==0][['Country_Region','Deaths']]
output


# In[90]:


output = data[data['Deaths']==0][['Country_Region','Confirmed','Deaths','Recovered']]
output


# ### Question 4

# #### Show the Top 10 countries with Confirmed cases

# In[119]:


d= data.sort_values('Confirmed', ascending=False).head(10)
d[['Country_Region', 'Recovered','Confirmed']]


# #### Show the Top 10 Countries with Active cases

# In[116]:


c= data.groupby("Country_Region")
c=c.sum()
c=c.sort_values(["Active"],ascending=False)
c.head(10)


# ### Question 5

# #### Plot Country-wise Total deaths, confirmed, recovered and active casaes where total deaths have exceeded 50,000

# In[20]:


import matplotlib.pyplot as plt


# In[22]:



New_data = data.groupby(["Country_Region"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
New_data = New_data.sort_values(by='Deaths', ascending=False)
New_data = New_data[New_data['Deaths']>50000]
plt.figure(figsize=(15, 5))
plt.plot(New_data['Country_Region'], New_data['Deaths'],color='blue')
plt.plot(New_data['Country_Region'], New_data['Confirmed'],color='red')
plt.plot(New_data['Country_Region'], New_data['Recovered'], color='yellow')
plt.plot(New_data['Country_Region'], New_data['Active'], color='black')

plt.title('Country-wise Total deaths, confirmed, recovered and active casaes where total deaths have exceeded 50,000')
plt.show()


# ### Question 6

# ### Plot Province/State wise Deaths in USA

# In[31]:


import plotly.express as px


# In[19]:


covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-09-2021.csv')


# In[20]:


covid_data.columns


# In[32]:


import pandas as pd
pio.templates.default = "ggplot2"
us_data = data[data['Country_Region']=='US'].drop(['Country_Region','Lat', 'Long_'], axis=1)
us_data = us_data[us_data.sum(axis = 1) > 0]
us_data = us_data.groupby(['Province_State'])['Deaths'].sum().reset_index()
us_data_death = us_data[us_data['Deaths'] > 0]
state_fig = px.bar(us_data_death, x='Province_State', y='Deaths', title='State wise deaths in USA', text='Deaths')
state_fig.show()


# ### Question 7

# ### Plot Province/State Wise Active Cases in USA

# In[27]:


import pandas as pd
import plotly.express as px
pio.templates.default = "plotly_dark"
us_data = data[data['Country_Region']=='US'].drop(['Country_Region','Lat', 'Long_'], axis=1)
us_data = us_data[us_data.sum(axis = 1) > 0]
us_data = us_data.groupby(['Province_State'])['Active'].sum().reset_index()
us_data_death = us_data[us_data['Active'] > 0]
state_fig = px.bar(us_data_death, x='Province_State', y='Active', title='State wise Active cases in USA', text='Active')
state_fig.show()


# ### Question 8

# ### Plot Province/State Wise Confirmed cases in USA

# In[26]:


import pandas as pd
import plotly.express as px
pio.templates.default = "plotly"
us_data = data[data['Country_Region']=='US'].drop(['Country_Region','Lat', 'Long_'], axis=1)
us_data = us_data[us_data.sum(axis = 1) > 0]
us_data = us_data.groupby(['Province_State'])['Confirmed'].sum().reset_index()
us_data_death = us_data[us_data['Confirmed'] > 0]
state_fig = px.bar(us_data_death, x='Province_State', y='Confirmed', title='State wise confirmed cases in USA', text='Confirmed')
state_fig.show()


# ### Question 9

# ### Plot Worldwide Confirmed Cases over time

# In[30]:



import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.templates.default = "seaborn"
 
data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-21-2021.csv')
data
grouping = data.groupby('Last_Update')['Last_Update', 'Confirmed', 'Deaths'].sum().reset_index()
fig = px.line(grouping, x="Last_Update", y="Confirmed",
             title="Worldwide Confirmed Cases Over Time")
fig.show()

