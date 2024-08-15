import sys
from dash import *
from graphing import (accuracy, survivor, kill, stratagems, metadata, stat_scraper)
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

# Create figures
kills_fig = kill.Create_Kill_Graph(CAR_df)
stratagems_fig = stratagems.Create_Stratagem_Graph(CAR_df)
# TODO: RC-TR-RC (top right square)

# Create dashboard layout 
CAR_dashapp.layout = html.Div([

    # Div Level 1 - Title
    html.Div( children = "Most Recent Mission Stats", className="CARdashapp-Div--title" ),

    # Div Level 1 - Main body
    html.Div( children = [
        
        # Div Level 2 - slider row
        html.Div( children = [
            # slider
            dcc.Slider(
                min=-(num_dfs_loaded-1),
                max=0,
                step=1,
                marks={i: f"Last Career Log" if i == 0 else str(i) + " Logs" for i in range(-(num_dfs_loaded),1)},
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

                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - 2nd gridbox
                html.Div( children=[
                    
                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - 3rd gridbox
                html.Div( children=[
                    
                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - 4th gridbox
                html.Div( children=[
                    
                ], className="CARdashapp-Div--gridbox")
            ], className="CARdashapp-Div--Top-row"),
            # Div Level 3 - Bottom row
            html.Div( children=[
                
                # Div Level 4 - left grid box
                html.Div( children=[
                    
                ], className="CARdashapp-Div--gridbox"),

                # Div Level 4 - right grid box
                html.Div( children=[
                    
                ], className="CARdashapp-Div--gridbox")
            ], className="CARdashapp-Div--Bottom-row"),
        ], className="CARdashapp--graphs-row"),
    ], className="CARdashapp-Div--main-box")
], className="CARdashapp-Div--base")

################################################################
################################################################
# Execution: CAR_dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    CAR_dashapp.run(debug=True,port=8050)