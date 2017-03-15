import pandas as pd
import plotly.graph_objs as go

df_map = pd.read_excel(r'C:\Users\tweatherall\Desktop\Python\2011_US_AGRI_Exports.xlsx', sheetname='Sheet1')

map_data = dict(type = 'choropleth',
           colorscale = 'YIOrRd',
           locations = df_map['code'],
           locationmode = 'USA-states',
           z = df_map['total exports'],
           text = df_map['text'],
           marker = dict(line = dict(color = 'rgb(255,255,255)', width = 2)),
           colorbar = {'title':'Millions USD'})

map_layout = dict(title = '2011 US Agriculture Exports by State',
             geo = dict(scope = 'usa', showlakes = True, lakecolor = 'rgb(85,173,240)'))

choromap = go.Figure(data=[map_data],layout=map_layout)
