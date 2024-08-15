import sys
from dash import *
import dash_daq as daq
from graphing import (accuracy, survivor, linegraph,
                    missions, kill, stratagems,
                    metadata, stat_scraper)

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

# Use Stat_Scraper to get most recent 10 (or less) files
list_of_old_EOM_filenames = scraper.get_last10_filenames("EOM", sys.argv[1])
list_of_old_CAR_filenames = scraper.get_last10_filenames("CAR", sys.argv[2])

# Use Stat_Scraper to load most recent 10 files and store how many were loaded
list_of_10_EOM_dfs = scraper.load_files(list_of_old_EOM_filenames)
num_EOM_dfs_loaded = len(list_of_10_EOM_dfs)
list_of_10_CAR_dfs = scraper.load_files(list_of_old_CAR_filenames)
num_CAR_dfs_loaded = len(list_of_10_CAR_dfs)

# Use Stat_Scraper to get the min and  max stats of all time - used with linechart
# Called here instead of in linechart callback so files are only scraped 1x
min_alltime_EOM, max_alltime_EOM = scraper.get_min_and_max_stats_alltime("EOM")
min_alltime_CAR, max_alltime_CAR = scraper.get_min_and_max_stats_alltime("CAR")

# Create dashboard layout 
dashapp.layout = html.Div([

    # Div Level 1 - Title
    html.Div( children = "Helldivers 2 Stats Dashboard", className="dashapp-Div--title" ),

    # Div Level 1 - Main Column - Grid
    html.Div( children = [
        
        # Div Level 2 - slider row
        html.Div( children = [
            # slider
            dcc.Slider(
                min=-(num_EOM_dfs_loaded-1),
                max=0,
                step=1,
                marks={i: f"Last Mission" if i == 0 else str(i) + " Games" for i in range(-(num_EOM_dfs_loaded-1),1)},
                value=0,
                id="slider"
            )
        ], className="dashapp-Div--slider"),

        # Div Level 2 - graphs row
        html.Div( children= [

            # Div Level 3 - Top Row
            html.Div( children = [

                # Div Level 4 - Top row - 1st gridbox
                html.Div( children = [
                    dcc.Graph(id="survivor-fig")
                ],className="dashapp-Div--TopRow-gridbox"),
                
                # Div Level 4 - Top row - 2nd gridbox
                html.Div( children = [
                    dcc.Graph(id="accuracy-fig")
                ],className="dashapp-Div--TopRow-gridbox"),
                
                # Div Level 4 - Top row - 3rd gridbox
                html.Div( children = [
                    dcc.Graph(id="missions-fig")
                ],className="dashapp-Div--TopRow-gridbox"),
                
                # Div Level 4 - Top row - 4th gridbox
                html.Div( children = [
                    dcc.Graph(id="stratagems-fig")
                ],className="dashapp-Div--TopRow-gridbox")
            ], className="dashapp-Div--TopRow"),

            # Div Level 3 - Bottom Row
            html.Div( children= [

                # Div Level 4 - Left gridbox
                html.Div( children = [
                    dcc.Graph(id="kills-fig")
                ], className="dashapp-Div--gridbox"), 
                
                # Div Level 4 - Middle gridbox
                html.Div( children = [
                    
                    # Div Level 5 - Line Graph
                    html.Div( children=[
                        dcc.Graph(id="line-graph")
                    ], className="dashapp-Div--gridbox"),

                    # Div Level 5 - Dropdown
                    html.Div( children = [
                        # dropdown - for line-graph
                        dcc.Dropdown(metadata.list_of_EOM_strats, "Kills", clearable=False, id="dropdown")
                    ], className="dashapp-Div--dropdown"),
                ], className="dashapp-Div--MiddleBox"), 
                
                # Div Level 4 - Right gridbox
                html.Div( children = [

                        # Div Level 5 - LED Display (TOP)
                        html.Div( children= [
                            daq.LEDDisplay(
                                id="deaths-LED-display",
                                label="Deaths",
                                value="0",
                                color=metadata.dict_of_colors["yellow"],
                                backgroundColor=metadata.dict_of_colors["light-black"],
                                size=64
                            )
                        ], className="CARdashapp-Div--LeftBox"),
                        
                        # Div Level 5 - LED Display (2nd)
                        html.Div( children=[
                            daq.LEDDisplay(
                                id="extractions-LED-display",
                                label="Successful Extractions",
                                value="0",
                                color=metadata.dict_of_colors["light-blue"],
                                backgroundColor=metadata.dict_of_colors["light-black"],
                                size=64
                            )
                        ], className="CARdashapp-Div--gridbox"),
                       
                        # Div Level 5 - LED Display (3rd)
                        html.Div( children= [
                            daq.LEDDisplay(
                                id="orbitals-LED-display",
                                label="Orbitals Used",
                                value="0",
                                color=metadata.dict_of_colors["white"],
                                backgroundColor=metadata.dict_of_colors["light-black"]
                            )
                        ], className="CARdashapp-Div--gridbox"),
                        
                        # Div Level 5 - LED Display (4th)
                        html.Div( children= [
                            daq.LEDDisplay(
                                id="mission-LED-display",
                                label="In-Mission Time",
                                value="000:00:00",
                                color=metadata.dict_of_colors["yellow"],
                                backgroundColor=metadata.dict_of_colors["light-black"]
                            )
                        ], className="CARdashapp-Div--gridbox"),
                        
                        # Div Level 5 - LED Display (BOTTOM)
                        html.Div( children=[
                            daq.LEDDisplay(
                                id="xp-LED-display",
                                label="Total XP Earned",
                                value="0",
                                color=metadata.dict_of_colors["red"],
                                backgroundColor=metadata.dict_of_colors["light-black"]
                            )
                        ], className="CARdashapp-Div--gridbox")
                    # ], className="dashapp-Div--RightBox-Right")
                ], className="dashapp-Div--RightBox"), 
            ], className="dashapp-Div--BottomRow"),
        ], className="dashapp-Div--graphs-row")
    ], className="dashapp-Div--main-box")
], className="dashapp-Div--base")

