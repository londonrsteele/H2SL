import plotly.graph_objects as pltgo
from graphing import metadata

def Create_Accuracy_Dataset(df, type):
    if type == "EOM":
        # EOM Accuracy = x%
        # EOM Shots Fired = y
        # EOM Shots Hit = z
        shots_data = {
            "x" : [0, 0],
            "Shots" : [df["eom_shots_fired"], df["eom_shots_hit"]],
            "labels" : ["Shots Fired", "Shots Hit"],
            "Accuracy": str("Accuracy = " + str(df["eom_accuracy"][0]) + "%")
        }
    elif type == "CAR":
        # CAR Shots Fired = y
        # CAR Shots Hit = z
        # CAR Accuracy = CAR Shots Fired / CAR Shots Hit
        if(df["CAR_shots_fired"][0] == 0):
            accuracy = 0
        else:
            accuracy = int(df["CAR_shots_hit"][0]/df["CAR_shots_fired"][0]*100)

        shots_data = {
            "x" : [0, 0],
            "Shots" : [df["CAR_shots_fired"], df["CAR_shots_hit"]],
            "labels" : ["Shots Fired", "Shots Hit"],
            "Accuracy": str("Accuracy = " + str(accuracy) + "%")
        }

    return shots_data
   

def Create_Accuracy_Graph(df, type):
    # Create dataset to use for graph
    shots_data=Create_Accuracy_Dataset(df, type)

    # Create figure
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
            yaxis_title = "<b><br>Shots</b>",
            font=dict(
                family="sans-serif",
                size=18,
                color=metadata.dict_of_colors["white"]
            ),
            hoverlabel={
                "font_size":14
            },
            paper_bgcolor=metadata.dict_of_colors["black"],
            plot_bgcolor=metadata.dict_of_colors["light-black"],
            legend=dict(
                font=dict(
                    color=metadata.dict_of_colors["white"]
                )
            )
        )
    )
    fig.update_xaxes(
        showticklabels=False, 
        linecolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["grey"]
    )
    fig.update_yaxes(
        ticks="outside", 
        gridcolor=metadata.dict_of_colors["grey"],
        linecolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["grey"]
    )
    fig.update_traces(textposition="outside", width=0.5)
    return fig