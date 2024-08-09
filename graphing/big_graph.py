import os
from pathlib import Path
import pandas as pd
import plotly.express as pltxp
import graphing.metadata as metadata
def Create_big_graph(stat):
    match stat:
        case "Total Kills":
            return create_Total_Kills_graph()
        case "Enemy Kills":
            return
        case "Terminid Kills":
            return
        case "Automaton Kills":
            return
        case "Grenade Kills":
            return
        case "Melee Kills",:
            return
        case "Eagle Kills":
            return
        case "Team Kills":
            return
        case "Shot Kills":
            return
        case "Accuracy":
            return
        case "Shots Fired":
            return
        case "Shots Hit":
            return
        case "Deaths":
            return
        case "Stims Used":
            return
        case "Total Stratagems Used":
            return
        case "Defensive Stratagems Used":
            return
        case "Eagle Stratagems Used":
            return
        case "Supply Stratagems Used":
            return
        case "Reinforce Stratagems Used":
            return
        case "Orbitals Used":
            return
        case "Times Reinforcing":
            return
        case "Successful Extractions":
            return
        case "Samples Collected":
            return
        case "Objectives Completed":
            return
        case "Missions Played":
            return
        case "Missions Won":
            return
        case "In-Misison Time":
            return
        case "Distance Traveled":
            return
        case "Total XP Earned":
            return


def get_last10_EOM_df():
    # sort files in directory by modified time
        filepaths = sorted(Path("./save_files/").iterdir(), key=os.path.getmtime)
        
        # get top 10 data_class files and load into dataframes
        dict_of_dfs = {}
        df_count = 0
        for filepath in filepaths:
            if filepath.name.startswith("career"):
                dict_of_dfs[df_count] = pd.read_csv("./save_files/"+filepath.name)
                df_count +=1
                if df_count == 10:
                    break
        
        # return dictionary of dataframes
        return dict_of_dfs


def create_Total_Kills_graph():
    dict_of_dfs = get_last10_EOM_df()
    TKs_df = pd.DataFrame()
    dfs_count = 0
    for i in range(0, len(dict_of_dfs)):
        dfs_count +=1

    print(TKs_df)
    fig = pltxp.line(
        x=TKs_df.keys(),
        y=TKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Total Kills"}
    )
    return fig