import plotly.graph_objects as pltgo
from graphing import metadata

def Create_Survivor_Graph(EOM_df):
    survivor_data = {
        "x_labels" : ["Deaths", "Stims Used"],
        "x" : [0,1],
        "stats" : [EOM_df["eom_deaths"][0], EOM_df["eom_stims_used"][0]],
    }
    
    fig = pltgo.Figure(
        data=[
            pltgo.Bar(
                name="Survival Stats",
                x=survivor_data["x"],
                y=survivor_data["stats"],
                marker_color=metadata.dict_of_colors["dark-yellow"],
                customdata=survivor_data["x_labels"],
                hovertemplate="%{customdata}: %{y}<extra></extra>"
            )
        ],
        layout=pltgo.Layout(
            title="<b>Survival Stats</b>",
            title_x = 0.5,
            xaxis_title = "<b>Survival Stat</b>",
            yaxis_title = "<b>Count</b>",
            font=dict(
                family="monospace",
                size=25,
                color=metadata.dict_of_colors["white"]
            ),
            hoverlabel={
                "font_size":18
            },
            hovermode="x",
            xaxis=dict(
                tickmode = "array",
                tickvals=survivor_data["x"],
                ticktext=survivor_data["x_labels"]
            ),
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
    fig.update_xaxes(ticks="outside", linecolor=metadata.dict_of_colors["black"])
    fig.update_yaxes(ticks="outside", gridcolor=metadata.dict_of_colors["light-black"])
    fig.update_traces(width=0.5)
    return fig