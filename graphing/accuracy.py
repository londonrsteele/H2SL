import plotly.graph_objects as pltgo

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
                marker_color="#024a70",
                text=shots_data["Shots"][0]
            ),
            pltgo.Bar(
                name="Shots Hit",
                x=shots_data["x"],
                y=shots_data["Shots"][1],
                offsetgroup=0,
                marker_color="#051c2c",
                text=shots_data["Shots"][1]
            )
        ],
        layout=pltgo.Layout(
            title="Shots Accuracy",
            yaxis_title = "Shots"
        ),
    )
    fig.add_annotation(xref="paper", yref="paper", 
                        x=0.75, y=(EOM_df["eom_accuracy"][0]/100),
                        text=shots_data["Accuracy"],
                        arrowhead=1, arrowsize=1, arrowwidth=2,
                        font=dict(
                            size=18,
                            color="White"
                        ),
                        arrowcolor="White"
                        )
    fig.update_xaxes(showticklabels=False)
    fig.update_traces(textposition="inside")
    return fig