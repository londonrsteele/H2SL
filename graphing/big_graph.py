import os
from pathlib import Path
import pandas as pd
import plotly.express as pltxp

################################################################
# 
# Create_big_graph()
#
################################################################
def Create_big_graph(stat):
    match stat:
        case "Total Kills":
            return create_Total_Kills_graph()
        case "Enemy Kills":
            return create_Enemy_Kills_graph()
        case "Terminid Kills":
            return create_Terminid_Kills_graph()
        case "Automaton Kills":
            return create_Automaton_Kills_graph()
        case "Grenade Kills":
            return create_Grenade_Kills_graph()
        case "Melee Kills",:
            return create_Melee_Kills_graph()
        case "Eagle Kills":
            return create_Eagle_Kills_graph()
        case "Team Kills":
            return create_Team_Kills_graph()
        case "Shot Kills":
            return create_Shot_Kills_graph()
        case "Accuracy":
            return create_Accuracy_graph()
        case "Shots Fired":
            return create_Shots_Fired_graph()
        case "Shots Hit":
            return create_Shots_Hit_graph()
        case "Deaths":
            return create_Deaths_graph()
        case "Stims Used":
            return create_Stims_Used_graph()
        case "Total Stratagems Used":
            return create_Total_Stratagems_graph()
        case "Defensive Stratagems Used":
            return create_Defensive_Stratagems_graph()
        case "Eagle Stratagems Used":
            return create_Eagle_Stratagems_graph()
        case "Supply Stratagems Used":
            return create_Supply_Stratagems_graph()
        case "Reinforce Stratagems Used":
            return create_Reinforce_Stratagems_graph()
        case "Orbitals Used":
            return create_Orbitals_Used_graph()
        case "Times Reinforcing":
            return create_Times_Reinforcing_graph()
        case "Successful Extractions":
            return create_Successful_Extractions_graph()
        case "Samples Collected":
            return create_Samples_Collected_graph()
        case "Objectives Completed":
            return create_Objectives_Completed_graph()
        case "Missions Played":
            return create_Missions_Played_graph()
        case "Missions Won":
            return create_Missions_Won_graph()
        case "In-Misison Time":
            return create_In_Mission_Time_graph()
        case "Distance Traveled":
            return create_Distance_Traveled_graph()
        case "Total XP Earned":
            return create_Total_XP_Earned_graph()


################################################################
# 
# get last 10 dataframes (career or EOM)
#
################################################################
def get_last10_df(arg1):
    # arg1 is either "career" for CAR, or "EOM" for EOM files
    # sort files in directory by modified time
    filepaths = sorted(Path("./save_files/").iterdir(), key=os.path.getmtime)
    
    # get top 10 data_class files and load into dataframes
    dict_of_dfs = {}
    df_count = 0
    for filepath in filepaths:
        if filepath.name.startswith(arg1):
            dict_of_dfs[df_count] = pd.read_csv("./save_files/"+filepath.name)
            df_count +=1
            if df_count == 10:
                break
    
    # return dictionary of dataframes
    return dict_of_dfs

################################################################
# 
# Create (strat) graph
#
################################################################
################################################################
# create_Total_Kills_graph()
################################################################
def create_Total_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    TKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        TKs_df[i] = dict_of_dfs[i]["CAR_enemy_kills"][0] + dict_of_dfs[i]["CAR_friendly_kills"][0]
    
    fig = pltxp.line(
        x=TKs_df.keys(),
        y=TKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Total Kills"}
    )
    return fig

################################################################
# create_Enemey_Kills_graph()
################################################################
def create_Enemy_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    EKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        EKs_df[i] = dict_of_dfs[i]["CAR_enemy_kills"][0]
    
    fig = pltxp.line(
        x=EKs_df.keys(),
        y=EKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Enemy Kills"}
    )
    return fig

################################################################
# create_Terminid_Kills_graph()
################################################################
def create_Terminid_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    TrKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        TrKs_df[i] = dict_of_dfs[i]["CAR_terminid_kills"][0]
    
    fig = pltxp.line(
        x=TrKs_df.keys(),
        y=TrKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Terminid Kills"}
    )
    return fig

