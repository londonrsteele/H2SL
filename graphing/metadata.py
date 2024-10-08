import matplotlib.colors as mplcolors

list_of_ALL_strats = [
    # Kills
    "Total Kills", # curated
    "Enemy Kills",
    "Terminid Kills",
    "Automaton Kills",
    "Grenade Kills",
    "Melee Kills", 
    "Eagle Kills",
    "Team Kills", 
    "Shot Kills", # curated
    # Accuracy
    "Accuracy",
    "Shots Fired",
    "Shots Hit",
    # Survivor
    "Deaths",
    "Stims Used",
    # Stratagems
    "Total Stratagems Used",
    "Defensive Stratagems Used",
    "Eagle Stratagems Used",
    "Supply Stratagems Used",
    "Reinforce Stratagems Used",
    # Other
    "Orbitals Used",
    "Times Reinforcing",
    "Friendly Fire Damage",
    # Game
    "Successful Extractions",
    "Samples Collected",
    "Objectives Completed",
    "Missions Played",
    "Missions Won",
    "In-Misison Time",
    "Distance Traveled",
    "Total XP Earned"
]

list_of_CAR_strats = [
    # Kills
    "Total Kills", # curated
    "Enemy Kills",
    "Terminid Kills",
    "Automaton Kills",
    "Grenade Kills",
    "Melee Kills", 
    "Eagle Kills",
    "Team Kills", 
    "Shot Kills", # curated
    # Accuracy
    "Shots Fired",
    "Shots Hit",
    # Survivor
    "Deaths",
    # Stratagems
    "Total Stratagems Used",
    "Defensive Stratagems Used",
    "Eagle Stratagems Used",
    "Supply Stratagems Used",
    "Reinforce Stratagems Used",
    # Other
    "Orbitals Used",
    # Game
    "Successful Extractions",
    "Samples Collected",
    "Objectives Completed",
    "Missions Played",
    "Missions Won",
    "In-Misison Time",
    "Distance Traveled",
    "Total XP Earned"
]

list_of_EOM_strats = [
    # Kills
    "Kills",
    "Team Kills",
    "Melee Kills",
    # Accuracy
    "Accuracy",
    "Shots Fired",
    "Shots Hit",
    # Survivor
    "Deaths",
    "Stims Used",
    #Stratagems
    "Stratagems Used",
    # Other
    "Times Reinforcing",
    "Friendly Fire Damage",
    # Game
    "Samples Extracted",
    "Distance Traveled"
]

list_of_missions = [
    # General
    "Terminate Illegal Broadcast",
    "Pump Fuel to ICBM",
    "Upload Escape Pod Data",
    "Conduct Geological Survey",
    "Launch ICBM",
    "Retrieve Valuable Data",
    "Emergency Evacuation",
    # Terminid
    "Spread Democracy",
    "Eliminate Brood Commanders",
    "Purge Hatcheries",
    "Activate E-710 Pumps",
    "Blitz: Search and Destroy (Terminid)",
    "Eliminate Chargers",
    "Eradicate Terminid Swarm",
    "Eliminate Bile Titans",
    "Enable E-710 Extraction",
    # Automaton
    "Eliminate Devastators",
    "Sabotage Supply Bases",
    "Destroy Transmission Network",
    "Eradicate Automaton Forces",
    "Blitz: Search and Destroy (Automaton)",
    "Sabotage Air Base", 
    "Eliminate Automation Factory Strider",
    "Destroy Command Bunkers"
]

dict_of_colors = {
    "black" : "#070707",
    "light-black" : "#373836",
    "grey"  : "#64615F",
    "white" : "#F0EFEA",
    "dark-yellow": "#685E1F",
    "yellow" : "#FFE80A",
    "dark-blue": "#082844",
    "light-blue": "#1EC6D8",
    "dark-red": "#72000d",
    "red": "#930012"
}

def convert_to_rgb(color):
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    return "rgb("+str(r)+","+str(g)+","+str(b)+")"

color_scale = [
    [0.0, convert_to_rgb(dict_of_colors["black"])], 
    [0.25, convert_to_rgb(dict_of_colors["red"])],
    [0.50, convert_to_rgb(dict_of_colors["yellow"])],
    [0.75, convert_to_rgb(dict_of_colors["light-blue"])],
    [1.0, convert_to_rgb(dict_of_colors["white"])] 
]