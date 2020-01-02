import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import json
from sqlalchemy import create_engine
import pandas as pd 
import plotly.express as px


# Create sqlalchemy connection 
engine = create_engine('postgresql://postgres:Teknikfisika123@localhost/homesweethome')

df = pd.read_sql('browse_home',engine)
all_columns = list(df.columns.values.tolist())
all_columns.remove('id_from_website')
all_columns.remove('id')
print(all_columns)
long_df = pd.melt(df,'id',all_columns)


#region dashapp
app = DjangoDash('housingPlot')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



available_indicators = long_df['variable'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='price'
            ),
        ],
        style={'width': '30%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='area'
            ),
        ], style={'width': '30%', 'display': 'inline-block'}),


        html.Div([
            dcc.Dropdown(
                id='crossfilter-color-by',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='region'
            ),
        ],
        style={'width': '30%', 'display': 'inline-block'}),

    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
        )
    ], style={'width': '98%','height':'200%', 'display': 'inline-block', 'padding': '0 20'}),

])


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-color-by', 'value'),
     ])
def update_graph(xaxis_column_name, yaxis_column_name,color_by
                 ):


    return px.scatter(df,
                      x=df[xaxis_column_name],
                      y = df[yaxis_column_name],
                      color=df[color_by],
                      size = [100 for i in range(len(df))],
                      height=800)
    


#endregion 