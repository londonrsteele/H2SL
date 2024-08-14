import plotly.graph_objects as pltgo
from graphing import metadata

def Create_Accuracy_Graph(EOM_df):
    # EOM Accuracy = x%
    # EOM Shots Fired = y
    # EOM Shots Hit = z
    shots_data = {
        "x" : [0, 0],
        "Shots" : [EOM_df["eom_shots_fired"], EOM_df["eom_shots_hit"]],
        "labels" : ["Shots Fired", "Shots Hit"],
        "Accuracy": str("Accuracy = " + str(EOM_df["eom_accuracy"][0]) + "%")
    }
    
    fig = pltgo.Figure(
        data=[
            pltgo.Bar(
                name="Shots Fired",
                x=shots_data["x"],
                y=shots_data["Shots"][0],
                offsetgroup=0,
                marker_color=metadata.dict_of_colors["grey"],
                hovertemplate = "Shots Fired: %{y}<extra></extra>"
            ),
            pltgo.Bar(
                name="Shots Hit",
                x=shots_data["x"],
                y=shots_data["Shots"][1],
                offsetgroup=0,
                marker_color=metadata.dict_of_colors["dark-yellow"],
                hovertemplate = "Shots Hit: %{y}<extra></extra>",
                text="<b>"+str(shots_data["Accuracy"])+"</b>",
                textfont=dict(
                    color=metadata.dict_of_colors["white"],
                    family="monospace",
                    size=25
                ),
                marker_pattern_shape="/"
            )
        ],
        layout=pltgo.Layout(
            title="<b>Shots Accuracy</b>",
            title_x = 0.5,
            yaxis_title = "<b>Shots</b>",
            font=dict(
                family="monospace",
                size=25,
                color=metadata.dict_of_colors["white"]
            ),
            hoverlabel={
                "font_size":18
            },
            paper_bgcolor=metadata.dict_of_colors["light-black"],
            plot_bgcolor=metadata.dict_of_colors["black"],
            legend=dict(
                x=0.3,
                y=0.1,
                xref="paper",
                yref="container",
                orientation="h",
                font=dict(
                    color=metadata.dict_of_colors["white"]
                )
            )
        )
    )
    fig.update_xaxes(showticklabels=False, linecolor=metadata.dict_of_colors["black"])
    fig.update_yaxes(ticks="outside", gridcolor=metadata.dict_of_colors["light-black"])
    fig.update_traces(textposition="outside", width=0.5)
    return fig