################################################################
# create_Automaton_Kills_graph()
################################################################
def create_Automaton_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    AKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        AKs_df[i] = dict_of_dfs[i]["CAR_automaton_kills"][0]
    
    fig = pltxp.line(
        x=AKs_df.keys(),
        y=AKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Automaton Kills"}
    )
    return fig

################################################################
# create_Grenade_Kills_graph()
################################################################
def create_Grenade_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    GKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        GKs_df[i] = dict_of_dfs[i]["CAR_grenade_kills"][0]
    
    fig = pltxp.line(
        x=GKs_df.keys(),
        y=GKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Grenade Kills"}
    )
    return fig

################################################################
# create_Melee_Kills_graph()
################################################################
def create_Melee_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    MKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        MKs_df[i] = dict_of_dfs[i]["CAR_melee_kills"][0]
    
    fig = pltxp.line(
        x=MKs_df.keys(),
        y=MKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Melee Kills"}
    )
    return fig

################################################################
# create_Eagle_Kills_graph()
################################################################
def create_Eagle_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    EKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        EKs_df[i] = dict_of_dfs[i]["CAR_eagle_kills"][0]
    
    fig = pltxp.line(
        x=EKs_df.keys(),
        y=EKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Eagle Kills"}
    )
    return fig

################################################################
# create_Team_Kills_graph()
################################################################
def create_Team_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    TeKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        TeKs_df[i] = dict_of_dfs[i]["CAR_team_kills"][0]
    
    fig = pltxp.line(
        x=TeKs_df.keys(),
        y=TeKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Team Kills"}
    )
    return fig

################################################################
# create_Shot_Kills_graph()
################################################################
def create_Shot_Kills_graph():
    dict_of_dfs = get_last10_df("career")
    SKs_df = {}
    for i in range(0, len(dict_of_dfs)):
        total_kills = dict_of_dfs[i]["CAR_enemy_kills"][0] + dict_of_dfs[i]["CAR_friendly_kills"][0]
        other_kills = dict_of_dfs[i]["CAR_grenade_kills"][0] + dict_of_dfs[i]["CAR_melee_kills"][0] + dict_of_dfs[i]["CAR_egale_kills"][0]
        SKs_df[i] = total_kills - other_kills
    
    fig = pltxp.line(
        x=SKs_df.keys(),
        y=SKs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Shot Kills"}
    )
    return fig

################################################################
# create_Accuracy_graph()
################################################################
def create_Accuracy_graph():
    dict_of_dfs = get_last10_df("EOM")
    Acc_df = {}
    for i in range(0, len(dict_of_dfs)):
        Acc_df[i] = dict_of_dfs[i]["EOM_accuracy"][0]

    fig = pltxp.line(
        x=Acc_df.keys(),
        y=Acc_df,
        template="simple_white",
        labels={"x":"Mission Save File", "y":"Accuracy"}
    )
    return fig

################################################################
# create_Shots_Fired_graph()
################################################################
def create_Shots_Fired_graph():
    dict_of_dfs = get_last10_df("EOM")
    SFs_df = {}
    for i in range(0, len(dict_of_dfs)):
        SFs_df[i] = dict_of_dfs[i]["EOM_shots_fired"][0]

    fig = pltxp.line(
        x=SFs_df.keys(),
        y=SFs_df,
        template="simple_white",
        labels={"x":"Mission Save File", "y":"Shots Fired"}
    )
    return fig

################################################################
# create_Shots_Hit_graph()
################################################################
def create_Shots_Hit_graph():
    dict_of_dfs = get_last10_df("EOM")
    SHs_df = {}
    for i in range(0, len(dict_of_dfs)):
        SHs_df[i] = dict_of_dfs[i]["EOM_shots_hit"][0]

    fig = pltxp.line(
        x=SHs_df.keys(),
        y=SHs_df,
        template="simple_white",
        labels={"x":"Mission Save File", "y":"Shots Hit"}
    )
    return fig

