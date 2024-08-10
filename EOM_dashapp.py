import sys
from flask import request
import pandas as pd
from dash import *
import graphing.accuracy as accuracy
import graphing.survivor as survivor
import graphing.kill as kill
import graphing.stratagems as stratagems
import graphing.metadata as metadata
import graphing.big_graph as big__graph
# Create Dash app
dashapp = Dash(suppress_callback_exceptions=True)

# TODO: handle either file == "ERROR"
EOM_datafile = sys.argv[1]

# Get data from sys.argv[1] and sys.arvg[2]
EOM_df = pd.read_csv("./save_files/"+EOM_datafile)

# Create figures
accuracy_fig = accuracy.Create_Accuracy_Graph(EOM_df)
survivor_fig = survivor.Create_Survivor_Graph(EOM_df)

# Create dashboard layout 
dashapp.layout = html.Div([

    # Div Level 1 - Title
    html.Div( children = "Most Recent Mission Stats", className="app-Div--title" ),

    # Div Level 1 - Main body
    html.Div( children = [
        
        # Div Level 2 - Left column
        html.Div( children= [
            dcc.Graph(id="accuracy-graph",
                        figure=accuracy_fig),
            dcc.Graph(id="survivor-graph",
                        figure=survivor_fig),
        ]),
        
        # Div Level 2 - Right column
        html.Div( children = [

            # Div Level 3 - Right column top row
            html.Div( children = [

                # Div Level 4 - Right column top row left column 
                html.Div( children = [

                ]),

                # Div Level 4 - Right column top row right column
                html.Div( children = "RCTRRC")
            
            ], style={"display":"flex", "flexDirection":"row"}),

            # Div Level 3 - Right column bottom row
            html.Div( children = [

            ], style={"display":"flex", "flexDirection":"column"})
        ], style={"display":"flex", "flexDirection":"column"})
    ], style={"display":"flex", "flexDirection":"row"})
], style={"display":"flex", "flexDirection":"column"})


# Set up functions to close Dash app on "X" click
def shutdown():
    func = request.environ.get("wekzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Wekzeug Server")
    func()

# this callback handles Flask redirecting to the /kill url
@dashapp.callback([Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/kill":
        shutdown()

# Run Dash app
if __name__ == "__main__":
    dashapp.run(debug=True,port=8050)