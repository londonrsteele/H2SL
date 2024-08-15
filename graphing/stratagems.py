import plotly.graph_objects as pltgo
from graphing import metadata

def Create_Stratagem_Graph(CAR_df):
    # CAR total stratagems used
    # CAR defensive stratagems used
    # CAR eagle stratagems used
    # CAR supply stratagems used
    # CAR reinforce stratagems used
    stratagems_data = {
        "x_labels" : ["Total", "Defensive", "Eagle", "Supply", "Reinforce"],
        "x": [0,1,2,3,4],
        "stats" : [ CAR_df["CAR_total_strats_used"][0], CAR_df["CAR_def_strats_used"][0], 
                   CAR_df["CAR_eagle_strats_used"][0], CAR_df["CAR_supply_strats_used"][0],
                   CAR_df["CAR_reinforce_strats_used"][0]
                ],
        "colors": [metadata.dict_of_colors["yellow"], metadata.dict_of_colors["light-blue"],
                   metadata.dict_of_colors["white"], metadata.dict_of_colors["red"],
                   metadata.dict_of_colors["dark-yellow"]
                ]
    }

    # fig = pltxp.bar(stratagems_data, x="x_labels", y="stats",
    #                 labels={"x_labels":"Stratagems Used", "stats":"Count"},
    #                 text_auto=True)
    fig = pltgo.Figure(
        data=[
            pltgo.Bar(
                name="Stratagems",
                x=stratagems_data["x"],
                y=stratagems_data["stats"],
                marker_color=stratagems_data["colors"],
                customdata=stratagems_data["x_labels"],
                hovertemplate="%{customdata}: %{y}<extra></extra>"
            )
        ],
        layout=pltgo.Layout(
            title="<b>Stratagems Used</b>",
            title_x = 0.5,
            xaxis_title = "<b>Stratagem Class<br></b>",
            yaxis_title = "<b><br>Count</b>",
            font=dict(
                family="sans-serif",
                size=25,
                color=metadata.dict_of_colors["white"]
            ),
            hoverlabel={
                "font_size":18
            },
            hovermode="x",
            xaxis=dict(
                tickmode = "array",
                tickvals=stratagems_data["x"],
                ticktext=stratagems_data["x_labels"]
            ),
            paper_bgcolor=metadata.dict_of_colors["black"],
            plot_bgcolor=metadata.dict_of_colors["light-black"],
        )
    )
    fig.update_xaxes(
        ticks="outside", 
        linecolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["grey"]
    )
    fig.update_yaxes(
        ticks="outside", 
        gridcolor=metadata.dict_of_colors["grey"],
        linecolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["grey"]
    )
    fig.update_traces(width=0.5)
    return fig
    return fig

    