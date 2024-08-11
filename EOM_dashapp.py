import sys
from dash import *
from graphing import (accuracy, survivor, kill, stratagems, metadata, stat_scraper)
import graphing.big_graph as big__graph

# Create Dash app
EOM_dashapp = Dash()

# Create Stat_Scraper
scraper = stat_scraper.Stat_Scraper()

# Use Stat_Scraper to load desired focus EOM_df
EOM_df = scraper.load_file(sys.argv[1])

# If _df is empty, don't run Dash
if (EOM_df.empty):
    raise RuntimeError("Empty dataframe at Dash initialization")

# Create figures
accuracy_fig = accuracy.Create_Accuracy_Graph(EOM_df)
survivor_fig = survivor.Create_Survivor_Graph(EOM_df)

# Create dashboard layout 
EOM_dashapp.layout = html.Div([

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

################################################################
################################################################
# Execution: dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    EOM_dashapp.run(debug=True,port=8050)