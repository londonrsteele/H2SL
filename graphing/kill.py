import plotly.graph_objects as pltgo
from graphing import metadata

def Create_Kill_Graph(CAR_df):
    # CAR total kills = CAR enemy kills + CAR friendly kills
    # CAR enemy kills
    # CAR terminid kills 
    # CAR automaton kills
    # CAR friendly kills
    # CAR grenade kills
    # CAR melee kills
    # CAR eagle kills
    # CAR shot kills = CAR total kills - CAR grenade kills - CAR melee kills - CAR eagle kills
    kills_data = {
        "x_labels" : ["Total Kills", "Team Kills", "Enemy Kills", 
                      "Terminid Kills", "Automaton Kills", "Melee Kills",  
                      "Grenade Kills", "Eagle Kills", "Shot Kills"
                    ],
        "x" : [0,1,2,3,4,5,6,7,8],
        "stats" : [ CAR_df["CAR_total_kills"][0], CAR_df["CAR_team_kills"][0], CAR_df["CAR_enemy_kills"][0], 
                   CAR_df["CAR_terminid_kills"][0], CAR_df["CAR_automaton_kills"][0], CAR_df["CAR_melee_kills"][0],
                   CAR_df["CAR_grenade_kills"][0], CAR_df["CAR_eagle_kills"][0], CAR_df["CAR_shot_kills"][0]
                ],
        "colors": metadata.dict_of_colors["red"]
    }

    # fig = pltxp.bar(kills_data, x="x_labels", y="stats",
    #                 labels={"x_labels":"Stat", "stats":"Count"},
    #                 text_auto=True)

    # return fig

    fig = pltgo.Figure(
        data=[
            pltgo.Bar(
                name="Kills",
                x=kills_data["x"],
                y=kills_data["stats"],
                marker_color=kills_data["colors"],
                customdata=kills_data["x_labels"],
                hovertemplate="%{customdata}: %{y}<extra></extra>"
            )
        ],
        layout=pltgo.Layout(
            title="<b>Kills</b>",
            title_x = 0.5,
            xaxis_title = "<b>Kill Type<br></b>",
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
                tickvals=kills_data["x"],
                ticktext=kills_data["x_labels"]
            ),
            paper_bgcolor=metadata.dict_of_colors["black"],
            plot_bgcolor=metadata.dict_of_colors["light-black"],
        )
    )
    fig.update_xaxes(
        ticks="outside", 
        linecolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["light-black"]
    )
    fig.update_yaxes(
        ticks="outside", 
        gridcolor=metadata.dict_of_colors["grey"],
        linecolor=metadata.dict_of_colors["grey"],
        zerolinecolor=metadata.dict_of_colors["grey"]
    )
    fig.update_traces(width=0.5)
    return fig