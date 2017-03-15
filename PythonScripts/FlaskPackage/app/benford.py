import pandas as pd
import plotly.graph_objs as go

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


#create visualization figure
benford_fig = go.Figure(data=benford_data,layout=benford_layout)