################################################################
# callback: create accuracy - EOM data
################################################################
@dashapp.callback(
    Output("accuracy-fig", "figure"),
    Input("slider", "value")
)
def update_accuracy(selected_game):
    fig = accuracy.Create_Accuracy_Graph(list_of_10_EOM_dfs[abs(selected_game)], "EOM")
    return fig

################################################################
# callback: create kill - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("kills-fig", "figure"),
    Input("slider", "value")
)
def update_kills(selected_game):
    fig = kill.Create_Kill_Graph(list_of_10_CAR_dfs[0])
    return fig

################################################################
# callback: create stratagem - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("stratagems-fig", "figure"),
    Input("slider", "value")
)
def update_stratagems(selected_game):
    fig = stratagems.Create_Stratagem_Graph(list_of_10_CAR_dfs[0])
    return fig

################################################################
# callback: create survival - EOM data
################################################################
@dashapp.callback(
    Output("survivor-fig", "figure"),
    Input("slider", "value")
)
def update_survivor(selected_game):
    fig = survivor.Create_Survivor_Graph(list_of_10_EOM_dfs[abs(selected_game)])
    return fig

################################################################
# callback: create missions - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("missions-fig", "figure"),
    Input("slider", "value")
)
def update_missions(selected_game):
    fig = missions.Create_Missions_Graph(list_of_10_CAR_dfs, 0)
    return fig

################################################################
# callback: create linechart - EOM data
################################################################
@dashapp.callback(
    Output("line-graph", "figure"),
    Input("dropdown", "value")
)
def update_linegraph(selected_stat):
    stats_last10 = scraper.get_last10_stat_list(selected_stat, "EOM", list_of_10_EOM_dfs)
    stat_alltime_max = scraper.get_max_stat_from_df(selected_stat, "EOM", max_alltime_EOM)
    fig = linegraph.Create_LineGraph(selected_stat, stats_last10, stat_alltime_max)
    return fig

################################################################
# callback: create deaths - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("deaths-LED-display", "value"),
    Input("slider", "value")
)
def update_deaths(selected_game):
    deaths = list_of_10_CAR_dfs[0]["CAR_deaths"][0]
    return deaths

################################################################
# callback: create orbitals - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("orbitals-LED-display", "value"),
    Input("slider", "value")
)
def update_orbitals(selected_game):
    orbitals = list_of_10_CAR_dfs[0]["CAR_orbitals_used"][0]
    return orbitals

################################################################
# callback: create in-mission time - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("extractions-LED-display", "value"),
    Input("slider", "value")
)
def update_inmission_time(selected_game):
    successful_extractions = list_of_10_CAR_dfs[0]["CAR_successful_extractions"][0]
    return successful_extractions

################################################################
# callback: create in-mission time - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("mission-LED-display", "value"),
    Input("slider", "value")
)
def update_inmission_time(selected_game):
    inmission_time = list_of_10_CAR_dfs[0]["CAR_inmission_time"][0]
    return inmission_time

################################################################
# callback: create total xp earned - CAR data (most recent only)
################################################################
@dashapp.callback(
    Output("xp-LED-display", "value"),
    Input("slider", "value")
)
def update_total_xp_earned(selected_game):
    total_xp_earned = list_of_10_CAR_dfs[0]["CAR_total_XP_earned"][0]
    return total_xp_earned


################################################################
################################################################
# Execution: dashapp.py __main__
################################################################
################################################################
if __name__ == "__main__":
    dashapp.run(debug=True,port=8052)