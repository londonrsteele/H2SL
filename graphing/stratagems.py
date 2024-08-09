import plotly.express as pltxp

def Create_Stratagem_Graph(CAR_df):
    # CAR total stratagems used
    # CAR defensive stratagems used
    # CAR eagle stratagems used
    # CAR supply stratagems used
    # CAR reinforce stratagems used
    stratagems_data = {
        "x_labels" : ["Total", "Defensive", "Eagle", "Supply", "Reinforce"],
        "stats" : [ CAR_df["CAR_total_strats_used"][0], CAR_df["CAR_def_strats_used"][0], 
                   CAR_df["CAR_eagle_strats_used"][0], CAR_df["CAR_supply_strats_used"][0],
                   CAR_df["CAR_reinforce_strats_used"][0]
                ]
    }

    fig = pltxp.bar(stratagems_data, x="x_labels", y="stats",
                    labels={"x_labels":"Stratagems Used", "stats":"Count"},
                    text_auto=True)

    return fig

    