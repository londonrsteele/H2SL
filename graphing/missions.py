import plotly.graph_objects as pltgo
from graphing import metadata

def Create_Missions_CAR_Graph(list_of_10dfs, selected_log):
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
        previous_log_samples_collected = previous_log["CAR_samples_collected"][0]
        previous_log_objectives_completed = previous_log["CAR_objectives_completed"][0]
    # if no previous log file exists, set previous stats = 0
    else:
        previous_log_wins = 0
        previous_log_percent_won = 0
        previous_log_samples_collected = 0
        previous_log_objectives_completed = 0

    # Get current log's stats
    CAR_wins = CAR_df["CAR_missions_won"][0]
    CAR_played = CAR_df["CAR_missions_played"][0]
    if CAR_played != 0:
        CAR_percent_won = int(CAR_wins/CAR_played*100)
    else:
        CAR_percent_won = 0
    CAR_samples_collected = CAR_df["CAR_samples_collected"][0]
    CAR_objectives_completed = CAR_df["CAR_objectives_completed"][0]

    # Create figure
    fig = pltgo.Figure()
    # Raw games number
    fig.add_trace(
        pltgo.Indicator(
            title={"text":"Missions Won"},
            mode="gauge+number+delta",
            domain={ "x": [0,0.6], "y": [0.55,1]},
            value=CAR_wins,
            gauge={
                "axis": {
                    "range": [0, CAR_played], 
                    "tickcolor": metadata.dict_of_colors["grey"], 
                    "tickfont": {"size": 14}
                },
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
            domain={ "x": [0, 0.6], "y": [0,0.45]},
            value=CAR_percent_won,
            gauge={
                "axis": {
                    "range": [0, 100], 
                    "tickcolor": metadata.dict_of_colors["grey"], 
                    "tickfont": {"size": 14}
                },
                "bar": {"color" : metadata.dict_of_colors["yellow"]}
            },
            number={
                "suffix": "%"
            },
            delta={
                "reference": previous_log_percent_won,
                "relative": False,
                "suffix": "%"
            }
        )
    )
    # Successful Extractions (number and delta)
    fig.add_trace(
        pltgo.Indicator(
            title={"text":"Samples Collected"},
            mode="number+delta",
            domain={ "x": [0.7,1], "y": [0.55,1]},
            value=CAR_samples_collected,
            delta={
                "reference": previous_log_samples_collected,
                "relative": False,
            }
        )
    )
    # Objectives completed (number and delta)
    fig.add_trace(
        pltgo.Indicator(
            title={"text":"Objectives Completed"},
            mode="number+delta",
            domain={ "x": [0.7,1], "y": [0,0.45]},
            value=CAR_objectives_completed,
            delta={
                "reference": previous_log_objectives_completed,
                "relative": False,
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


def Create_Missions_Graph(list_of_10dfs, selected_log):
    # Set selected log to CAR_df
    CAR_df = list_of_10dfs[selected_log]
    
    # Get current log's stats
    wins = CAR_df["CAR_missions_won"][0]
    played = CAR_df["CAR_missions_played"][0]
    if played != 0:
        percent_won = int(wins/played*100)
    else:
        percent_won = 0
   
    # Create figure
    fig = pltgo.Figure()
    # Raw games number
    fig.add_trace(
        pltgo.Indicator(
            title={"text":"Missions Won"},
            mode="gauge+number",
            domain={ "x": [0,1], "y": [0,1]},
            value=wins,
            gauge={
                "axis": {
                    "range": [0, played], 
                    "tickcolor": metadata.dict_of_colors["grey"], 
                    "tickfont": {"size": 14}
                },
                "bar": {"color" : metadata.dict_of_colors["yellow"]}
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
    fig.add_annotation(
        x=0.45,
        y=0.0,
        text=str(percent_won)+"%",
        showarrow=False,
        xanchor="left",
        font={
            "size": 14
        }
    )
    return fig