from flask import Flask, render_template
import plotly
import pandas as pd
import plotly.graph_objs as go
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

app = Flask(__name__)

df = pd.read_excel(r'C:\\Users\\tweatherall\\Desktop\\BenfordsLaw.xlsx',sheetname='Sheet1')
benford = go.Scatter(x=df['FirstDigit'],y=df['BenfordLaw'],name='Probability')
pct = go.Bar(x=df['FirstDigit'],y=df['PCT'],name='Actual Occurance')

data1 = [benford,pct]
data2 = [benford,pct]

layout = go.Layout(
    barmode='group',
    xaxis = dict(title='First Digit'),
    yaxis = dict(title='Percentage')
)

fig1 = go.Figure(data=data1,layout=layout)
fig2 = go.Figure(data=data2,layout=layout)
figs = [fig1,fig2]
figs = (fig for fig in figs)

@app.route('/')
def index():
    #return ''.join([plotly.offline.plot(fig1, output_type='div'),plotly.offline.plot(fig1, output_type='div')]) #,include_plotlyjs=False,show_link=False)
    #this iterates through the list of plots, using a generator, and returns the divs, joined together, to the index (home) page.
    return ''.join([plotly.offline.plot(fig, output_type='div') for fig in figs])

@app.route('/tuna')
def tuna():
    return '<h2> tuna is gooooood</h2>'

@app.route('/profile/<username>')
def profile(username):
    return 'Hey there {}'.format(username)

if __name__ == "__main__":
    app.run(debug=True)
