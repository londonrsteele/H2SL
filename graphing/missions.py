import plotly.graph_objects as pltgo
from graphing import metadata

def Create_Missions_Graph(list_of_10dfs, selected_log):
    # Set selected log to CAR_df, set previous log if exists
    CAR_df = list_of_10dfs[selected_log]
    if len(list_of_10dfs) > selected_log+1:
        previous_log = list_of_10dfs[selected_log+1]
        # Get the previous log's stats
        previous_log_wins = previous_log["CAR_missions_won"][0]
        previous_log_played = previous_log["CAR_missions_played"][0]
        if previous_log_played != 0:
            previous_log_percent_won = int(previous_log_wins/previous_log_played*100)
        else:
            previous_log_percent_won = 0
    # if no previous log file exists, set previous_log_wins and previous_log_percent = 0
    else:
        previous_log_wins = 0
        previous_log_percent_won = 0
    
    # Get current log's stats
    CAR_wins = CAR_df["CAR_missions_won"][0]
    CAR_played = CAR_df["CAR_missions_played"][0]
    if CAR_played != 0:
        percent_won = int(CAR_wins/CAR_played*100)
    else:
        percent_won = 0
    
    # Create figure
    fig = pltgo.Figure()
    # Raw games number
    fig.add_trace(
        pltgo.Indicator(
            title={"text":"Missions Won"},
            mode="gauge+number+delta",
            domain={ "x": [0,1], "y": [0.6,1]},
            value=CAR_wins,
            gauge={
                "axis": {"range": [0, CAR_played], "tickcolor": metadata.dict_of_colors["grey"]},
                "bar": {"color" : metadata.dict_of_colors["yellow"]}
            },
            delta={
                "reference": previous_log_wins,
                "relative": False
            }
        )
    )
    # Percent games number
    fig.add_trace(
        pltgo.Indicator(
            title={"text":"Percent Won"},
            mode="gauge+number+delta",
            domain={ "x": [0,1], "y": [0,0.4]},
            value=percent_won,
            gauge={
                "axis": {"range": [0, 100], "tickcolor": metadata.dict_of_colors["grey"]},
                "bar": {"color" : metadata.dict_of_colors["yellow"]}
            },
            delta={
                "reference": previous_log_percent_won,
                "relative": False,
                "suffix": "%"
            }
        )
    )
    fig.update_layout(
        font=dict(
                family="sans-serif",
                size=25,
                color=metadata.dict_of_colors["white"]
            ),
        paper_bgcolor=metadata.dict_of_colors["black"],
        plot_bgcolor=metadata.dict_of_colors["light-black"],
    )
    return fig