################################################################
# create_Accuracy_graph()
################################################################
def create_Accuracy_graph():
    dict_of_dfs = get_last10_df("EOM")
    Acc_df = {}
    for i in range(0, len(dict_of_dfs)):
        Acc_df[i] = dict_of_dfs[i]["EOM_accuracy"][0]

    fig = pltxp.line(
        x=Acc_df.keys(),
        y=Acc_df,
        template="simple_white",
        labels={"x":"Mission Save File", "y":"Accuracy"}
    )
    return fig

################################################################
# create_Deaths_graph()
################################################################
def create_Deaths_graph():
    dict_of_dfs = get_last10_df("career")
    Ds_df = {}
    for i in range(0, len(dict_of_dfs)):
        Ds_df[i] = dict_of_dfs[i]["CAR_deaths"][0]

    fig = pltxp.line(
        x=Ds_df.keys(),
        y=Ds_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Deaths"}
    )
    return fig

################################################################
# create_Stims_Used_graph()
################################################################
def create_Stims_Used_graph():
    dict_of_dfs = get_last10_df("EOM")
    SUs_df = {}
    for i in range(0, len(dict_of_dfs)):
        SUs_df[i] = dict_of_dfs[i]["EOM_stims_used"][0]

    fig = pltxp.line(
        x=SUs_df.keys(),
        y=SUs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Stims Used"}
    )
    return fig

################################################################
# create_Total_Stratagems_graph()
################################################################
def create_Total_Stratagems_graph():
    dict_of_dfs = get_last10_df("career")
    TSs_df = {}
    for i in range(0, len(dict_of_dfs)):
        TSs_df[i] = dict_of_dfs[i]["CAR_total_strats_used"][0]

    fig = pltxp.line(
        x=TSs_df.keys(),
        y=TSs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Total Stratagems Used"}
    )
    return fig

################################################################
# create_Defensive_Stratagems_graph()
################################################################
def create_Defensive_Stratagems_graph():
    dict_of_dfs = get_last10_df("career")
    DSs_df = {}
    for i in range(0, len(dict_of_dfs)):
        DSs_df[i] = dict_of_dfs[i]["CAR_def_strats_used"][0]

    fig = pltxp.line(
        x=DSs_df.keys(),
        y=DSs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Defensive Stratagems Used"}
    )
    return fig

################################################################
# create_Eagle_Stratagems_graph()
################################################################
def create_Eagle_Stratagems_graph():
    dict_of_dfs = get_last10_df("career")
    ESs_df = {}
    for i in range(0, len(dict_of_dfs)):
        ESs_df[i] = dict_of_dfs[i]["CAR_eagle_strats_used"][0]

    fig = pltxp.line(
        x=ESs_df.keys(),
        y=ESs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Eagle Stratagems Used"}
    )
    return fig

################################################################
# create_Supply_Stratagems_graph()
################################################################
def create_Supply_Stratagems_graph():
    dict_of_dfs = get_last10_df("career")
    SSs_df = {}
    for i in range(0, len(dict_of_dfs)):
        SSs_df[i] = dict_of_dfs[i]["CAR_supply_strats_used"][0]

    fig = pltxp.line(
        x=SSs_df.keys(),
        y=SSs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Supply Stratagems Used"}
    )
    return fig

################################################################
# create_Reinforce_Stratagems_graph()
################################################################
def create_Reinforce_Stratagems_graph():
    dict_of_dfs = get_last10_df("career")
    RSs_df = {}
    for i in range(0, len(dict_of_dfs)):
        RSs_df[i] = dict_of_dfs[i]["CAR_reinforce_strats_used"][0]

    fig = pltxp.line(
        x=RSs_df.keys(),
        y=RSs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Reinforce Stratagems Used"}
    )
    return fig

################################################################
# create_Orbitals_Used_graph()
################################################################
def create_Orbitals_Used_graph():
    dict_of_dfs = get_last10_df("career")
    OUs_df = {}
    for i in range(0, len(dict_of_dfs)):
        OUs_df[i] = dict_of_dfs[i]["CAR_orbitals_used"][0]

    fig = pltxp.line(
        x=OUs_df.keys(),
        y=OUs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Orbitals Used"}
    )
    return fig

