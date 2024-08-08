import pandas as pd
import plotly.express as pltxp

def Create_Survivor_Graph(EOM_df):
    survivor_data = {
        "x_labels" : ["Deaths", "Stims Used"],
        "stats" : [EOM_df["eom_deaths"][0], EOM_df["eom_stims_used"][0]],
    }
    
    fig = pltxp.bar(survivor_data, x="x_labels", y="stats",
                    labels={"x_labels":"Stat", "stats":"Count"},
                    text_auto=True)
    return fig