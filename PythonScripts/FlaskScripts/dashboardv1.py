from flask import Flask, render_template, Markup
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

#pull data into dataframe and create line and bar chart
df = pd.read_excel(r'C:\\Users\\tweatherall\\Desktop\\BenfordsLaw.xlsx',sheetname='Sheet1')
benfordline = go.Scatter(x=df['FirstDigit'],y=df['BenfordLaw'],name='Probability')
benfordbar = go.Bar(x=df['FirstDigit'],y=df['PCT'],name='Actual Occurance')

#formate visualization data into format required by plotly
benford_data = [benfordline,benfordbar]

#define layout for visualization
benford_layout = go.Layout(
    barmode='group',
    xaxis = dict(title='First Digit'),
    yaxis = dict(title='Percentage'),
    # width=500,
    # height=500
)

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

#create visualization figure
benford_fig = go.Figure(data=benford_data,layout=benford_layout)

#plotly.offline.plot(fig1, show_link=False, output_type='div', include_plotlyjs=False)

#create web server app and point to html and css template
# app = Flask(__name__,static_folder= r'C:\Users\tweatherall\AppData\Local\Programs\Python\Python35-32\PythonScripts\FlaskScripts\static',
# template_folder= r'C:\Users\tweatherall\AppData\Local\Programs\Python\Python35-32\PythonScripts\FlaskScripts\templates')

#this works same as above, but instead of hard coding the path for static and template files, I only need to hardcode the path of the app object
app = Flask(__name__,root_path=r'C:\Users\tweatherall\AppData\Local\Programs\Python\Python35-32\PythonScripts\FlaskScripts')

@app.route('/')
def index():
    return render_template('index2.html',BenfordsLaw=Markup(plot(benford_fig, output_type='div'))
    # ,chart2=Markup(plot(benford_fig, output_type='div')),
    ,chart2=Markup(plot( choromap, output_type='div')))

if __name__ == "__main__":
    # print(app.root_path)
    # print(app.instance_path)
    app.run(debug=True)
