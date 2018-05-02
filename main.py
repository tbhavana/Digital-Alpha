import numpy as np
import pandas as pd

from os.path import dirname, join

from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from bokeh.plotting import figure,show,output_file
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states

from scripts.top5Products import graph_tab

states_sort = sorted(states)
state_xs = [states[code]['lons'] for code in states_sort]
state_ys = [states[code]['lats'] for code in states_sort]
state_names = [states[code]['name'] for code in states_sort]

data = pd.read_excel(r'C:\Users\user\Desktop\dashboard\store-dataset.xlsx')
data['Order_Date'] = pd.to_datetime(data['Order_Date'])

data['year'],data['month'] = data['Order_Date'].dt.year, data['Order_Date'].dt.month


tab1 = top5Products(data)

tabs = Tabs(tabs = [tab1, tab2, tab3])

curdoc().add_root(tabs)