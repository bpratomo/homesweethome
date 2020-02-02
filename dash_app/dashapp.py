import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask_cors import CORS
import json
import redis

from sqlalchemy import create_engine
import pandas as pd 
import plotly.express as px
from textwrap import dedent as d

import base64

# Create sqlalchemy connection 
engine = create_engine('postgresql://postgres:Teknikfisika123@localhost/homesweethome')

df = pd.read_sql('browse_home',engine)
all_columns = list(df.columns.values.tolist())
all_columns.remove('id_from_website')
all_columns.remove('id')
print(all_columns)
long_df = pd.melt(df,'id',all_columns)


#region dashapp
app = dash.Dash('housingPlot')
CORS(app)


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
        #Event containers
        html.Div(id='relayout-data-event', style={'display': 'none'}),
        html.Div(id='click-data-event', style={'display': 'none'}),
        html.Div(id='selected-data-event', style={'display': 'none'}),

        
        # Filters
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='price'
            ),
        ],
        style={'width': '30%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='area'
            ),
        ], style={'width': '30%', 'display': 'inline-block'}),


        html.Div([
            dcc.Dropdown(
                id='color-by',
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

    # Graph
    html.Div([
        dcc.Graph(
            id='indicator-scatter',
        )
    ], style={'width': '98%','height':'200%', 'display': 'inline-block', 'padding': '0 20'}),


    ])




# Graph update callback
@app.callback(
    dash.dependencies.Output('indicator-scatter', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('yaxis-column', 'value'),
     dash.dependencies.Input('color-by', 'value'),
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








# Event data functions

@app.callback( 
Output('relayout-data-event', 'children'),
[Input('indicator-scatter', 'relayoutData'),]
)
def save_relayout_data(relayoutData):
    return json.dumps(relayoutData)


@app.callback( 
Output('click-data-event', 'children'),
[Input('indicator-scatter', 'clickData'),]
)
def save_click_data(clickData):
    return json.dumps(clickData)

@app.callback( 
Output('selected-data-event', 'children'),
[Input('indicator-scatter', 'selectedData'),]
)
def save_selected_data(selectedData):
    return json.dumps(selectedData)



#endregion 


class SessionStore(object):
    # The default serializer, for now
    def __init__(self, conn, session_key, secret, serializer=None):

        self._conn = conn
        self.session_key = session_key
        self._secret = secret
        self.serializer = serializer or JSONSerializer
        self.hash, self.decoded_data = self.load()


    def load(self):
        session_data = self._conn.get(self.session_key)
        
        if not session_data is None:
            return self._decode(session_data)
        
        else:
            return {}


    def _decode(self, session_data):
        encoded_data = base64.b64decode(force_bytes(session_data))
        try:

            hash, serialized = encoded_data.split(b':',1)
            return hash, self.serializer().loads(serialized)
        
        except Exception as e:
            return {}


    def _encode(self, session_data):
        serialized = self.serializer().dumps(session_data)
 

    def save(self):
        session_data = self.encode(self._get_session(no_load=must_create))
        self._conn.save(session_key,expire_in, session_data, must_create)

        








if __name__ == "__main__":
    app.run_server(debug=True)