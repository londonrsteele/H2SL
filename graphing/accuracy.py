import plotly.graph_objects as pltgo
import plotly.express as pltxp

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
                marker_color=pltxp.colors.qualitative.G10[8]
            ),
            pltgo.Bar(
                name="Shots Hit",
                x=shots_data["x"],
                y=shots_data["Shots"][1],
                offsetgroup=0,
                marker_color=pltxp.colors.qualitative.G10[8],
                text=shots_data["Accuracy"],
                textfont=dict(
                    color="white",
                    family="monospace",
                    size=25
                ),
                marker_pattern_shape="/"
            )
        ],
        layout=pltgo.Layout(
            title="Shots Accuracy",
            xaxis_title = "Shots",
            font=dict(
                family="monospace",
                size=25
            )
        )
    )
    fig.update_xaxes(showticklabels=False)
    fig.update_traces(textposition="outside", width=0.7)
    return fig