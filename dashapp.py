import sys
from dash import *
from graphing import (accuracy, survivor, kill, stratagems, metadata, stat_scraper)
import graphing.big_graph as big__graph

# Create Dash app
dashapp = Dash()

# Create Stat_Scraper
scraper = stat_scraper.Stat_Scraper()

# Use Stat_Scraper to load desired focus EOM_df and CAR_df
EOM_df = scraper.load_file(sys.argv[1])
CAR_df = scraper.load_file(sys.argv[2])

# If _df is empty, don't run Dash
if (EOM_df.empty) | (CAR_df.empty):
    raise RuntimeError("Empty dataframe(s) at Dash initialization")

# Create figures
accuracy_fig = accuracy.Create_Accuracy_Graph(EOM_df)
survivor_fig = survivor.Create_Survivor_Graph(EOM_df)
kills_fig = kill.Create_Kill_Graph(CAR_df)
stratagems_fig = stratagems.Create_Stratagem_Graph(CAR_df)
# TODO: RC-TR-RC (top right square)

# Create dropdown for bottom right graph ("big_graph")
dropdown = dcc.Dropdown(metadata.list_of_strats, "Total Kills", clearable=False)
# make skeleton of big_graph
big_graph = dcc.Graph()

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
                html.H4("Big Graph"), dropdown, big_graph
            ], style={"display":"flex", "flexDirection":"column"})
        ], style={"display":"flex", "flexDirection":"column"})
    ], style={"display":"flex", "flexDirection":"row"})
], style={"display":"flex", "flexDirection":"column"})


# Set up function to handle dropdown and big_graph
@dashapp.callback(Output(big_graph, "figure"), Input(dropdown, "value"))
def update_big_graph(stat):
    fig = big__graph.Create_big_graph(stat)
    return fig

################################################################
################################################################
# Execution: dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    dashapp.run(debug=True,port=8052)