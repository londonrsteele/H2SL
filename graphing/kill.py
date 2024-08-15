import plotly.express as pltxp

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
        "x_labels" : ["Total Kills", "Enemy Kills", "Terminid Kills", 
                      "Automaton Kills", "Team Kills", "Grenade Kills", 
                      "Melee Kills", "Eagle Kills", "Shot Kills"
                    ],
        "stats" : [ CAR_df["CAR_total_kills"][0], CAR_df["CAR_enemy_kills"][0], CAR_df["CAR_terminid_kills"][0],
                   CAR_df["CAR_automaton_kills"][0], CAR_df["CAR_team_kills"][0], CAR_df["CAR_grenade_kills"][0],
                   CAR_df["CAR_melee_kills"][0], CAR_df["CAR_eagle_kills"][0], CAR_df["CAR_shot_kills"][0]
                ]
    }

    fig = pltxp.bar(kills_data, x="x_labels", y="stats",
                    labels={"x_labels":"Stat", "stats":"Count"},
                    text_auto=True)

    return fig
