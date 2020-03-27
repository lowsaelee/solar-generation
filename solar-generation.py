# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 08:30:31 2020

Data Visualization - Solar Readings

Required Visualization

1. Average Daily Generation - Get Mean of daily generations through out years
2. Total generation per year - yearly bar graph - Done
3. Monthly generation - for every year

@author: lsaelee
"""

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("SolarReadings-2020-03-26.csv")

#print(df.head())


###################### 1. Average Daily Generation#############################
df_date = df['Date'].str.split("/", n=2, expand=True)
df_date[0] = df_date[0].apply('{:0>2}'.format)
df_date[1] = df_date[1].apply('{:0>2}'.format)
#print(df_date.head(5))

#df_date_split = df
#df_date_split["Month"] = df_date[0]
#print(df_date.shape)
#df_date['monthDay']=df_date[0] + '.' + df_date[1]
df_date['monthDay']=df_date[0]
df_date['daily'] = df['DailyGenerations']
df_date=df_date.drop([0,1], axis=1)
#df_date.rename(columns={2: "year"}, axis='index')
df_date.columns.values[0]='year'
print(df_date.head(5))
print(df_date.shape)
print("=====================================================================")
df_daily_average = df_date.groupby(['monthDay'], as_index=False).mean()
print(df_daily_average.head(12))
print(df_daily_average.shape)
plt.plot(df_daily_average['monthDay'],df_daily_average['daily'])
#plt.xticks(np.arange(0, 366, 30), rotation=45) 
###################### 1. Average Daily Generation#############################



"""
print("=====================================================================")

################### 2. Total generation per year###############################
df['Year'] = df['Date'].str[-4:]
df_year_daily = df.groupby(['Year'], as_index=False).sum()
print(df_year_daily.head(6))
#df_year_daily.plot(x='Year',y='DailyGenerations', kind='bar')
plt.bar(df_year_daily['Year'],df_year_daily['DailyGenerations'])
plt.title('Yearly Generations')
################### 2. Total generation per year###############################

print("=====================================================================")
"""

"""
################ 3. Monthly Total Generation By Year###########################
################ Line Graph ###################################################
df_date = df['Date'].str.split("/", n=2, expand=True)
df_date[0] = df_date[0].apply('{:0>2}'.format)
df_date[1] = df_date[1].apply('{:0>2}'.format)
#print(df_date.head(5))

#df_date_split = df
#df_date_split["Month"] = df_date[0]
#print(df_date.shape)
#df_date['monthDay']=df_date[0] + '.' + df_date[1]
df_date['monthDay']=df_date[0]
df_date['daily'] = df['DailyGenerations']
df_date=df_date.drop([0,1], axis=1)
#df_date.rename(columns={2: "year"}, axis='index')
df_date.columns.values[0]='year'
df_year_2015 = df_date[df_date['year']=="2015"]
df_year_2016 = df_date[df_date['year']=="2016"]
df_year_2017 = df_date[df_date['year']=="2017"]
df_year_2018 = df_date[df_date['year']=="2018"]
df_year_2019 = df_date[df_date['year']=="2019"]
df_year_2020 = df_date[df_date['year']=="2020"]
#print(df_year_2020.head(32))
#print(df_year_2020.shape)

#print(df_date_2016.head(31))
#print(df_date_2016.shape)
print("=====================================================================")
df_daily_average1 = df_year_2015.groupby(['monthDay'], as_index=False).sum()
df_daily_average2 = df_year_2016.groupby(['monthDay'], as_index=False).sum()
df_daily_average3 = df_year_2017.groupby(['monthDay'], as_index=False).sum()
df_daily_average4 = df_year_2018.groupby(['monthDay'], as_index=False).sum()
df_daily_average5 = df_year_2019.groupby(['monthDay'], as_index=False).sum()
df_daily_average6 = df_year_2020.groupby(['monthDay'], as_index=False).sum()
#print(df_daily_average2.head(12))
#print(df_daily_average2.shape)

plt.figure(figsize=(20,10))
plt.plot(df_daily_average2['monthDay'],df_daily_average2['daily'])
plt.plot(df_daily_average3['monthDay'],df_daily_average3['daily'])
plt.plot(df_daily_average4['monthDay'],df_daily_average4['daily'])
plt.plot(df_daily_average5['monthDay'],df_daily_average5['daily'])
#plt.plot(df_daily_average6['monthDay'],df_daily_average6['daily'])
plt.plot(df_daily_average1['monthDay'],df_daily_average1['daily'])
#plt.xticks(np.arange(0, 366, 30), rotation=45) 
################ 3. Monthly Total Generation By Year###########################
"""


################ 3. Monthly Total Generation By Year###########################
################ Bar Graph ###################################################
df_date = df['Date'].str.split("/", n=2, expand=True)
df_date[0] = df_date[0].apply('{:0>2}'.format)
df_date[1] = df_date[1].apply('{:0>2}'.format)

n_groups = 12

df_date['monthDay']=df_date[0]
df_date['daily'] = df['DailyGenerations']
df_date=df_date.drop([0,1], axis=1)

df_date.columns.values[0]='year'
df_year_2015 = df_date[df_date['year']=="2015"]
df_year_2016 = df_date[df_date['year']=="2016"]
df_year_2017 = df_date[df_date['year']=="2017"]
df_year_2018 = df_date[df_date['year']=="2018"]
df_year_2019 = df_date[df_date['year']=="2019"]
df_year_2020 = df_date[df_date['year']=="2020"]

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.6
plt.figure(figsize=(20,10))



print("=====================================================================")
df_daily_average1 = df_year_2015.groupby(['monthDay'], as_index=False).sum()
df_daily_average2 = df_year_2016.groupby(['monthDay'], as_index=False).sum()
df_daily_average3 = df_year_2017.groupby(['monthDay'], as_index=False).sum()
df_daily_average4 = df_year_2018.groupby(['monthDay'], as_index=False).sum()
df_daily_average5 = df_year_2019.groupby(['monthDay'], as_index=False).sum()
df_daily_average6 = df_year_2020.groupby(['monthDay'], as_index=False).sum()
#print(df_daily_average2.head(12))
#print(df_daily_average2.shape)



rects1 = plt.bar(index,df_daily_average2['daily'], bar_width,
alpha=opacity,
color='b',
label='2016')

rects2 = plt.bar(index + bar_width,df_daily_average3['daily'], bar_width,
alpha=opacity,
color='g',
label='2017')

rects3 = plt.bar(index + (bar_width*2),df_daily_average4['daily'], bar_width,
alpha=opacity,
color='y',
label='2018')

rects4 = plt.bar(index + (bar_width*3),df_daily_average5['daily'], bar_width,
alpha=opacity,
color='r',
label='2019')


plt.xlabel('Month')
plt.ylabel('Monthly Generation (kWh)')
plt.title('Monthly Generation by Year')
plt.xticks(index + bar_width, ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
plt.legend()
################ 3. Monthly Total Generation By Year###########################
