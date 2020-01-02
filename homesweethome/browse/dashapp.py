import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import json
from sqlalchemy import create_engine
import pandas as pd 
import plotly.express as px
from textwrap import dedent as d


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
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


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

    html.Div([
            dcc.Markdown(d("""
                **Zoom and Relayout Data**

                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
                Clicking on legend items will also fire
                this event.
            """)),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='three columns')
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
                      height=800,
                      custom_data=['id'])


@app.callback(
    Output('relayout-data', 'children'),
    [Input('crossfilter-indicator-scatter', 'relayoutData'),
    Input('crossfilter-indicator-scatter', 'hoverData'),
    Input('crossfilter-indicator-scatter', 'clickData'),
    Input('crossfilter-indicator-scatter', 'selectedData'),
    Input('crossfilter-indicator-scatter', 'clickAnnotationData')
    ])
def display_relayout_data(relayoutData,hoverData,clickData,selectedData,clickAnnotationData):
    ctx = dash.callback_context
    print(ctx.states)
    ctx_msg = json.dumps({
    'states': ctx.states,
    'triggered': ctx.triggered,
    'inputs': ctx.inputs
    }, indent=2)
    print(ctx_msg)
    data_dict = {}
    data_dict['relayoutData'] = relayoutData
    data_dict['hoverData'] = hoverData
    data_dict['clickData'] = clickData    
    if clickData:
        clickdata_dict = clickData
        index_from_clickdata = clickdata_dict['points'][0]['pointIndex']
        row_from_df = df.loc[index_from_clickdata]
        print(row_from_df)

    data_dict['selectedData'] = selectedData
    data_dict['clickAnnotationData'] = clickAnnotationData

    return json.dumps(data_dict,indent=4)


#endregion 