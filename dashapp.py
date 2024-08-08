import sys
from flask import request
import pandas as pd
from dash import *
import dash_bootstrap_components as dbc
import graphing.accuracy as accuracy

# Create Dash app
dashapp = Dash()

# Get data from sys.argv[1] and sys.arvg[2]
EOM_df = pd.read_csv(sys.argv[1])

# Create figures
accuracy_fig = accuracy.Create_Accuracy_Graph(EOM_df)

# Create dashboard layout 
dashapp.layout = dbc.Container([
    dbc.Row([
        html.Div("Last Mission Data")
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=EOM_df.to_dict("records"))
        ], width=6),
        dbc.Col([
            dcc.Graph(figure=accuracy_fig, id="accuracy-graph")
        ], width=6),
    ]),
], fluid=True)

# Set up functions to close Dash app on "X" click
def shutdown():
    func = request.environ.get("wekzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Wekzeug Server")
    func()

@dashapp.callback([Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/kill":
        shutdown()

# Run Dash app
if __name__ == "__main__":
    dashapp.run(debug=True,port=8050)