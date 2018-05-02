import numpy as np
import pandas as pd

from bokeh.plotting import figure,show,output_file
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.models import (ColumnDataSource, HoverTool, LogColorMapper)
from bokeh.palettes import Viridis6 as palette
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select

#del states["HI"]
#del states["AK"]

states_sort = sorted(states)
state_xs = [states[code]['lons'] for code in states_sort]
state_ys = [states[code]['lats'] for code in states_sort]
state_names = [states[code]['name'] for code in states_sort]
#state_names.sort()
print(len(state_names))
data = pd.read_excel(r'C:\Users\user\Desktop\store-dataset.xlsx')

data['Order_Date'] = pd.to_datetime(data['Order_Date'])

data['year'],data['month'] = data['Order_Date'].dt.year, data['Order_Date'].dt.month
'''
by_year = data.groupby('year')
print(by_year['Sales'].agg(np.sum))

by_month = data.groupby('month')
sales_by_month = by_month['Sales'].agg(np.sum)
'''
by_state = data.groupby('State')

sales_by_state = by_state['Sales'].agg(np.sum)
print(len(sales_by_state))

sales = [sales for sales in sales_by_state]

source = ColumnDataSource(data=dict(x=state_xs,y=state_ys,name=state_names,state_sales=sales))
color_mapper = LogColorMapper(palette=palette)
TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(title="Sales by State", tools = TOOLS,x_axis_location=None,y_axis_location=None,toolbar_location="left",plot_width=1100,plot_height=700)


p.patches('x','y',source=source,line_color="#000000",fill_color={'field':'state_sales','transform':color_mapper},fill_alpha=0.7,line_width=0.5)
hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("Name","@name"),("Sales:","@state_sales"),("(Long,Lat)","($x,$y)")]
#output_file('states.html')
show(p)

