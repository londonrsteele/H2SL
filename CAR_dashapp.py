import sys
from dash import *
from graphing import (accuracy, missions, kill, stratagems,
                      metadata, stat_scraper)
import graphing.big_graph as big__graph

# Create Dash app
CAR_dashapp = Dash()

# Create Stat_Scraper
scraper = stat_scraper.Stat_Scraper()

# Use Stat_Scraper to load desired focus CAR_df
CAR_df = scraper.load_file(sys.argv[2])

# If _df is empty, don't run Dash
if (CAR_df.empty):
    raise RuntimeError("Empty dataframe at Dash initialization")

# Use Stat_Scraper to get most recent 10 (or less) files
list_of_old_filenames = scraper.get_last10_filenames("CAR", sys.argv[2])

# Use Stat_Scraper to load most recent 10 files and store how many were loaded
list_of_10_dfs = scraper.load_files(list_of_old_filenames)
num_dfs_loaded = len(list_of_10_dfs)

# Create dashboard layout 
CAR_dashapp.layout = html.Div([

    # Div Level 1 - Title
    html.Div( children = "Most Recent Career Stats", className="CARdashapp-Div--title" ),

    # Div Level 1 - Main body
    html.Div( children = [
        
        # Div Level 2 - slider row
        html.Div( children = [
            # slider
            dcc.Slider(
                min=-(num_dfs_loaded-1),
                max=0,
                step=1,
                marks={i: f"Last Log" if i == 0 else str(i) + " Logs" for i in range(-(num_dfs_loaded-1),1)},
                value=0,
                id="slider"
            )
        ], className="CARdashapp-Div--slider"),

        # Div Level 2 - graphs row
        html.Div( children= [
            
            # Div Level 3 - Top row
            html.Div( children=[
                
                # Div Level 4 - 1st gridbox
                html.Div( children=[
                    dcc.Graph(id="accuracy-fig")
                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - 2nd gridbox
                html.Div( children=[
                    
                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - 3rd gridbox
                html.Div( children=[
                    dcc.Graph(id="missions-fig")
                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - 4th gridbox
                html.Div( children=[
                    
                ], className="CARdashapp-Div--gridbox")
            ], className="CARdashapp-Div--Top-row"),
            # Div Level 3 - Bottom row
            html.Div( children=[
                
                # Div Level 4 - left grid box
                html.Div( children=[
                    # kills fig (interactive with slider)
                    dcc.Graph(id="kills-fig")
                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - right grid box
                html.Div( children=[
                    # stratagems fig (interactive with slider)
                    dcc.Graph(id="stratagems-fig")
                ], className="CARdashapp-Div--gridbox")
            ], className="CARdashapp-Div--Bottom-row"),
        ], className="CARdashapp-Div--graphs-row"),
    ], className="CARdashapp-Div--main-box")
], className="CARdashapp-Div--base")

################################################################
# callback: create kill
################################################################
@CAR_dashapp.callback(
    Output("kills-fig", "figure"),
    Input("slider", "value")
)
def update_kills(selected_game):
    fig = kill.Create_Kill_Graph(list_of_10_dfs[abs(selected_game)])
    return fig

################################################################
# callback: create stratagem
################################################################
@CAR_dashapp.callback(
    Output("stratagems-fig", "figure"),
    Input("slider", "value")
)
def update_stratagems(selected_game):
    fig = stratagems.Create_Stratagem_Graph(list_of_10_dfs[abs(selected_game)])
    return fig

################################################################
# callback: create accuracy
################################################################
@CAR_dashapp.callback(
    Output("accuracy-fig", "figure"),
    Input("slider", "value")
)
def update_accuracy(selected_game):
    fig = accuracy.Create_Accuracy_Graph(list_of_10_dfs[abs(selected_game)], "CAR")
    return fig

################################################################
# callback: create missions
################################################################
@CAR_dashapp.callback(
    Output("missions-fig", "figure"),
    Input("slider", "value")
)
def update_missions(selected_game):
    fig = missions.Create_Missions_Graph(list_of_10_dfs, abs(selected_game))
    return fig


################################################################
################################################################
# Execution: CAR_dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    CAR_dashapp.run(debug=True,port=8051)