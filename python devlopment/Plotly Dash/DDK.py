# Import packages
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv'
)

# Initialize app
app = Dash(__name__)

# Layout
app.layout = html.Div([

    html.H1(
        "My First App with Data, Graph, and Controls",
        style={'textAlign': 'center'}
    ),

    dcc.RadioItems(
        options=['pop', 'lifeExp', 'gdpPercap'],
        value='lifeExp',
        inline=True,
        id='my-radio-items',
        style={'margin': '20px'}
    ),

    html.Div([

        # Table
        html.Div([
            dag.AgGrid(
                rowData=df.to_dict('records'),
                columnDefs=[{"field": i} for i in df.columns],
                defaultColDef={
                    "resizable": True,
                    "sortable": True,
                    "filter": True
                },
                style={"height": "500px"}
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        # Graph
        html.Div([
            dcc.Graph(id='graph-placeholder')
        ], style={'width': '48%', 'display': 'inline-block'})

    ])

])

# Callback
@callback(
    Output('graph-placeholder', 'figure'),
    Input('my-radio-items', 'value')
)
def update_graph(col_chosen):

    fig = px.histogram(
        df,
        x='continent',
        y=col_chosen,
        histfunc='avg',
        title=f'Average {col_chosen} by Continent'
    )

    return fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)