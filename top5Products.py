import pandas as pd
import numpy as np

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper,ColumnDataSource, HoverTool, LogColorMapper)
from bokeh.palettes import Viridis6 as palette
from bokeh.layouts import widgetbox,column
from bokeh.models.widgets import Select 

def f(data,year,month):
    recent = data[(data['year']==year) & (data['month']==month)]
    recent_by_day = recent.groupby('day')
    sales_by_year = recent_by_day['Sales'].agg(np.sum)
    sales = [sales for sales in sales_by_year]
    return sales


data = pd.read_excel(r'C:\Users\user\Desktop\dashboard\store-dataset.xlsx')
data['Order_Date'] = pd.to_datetime(data['Order_Date'])
data['year'],data['month'],data['day'] = data['Order_Date'].dt.year, data['Order_Date'].dt.month,data['Order_Date'].dt.day

recent = data[(data['year'] == 2017) & (data['month'] == 12)] 

group_by_day = recent.groupby('day')
x=group_by_day['Sales'].agg(np.sum)
sales = [sale for sale in x]
print(type(sales))
source = ColumnDataSource(data={'days':[x for x in range(1,30)],'sales':sales})
plot = figure()
plot.line(x='days', y='sales', source=source)

menu1 = Select(title="Year", value="2017", options=['2017','2016','2015','2014'])
#menu2 = Select(title="Month", value="Dec",options=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

def callback(attr,old,new):
    month_num = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    year = int(menu1.value)
    #month = month_num[menu2.value]
    source.data = {'days':[x for x in range(1,30)],'sales':f(data,year,12)}

menu1.on_change('value',callback)
#menu2.on_change('value',callback)

layout = column(menu1,plot)
curdoc().add_root(layout)