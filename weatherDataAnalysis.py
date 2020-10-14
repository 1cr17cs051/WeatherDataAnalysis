import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\Hithesh\AppData\Local\Programs\Python\Python37-32\Scripts\weatherHistory.csv");
data['Formatted Date'] = pd.to_datetime(data['Formatted Date'] , utc=True)
data['Formatted Date']
data.dtypes
data = data.set_index('Formatted Date')
data_columns = ['Apparent Temperature (C)','Humidity']
data_monthly_mean = data[data_columns].resample('MS').mean()
data_monthly_mean
import seaborn as sns
import warnings
data_monthly_mean
warnings.filterwarnings("ignore")
plt.figure(figsize=(10,5))
plt.title("Variation in Apparent Temperature and Humidity with Time")
sns.lineplot(data=data_monthly_mean)
data1 = data_monthly_mean[data_monthly_mean.index.month==4]
print(data1)
data1.dtypes
import matplotlib.dates as mdates
fig,ax1 = plt.subplots(figsize=(15,5))
ax1.plot(data1.loc['2006-04-01':'2016-04-01','Apparent Temperature (C)'],marker='o',linestyle='-',label='Apparent Temperature(c)')
ax1.plot(data1.loc['2006-04-01':'2016-04-01','Humidity'],marker='o',linestyle='-',label='Humidity')
ax1.set_xticks= ["04-01-2006","04-01-2007",'04-01-2008','04-01-2009','04-01-2010','04-01-2011','04-01-2012','04-01-2013','04-01-2014','04-01-2015','04-01-2016']
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %m %Y'))
ax1.legend(loc = 'center right')
ax1.set_xlabel('Month of April')