import sys
from dash import *
from graphing import (stat_scraper, accuracy, survivor, dotplot, linegraph, metadata)

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

# Create dashboard layout 
EOM_dashapp.layout = html.Div([

    # Div Level 1 - Title
    html.Div( children = "Most Recent Mission Stats", className="EOMdashapp-Div--title" ),

    # Div Level 1 - Main Column - Grid
    html.Div( children = [
        
        # Div Level 2 - slider row
        html.Div( children = [
            # slider
            dcc.Slider(
                min=-(num_dfs_loaded-1),
                max=0,
                step=1,
                marks={i: f"Last Mission" if i == 0 else str(i) + " Games" for i in range(-(num_dfs_loaded-1),1)},
                value=0,
                id="slider"
            )
        ], className="EOMdashapp-Div--slider"),

        # Div Level 2 - graphs row
        html.Div( children= [

            # Div Level 3 - Left/Middle Column
            html.Div( children = [

                # Div Level 4 - Top row
                html.Div( children = [

                    # Div Level 5 - Left gridbox
                    html.Div( children = [
                        # accuracy-graph (interactive with slider)
                        dcc.Graph(id="accuracy-graph")
                    ], className="EOMdashapp-Div--gridbox"),

                    # Div Level 5 - Right gridbox
                    html.Div( children = [
                        # survivor-graph (interactive with slider)
                        dcc.Graph(id="survivor-graph")
                    ], className="EOMdashapp-Div--gridbox"),
                ], className="EOMdashapp-Div--LMC-Top-row"),

                # Div Level 4 - Middle/Bottom row
                html.Div( children = [
                    
                    # Div Level 5 - Top row
                    html.Div( children = [
                        # line-graph (interactive with dropdown)
                        dcc.Graph(id="line-graph")
                    ], className="EOMdashapp-Div--gridbox"),

                    # Div Level 5 - Bottom row
                    html.Div( children = [
                        # dropdown - for line-graph
                        dcc.Dropdown(metadata.list_of_EOM_strats, "Kills", clearable=False, id="dropdown")
                    ], className="EOMdashapp-Div--dropdown"),
                    
                ], className="EOMdashapp-Div--LMC-Bottom-row"),
            ], className="EOMdashapp-Div--LeftMiddle-column"),

            # Div Level 3 - Right column
            html.Div( children= [
                html.Div( children = [
                    # dotplot (interactive with slider)
                    dcc.Graph(id="dotplot-graph")
                ], className="EOMdashapp-Div--gridbox"), 
            ], className="EOMdashapp-Div--Right-column"),
        ], className="EOMdashapp-Div--graphs-row")
    ], className="EOMdashapp-Div--main-box")
], className="EOMdashapp-Div--base")


################################################################
# callback: create accuracy
################################################################
@EOM_dashapp.callback(
    Output("accuracy-graph", "figure"),
    Input("slider", "value")
)
def update_accuracy(selected_game):
    fig = accuracy.Create_Accuracy_Graph(list_of_10_dfs[abs(selected_game)], "EOM")
    return fig

################################################################
# callback: create survival
################################################################
@EOM_dashapp.callback(
    Output("survivor-graph", "figure"),
    Input("slider", "value")
)
def update_survivor(selected_game):
    fig = survivor.Create_Survivor_Graph(list_of_10_dfs[abs(selected_game)])
    return fig

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
    minmax_norm_of_selected_game = scraper.minmax_normalize(min_last10, max_last10, list_of_10_dfs[abs(selected_game)], "EOM")
    fig = dotplot.Create_EOM_Dotplot(minmax_norm_of_selected_game)
    return fig


################################################################
################################################################
# Execution: EOM_dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    EOM_dashapp.run(debug=True,port=8050)