################################################################
# create_Times_Reinforcing_graph()
################################################################
def create_Times_Reinforcing_graph():
    dict_of_dfs = get_last10_df("EOM")
    TRs_df = {}
    for i in range(0, len(dict_of_dfs)):
        TRs_df[i] = dict_of_dfs[i]["EOM_times_reinforcing"][0]

    fig = pltxp.line(
        x=TRs_df.keys(),
        y=TRs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Times Reinforcing"}
    )
    return fig

################################################################
# create_Successful_Extractions_graph()
################################################################
def create_Successful_Extractions_graph():
    dict_of_dfs = get_last10_df("career")
    SEs_df = {}
    for i in range(0, len(dict_of_dfs)):
        SEs_df[i] = dict_of_dfs[i]["CAR_successful_extractions"][0]

    fig = pltxp.line(
        x=SEs_df.keys(),
        y=SEs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Successful Extractions"}
    )
    return fig

################################################################
# create_Samples_Collected_graph()
################################################################
def create_Samples_Collected_graph():
    dict_of_dfs = get_last10_df("career")
    SCs_df = {}
    for i in range(0, len(dict_of_dfs)):
        SCs_df[i] = dict_of_dfs[i]["CAR_samples_collected"][0]

    fig = pltxp.line(
        x=SCs_df.keys(),
        y=SCs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Samples Collected"}
    )
    return fig

################################################################
# create_Objectives_Completed_graph()
################################################################
def create_Objectives_Completed_graph():
    dict_of_dfs = get_last10_df("career")
    OCs_df = {}
    for i in range(0, len(dict_of_dfs)):
        OCs_df[i] = dict_of_dfs[i]["CAR_objectives_completed"][0]

    fig = pltxp.line(
        x=OCs_df.keys(),
        y=OCs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Objectives Completed"}
    )
    return fig

################################################################
# create_Missions_Played_graph()
################################################################
def create_Missions_Played_graph():
    dict_of_dfs = get_last10_df("career")
    MPs_df = {}
    for i in range(0, len(dict_of_dfs)):
        MPs_df[i] = dict_of_dfs[i]["CAR_missions_played"][0]

    fig = pltxp.line(
        x=MPs_df.keys(),
        y=MPs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Missions Played"}
    )
    return fig

################################################################
# create_Missions_Won_graph()
################################################################
def create_Missions_Won_graph():
    dict_of_dfs = get_last10_df("career")
    MWs_df = {}
    for i in range(0, len(dict_of_dfs)):
        MWs_df[i] = dict_of_dfs[i]["CAR_missions_won"][0]

    fig = pltxp.line(
        x=MWs_df.keys(),
        y=MWs_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Missions Won"}
    )
    return fig

################################################################
# create_In_Mission_Time_graph()
################################################################
def create_In_Mission_Time_graph():
    dict_of_dfs = get_last10_df("career")
    IMT_df = {}
    for i in range(0, len(dict_of_dfs)):
        IMT_df[i] = dict_of_dfs[i]["CAR_inmission_time"][0]

    fig = pltxp.line(
        x=IMT_df.keys(),
        y=IMT_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"In-Mission Time"}
    )
    return fig

################################################################
# create_Distance_Traveled_graph()
################################################################
def create_Distance_Traveled_graph():
    dict_of_dfs = get_last10_df("EOM")
    DT_df = {}
    for i in range(0, len(dict_of_dfs)):
        DT_df[i] = dict_of_dfs[i]["EOM_distance_traveled"][0]

    fig = pltxp.line(
        x=DT_df.keys(),
        y=DT_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Distance Traveled"}
    )
    return fig

################################################################
# create_Total_XP_Earned_graph()
################################################################
def create_Total_XP_Earned_graph():
    dict_of_dfs = get_last10_df("career")
    TXP_df = {}
    for i in range(0, len(dict_of_dfs)):
        TXP_df[i] = dict_of_dfs[i]["CAR_total_xp_earned"][0]

    fig = pltxp.line(
        x=TXP_df.keys(),
        y=TXP_df,
        template="simple_white",
        labels={"x":"Career Save File", "y":"Total XP Earned"}
    )
    return fig