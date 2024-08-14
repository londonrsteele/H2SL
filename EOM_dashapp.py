import sys
from dash import *
from graphing import (stat_scraper, accuracy, survivor, dotplot, linegraph, metadata)
import pandas as pd
import plotly.express as pltxp
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

# Use Stat_Scraper to get most recent 10 (or less) files
list_of_old_filenames = scraper.get_last10_filenames("EOM", sys.argv[1])

# Use Stat_Scraper to load most recent 10 files and store how many were loaded
list_of_10_dfs = scraper.load_files(list_of_old_filenames)
num_dfs_loaded = len(list_of_10_dfs)

# Use Stat_Scraper to get the min and  max stats of all time - used with linechart
# Called here instead of in linechart callback so files are only scraped 1x
min_alltime, max_alltime = scraper.get_min_and_max_stats_alltime("EOM")

# Use Stat_Scraper to get the min and max stats of last 10 missions - used with dotplot
# Called here instead of in dotplot callback so files are only scraped 1x
min_last10, max_last10 = scraper.get_min_and_max_stats_last10(list_of_10_dfs, "EOM")

# Create static figures
accuracy_fig = accuracy.Create_Accuracy_Graph(EOM_df)
survivor_fig = survivor.Create_Survivor_Graph(EOM_df)

# Create dashboard layout 
EOM_dashapp.layout = html.Div([

    # Div Level 1 - Title
    html.Div( children = "Most Recent Mission Stats", className="EOMdashapp-Div--title" ),

    # Div Level 1 - Main Column - Grid
    html.Div( children = [
        
        # Div Level 2 - Left/Middle column
        html.Div( children= [

            # Div Level 3 - Top row
            html.Div( children = [

                # Div Level 4 - Left gridbox
                html.Div( children = [
                    # accuracy-graph (static)
                    dcc.Graph(id="accuracy-graph",
                        figure=accuracy_fig)
                ], className="EOMdashapp-Div--gridbox"),

                # Div Level 4 - Right gridbox
                html.Div( children = [
                    # survivor-graph (static)
                    dcc.Graph(id="survivor-graph",
                        figure=survivor_fig)
                ], className="EOMdashapp-Div--gridbox"),
            ], className="EOMdashapp-Div--LMC-Top-row"),

            # Div Level 3 - Middle/Bottom row
            html.Div( children = [
                
                # Div Level 4 - Top row
                html.Div( children = [
                    # line-graph (interactive with dropdown)
                    dcc.Graph(id="line-graph")
                ], className="EOMdashapp-Div--gridbox"),

                # Div Level 4 - Bottom row
                html.Div( children = [
                    # dropdown - for line-graph
                    dcc.Dropdown(metadata.list_of_EOM_strats, "Kills", clearable=False, id="dropdown")
                ], className="EOMdashapp-Div--dropdown"),
                
            ], className="EOMdashapp-Div--LMC-Bottom-row"),
        ], className="EOMdashapp-Div--LeftMiddle-column"),
        
        # Div Level 2 - Right column
        html.Div( children= [

            # Div Level 3 - Top row
            html.Div( children = [
                # slider - for dotplot
                dcc.Slider(
                    min=-(num_dfs_loaded-1),
                    max=0,
                    step=1,
                    marks={i: f"Last Mission" if i == 0 else str(i) + " Games" for i in range(-(num_dfs_loaded-1),1)},
                    value=0,
                    id="slider"
                )
            ], className="EOMdashapp-Div--slider"),

            # Div Level 3 - Bottom row
            html.Div( children = [
                # dotplot (interactive with slider)
                dcc.Graph(id="dotplot-graph")
            ], className="EOMdashapp-Div--gridbox"),
        ], className="EOMdashapp-Div--Right-column"),
    ], className="EOMdashapp-Div--main-box")
], className="EOMdashapp-Div--base")


################################################################
# callback: create linechart
################################################################
@EOM_dashapp.callback(
    Output("line-graph", "figure"),
    Input("dropdown", "value")
)
def update_linegraph(selected_stat):
    stats_last10 = scraper.get_last10_stat_list(selected_stat, "EOM", list_of_10_dfs)
    stat_alltime_max = scraper.get_max_stat_from_df(selected_stat, "EOM", max_alltime)
    fig = linegraph.Create_LineGraph(selected_stat, stats_last10, stat_alltime_max)
    return fig

################################################################
# callback: create dotplot
################################################################
@EOM_dashapp.callback(
    Output("dotplot-graph", "figure"),
    Input("slider", "value")
)
def update_dotplot(selected_game):
    minmax_norm_of_selected_game = scraper.minmax_normalize(min_last10, max_last10, list_of_10_dfs[selected_game], "EOM")
    fig = dotplot.Create_EOM_Dotplot(minmax_norm_of_selected_game)
    return fig


################################################################
################################################################
# Execution: EOM_dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    EOM_dashapp.run(debug=True,port=8050)