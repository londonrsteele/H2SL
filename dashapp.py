import sys
from flask import request
import pandas as pd
from dash import *
import dash_bootstrap_components as dbc
import graphing.accuracy as accuracy
import graphing.survivor as survivor
import graphing.kill as kill

# Create Dash app
dashapp = Dash(suppress_callback_exceptions=True)

# Get data from sys.argv[1] and sys.arvg[2]
EOM_df = pd.read_csv(sys.argv[1])
CAR_df = pd.read_csv(sys.argv[2])

# Create figures
accuracy_fig = accuracy.Create_Accuracy_Graph(EOM_df)
survivor_fig = survivor.Create_Survivor_Graph(EOM_df)
kills_fig = kill.Create_Kill_Graph(CAR_df)

# Create dashboard layout 
dashapp.layout = html.Div([

    html.Div( children = "Most Recent Mission Stats" ),

    html.Div( children= [
        dcc.Graph(id="accuracy-graph",
                  figure=accuracy_fig),
        dcc.Graph(id="survivor-graph",
                  figure=survivor_fig),
        dcc.Graph(id="kills-graph",
                  figure=kills_fig)
    ])

], style={"display":"flex", "flexDirection":"row"})

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