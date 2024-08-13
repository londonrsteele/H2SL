import pandas as pd
from PySide6.QtWidgets import (QGridLayout, QPushButton, QWidget, QLabel)
from graphing import stat_scraper
################################################################
# 
# Mission_Tab class
#
################################################################
class Mission_Tab(QWidget):
    ################################################################
    # Mission_Tab initialization
    ################################################################
    def __init__(self, parent: QWidget, datafile):
        super().__init__(parent)
        # set up layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Add View Dashboard Button
        self.view_dashboard_button = QPushButton("View Mission Dashboard")

        # validate datafile
        if (datafile == "") | (datafile == "Error: No File Loaded"):
            # Create warning label
            Warning_Label = QLabel("Warning: No Misison file loaded")
            self.layout.addWidget(Warning_Label)
            print("Warning: No Mission file loaded")
            
            # If no datafile loaded, make "View Dashboard" button disabled
            self.view_dashboard_button.setDisabled(True)

        else:
            # If datafile loaded, make "View Dashboard" button disabled
            self.view_dashboard_button.setEnabled(True)
            
            # use Stat_Scraper to load data
            scraper = stat_scraper.Stat_Scraper()
            self.data = scraper.load_file(datafile)

            # Create data labels
            Accuracy = QLabel("Accuracy: " + str(self.data["eom_accuracy"][0]) + "%")
            Shots_Fired = QLabel("Shots Fired: " + str(self.data["eom_shots_fired"][0]))
            Shots_Hit = QLabel("Shots Hit: " + str(self.data["eom_shots_hit"][0]))
            Deaths = QLabel("Deaths: " + str(self.data["eom_deaths"][0]))
            Stims_Used = QLabel("Stims Used: " + str(self.data["eom_stims_used"][0]))
            Samples_Extracted = QLabel("Samples Extracted: " + str(self.data["eom_samples_extracted"][0]))
            Stratagems_Used = QLabel("Stratagems Used: " + str(self.data["eom_stratagems_used"][0]))
            Melee_Kills = QLabel("Melee Kills: " + str(self.data["eom_melee_kills"][0]))
            Times_Reinforcing = QLabel("Times Reinforcing: " + str(self.data["eom_times_reinforcing"][0]))
            Accidentals = QLabel("Accidentals: " + str(self.data["eom_team_kills"][0]))
            Friendly_Fire_Dmg = QLabel("Friendly Fire Damage: " + str(self.data["eom_friendly_fire_dmg"][0]))
            Distance_Traveled = QLabel("Distance Traveled: " + str(self.data["eom_distance_traveled"][0]))

            # Add data labels
            self.layout.addWidget(Accuracy, 0, 0, 1, 1)
            self.layout.addWidget(Shots_Fired, 1, 0, 1, 1)
            self.layout.addWidget(Shots_Hit, 2, 0, 1, 1)
            self.layout.addWidget(Deaths, 3, 0, 1, 1)
            self.layout.addWidget(Stims_Used, 4, 0, 1, 1)
            self.layout.addWidget(Samples_Extracted, 5, 0, 1, 1)
            self.layout.addWidget(Stratagems_Used, 0, 1, 1, 1)
            self.layout.addWidget(Melee_Kills, 1, 1, 1, 1)
            self.layout.addWidget(Times_Reinforcing, 2, 1, 1, 1)
            self.layout.addWidget(Accidentals, 3, 1, 1, 1)
            self.layout.addWidget(Friendly_Fire_Dmg, 4, 1, 1, 1)
            self.layout.addWidget(Distance_Traveled, 5, 1, 1, 1)

        # Add view dashboard button to layout last
        self.layout.addWidget(self.view_dashboard_button, 6, 0, 1, 2)

################################################################
# 
# Career_Tab class
#
################################################################
class Career_Tab(QWidget):
    ################################################################
    # Career_Tab initialization
    ################################################################
    def __init__(self, parent: QWidget, datafile):
        super().__init__(parent)
        # set up layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Add View Dashboard Button
        self.view_dashboard_button = QPushButton("View Career Dashboard")
        
        # validate datafile
        if (datafile == "") | (datafile == "Error: No File Loaded"):
            # Create warning label
            Warning_Label = QLabel("Warning: No Career file loaded")
            self.layout.addWidget(Warning_Label)
            print("Warning: No Career file loaded")

            # If no datafile loaded, make "View Dashboard" button disabled
            self.view_dashboard_button.setDisabled(True)

        else:
            # If datafile loaded, make "View Dashboard" button disabled
            self.view_dashboard_button.setEnabled(True)
            
            # use Stat_Scraper to load data
            scraper = stat_scraper.Stat_Scraper()
            self.data = scraper.load_file(datafile)

            # Create data labels
            Accuracy = QLabel("Enemy kills")

            # Add data labels
            self.layout.addWidget(Accuracy)
        
        # Add view dashboard button to layout last
        self.layout.addWidget(self.view_dashboard_button, 6, 0, 1, 2)

        