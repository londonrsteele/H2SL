import sys
from flask import request
import pandas as pd
from dash import *
from graphing import (accuracy, survivor, kill, stratagems, metadata, stat_scraper)
import graphing.big_graph as big__graph

# Create Dash app
CAR_dashapp = Dash()

# Create Stat_Scraper
scraper = stat_scraper.Stat_Scraper()

CAR_df = scraper.load_file(sys.argv[1])

# If _df is empty, don't run Dash
if (CAR_df.empty):
    sys.exit("Empty dataframe at Dash initialization")

# Create figures
kills_fig = kill.Create_Kill_Graph(CAR_df)
stratagems_fig = stratagems.Create_Stratagem_Graph(CAR_df)
# TODO: RC-TR-RC (top right square)

# Create dashboard layout 
CAR_dashapp.layout = html.Div([

    # Div Level 1 - Title
    html.Div( children = "Most Recent Mission Stats", className="app-Div--title" ),

    # Div Level 1 - Main body
    html.Div( children = [
        
        # Div Level 2 - Left column
        html.Div( children= [
            dcc.Graph(id="kills-graph",
                        figure=kills_fig)
        ]),
        
        # Div Level 2 - Right column
        html.Div( children = [

            # Div Level 3 - Right column top row
            html.Div( children = [

                # Div Level 4 - Right column top row left column 
                html.Div( children = [
                    dcc.Graph(id="stratagem-graph",
                              figure=stratagems_fig)
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
@CAR_dashapp.server.route("/kill", methods=["POST"])
def display_page(pathname):
    print("Killing Dash...")
    if pathname == "/kill":
        shutdown()

# Run Dash app
if __name__ == "__main__":
    CAR_dashapp.run(debug=True,port=8050)