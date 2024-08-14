import pandas as pd
import plotly.graph_objects as pltgo
import plotly.express as pltxp
from graphing import metadata

def Create_LineGraph(selected_stat, stats_last10, max_all_time):
    # Make list of labels for x axis, from -i -> Last Mission (0)
    # Note: i may not == 10, may be < 10!
    x_list = []
    for i in range(-len(stats_last10)+1,0):
        if i == -1:
            x_list.append(str(i) +"\nGame")
        else:
            x_list.append(str(i) +"\nGames")
    x_list.append("Last Mission")
    # Make list to represent max_all_time line
    max_all_time_list = []
    for i in range(-len(stats_last10)+1,1):
        max_all_time_list.append(max_all_time)
    # Make list to represent average line
    average_list = []
    average = sum(stats_last10)/len(stats_last10)
    for i in range(-len(stats_last10)+1,1):
        average_list.append(int(average))
    
    # Create the Figure
    fig = pltgo.Figure()
    fig.add_trace(
        pltgo.Scatter(
            name="All-time Max",
            x=x_list,
            y=max_all_time_list,
            mode="lines",
            line=dict(color=metadata.dict_of_colors["yellow"], width=3),
            hovertemplate = "All-time Max: %{y}<extra></extra>"
        )    
    )
    fig.add_trace(
        pltgo.Scatter(
            name="Stat Over Time",
            x=x_list,
            y=stats_last10,
            mode="lines+markers",
            line=dict(color=metadata.dict_of_colors["white"], width=5),
            hovertemplate = "Game Stat: %{y}<extra></extra>"
        )
    )
    fig.add_trace(
        pltgo.Scatter(
            name="Last "+ str(len(stats_last10)) + " Games Average",
            x=x_list,
            y=average_list,
            mode="lines",
            line=dict(color=metadata.dict_of_colors["dark-yellow"], width=5),
            hovertemplate = str(len(stats_last10))+"-Game Avg: %{y}<extra></extra>"
        )
    )
    fig.update_layout(
        title="<b>Statistics Over Last " + str(len(stats_last10)) + " Games</b>",
        title_x=0.5,
        xaxis_title="<b>Last " + str(len(stats_last10)) + " Games</b>",
        yaxis_title="<b>" +  selected_stat + "</b>",
        font=dict(
                family="monospace",
                size=25,
                color=metadata.dict_of_colors["white"]
            ),
        hovermode="x unified",
        hoverlabel={
            "font_size":18
        },
        paper_bgcolor=metadata.dict_of_colors["light-black"],
        plot_bgcolor=metadata.dict_of_colors["black"],
        legend=dict(
            # x=0.3,
            # y=0.1,
            # xref="paper",
            # yref="container",
            # orientation="h",
            font=dict(
                color=metadata.dict_of_colors["white"]
            )
        )
    )
    fig.update_xaxes(
        ticks="outside",
        showspikes=True, 
        linecolor=metadata.dict_of_colors["black"], 
        gridcolor=metadata.dict_of_colors["light-black"]
    )
    fig.update_yaxes(
        ticks="outside", 
        linecolor=metadata.dict_of_colors["black"], 
        gridcolor=metadata.dict_of_colors["light-black"]
    )
    fig.update_traces(textposition="top center")
    return fig