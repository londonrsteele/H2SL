import sys
from dash import *
from graphing import (accuracy, survivor, kill, stratagems, metadata, stat_scraper)
import graphing.big_graph as big__graph

# Create Dash app
CAR_dashapp = Dash()

# Create Stat_Scraper
scraper = stat_scraper.Stat_Scraper()

# Use Stat_Scraper to load desired focus CAR_df
CAR_df = scraper.load_file(sys.argv[1])

# If _df is empty, don't run Dash
if (CAR_df.empty):
    raise RuntimeError("Empty dataframe at Dash initialization")

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

################################################################
################################################################
# Execution: dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    CAR_dashapp.run(debug=True,port=8050)