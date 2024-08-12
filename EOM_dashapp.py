import sys
from dash import *
from graphing import (stat_scraper, accuracy, survivor, dotplot)
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

# Use Stat_Scraper to load most recent 10 files
list_of_10_dfs = scraper.load_files(list_of_old_filenames)

# Use Stat_Scraper to get the max stats of last 10 missions
min_last10, max_last10 = scraper.get_min_and_max_stats_last10(list_of_10_dfs, "EOM")

# Use Stat_Scraper to get the min and  max stats of all time
min_alltime, max_alltime = scraper.get_min_and_max_stats_alltime("EOM")

# Use Stat_Scraper to get the last10 minmax normalized numeric stats (list)
last10_minmax_EOM_list = scraper.minmax_normalize(min_last10, max_last10, EOM_df, "EOM")

# Use Stat_Scraper to get the alltime minmax normalized numeric stats (list)
alltime_minmax_EOM_list = scraper.minmax_normalize(min_alltime, max_alltime, EOM_df, "EOM")




# Create figures
accuracy_fig = accuracy.Create_Accuracy_Graph(EOM_df)
survivor_fig = survivor.Create_Survivor_Graph(EOM_df)
dotplot_fig = dotplot.Create_EOM_Dotplot(alltime_minmax_EOM_list)

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
            dcc.Graph(id="dotplot-graph",
                      figure=dotplot_fig),
 
        ], style={"display":"flex", "flexDirection":"column"})
    ], style={"display":"flex", "flexDirection":"row"})
], style={"display":"flex", "flexDirection":"column"})

################################################################
################################################################
# Execution: EOM_dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    EOM_dashapp.run(debug=True,port=8050)