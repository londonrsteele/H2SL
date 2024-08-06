import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFormLayout, QPushButton, QWidget,
                                QGroupBox, QDateEdit, QTimeEdit,
                                QGridLayout, QSpinBox, QMessageBox)

################################################################
# 
# CAR_Input_Widget class
#
################################################################
class CAR_Input_Widget(QWidget):
    ################################################################
    # CAR_Input_Widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0
        
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.create_CAR_data_entry_groupbox(), 0, 0, 6, 1)
        self.CAR_button = QPushButton("Save Career Data", self)
        self.grid_layout.addWidget(self.CAR_button, 6, 0, 1, 1, Qt.AlignCenter)
        self.view_button = QPushButton("View Data Dashboard", self)
        self.grid_layout.addWidget(self.view_button, 7, 0, 1, 2)
        self.setLayout(self.grid_layout)

        # Add functionality to "Save Career Data" button
        self.CAR_button.clicked.connect(self.CAR_form_save)

        # QMessageBoxes for Popup windows to confirm saving
        self.CAR_popup = QMessageBox()
        self.CAR_popup.setWindowTitle("Caereer Form")
        self.CAR_popup.setText("Career data saved successfully!")
        self.error_popup = QMessageBox()
        self.error_popup.setWindowTitle("Save Error")
        self.error_popup.setText("Error saving data: File Already Exists!")
        # TODO: add functionality "do you want to overwrite?" etc.

    ################################################################
    # CAR_Input_Widget member function: create_CAR_data_entry_groupbox
    ################################################################
    def create_CAR_data_entry_groupbox(self):
        self.CAR_groupbox = QGroupBox("Career Stats Entry")
        self.form_layout = QFormLayout()

        # Create Entry Boxes
        self.CAR_enemy_kills = QSpinBox(minimum=0, maximum=1000000000)

        # Add Entry Boxes to layout
        self.form_layout.addRow(("Enemy Kills: "), self.CAR_enemy_kills)

        # Return groupbox to grid layout
        self.CAR_groupbox.setLayout(self.form_layout)
        return self.CAR_groupbox

    ################################################################
    # CAR_Input_Widget member function: CAR_form_save
    ################################################################
    def CAR_form_save(self):
        # Put data from form into Pandas DataFrame
        CAR_data = {"CAR_enemy_kills":self.CAR_enemy_kills.text()
                    }
        CAR_df = pd.DataFrame(data=CAR_data, index=[0])

        # Create csv file
        file_path = "./save_files/career_savefile.csv"
        try:
            with open(file_path, "x") as file:
                file.close()

            # Write DataFrame to file
            CAR_df.to_csv(file_path, index=False)

            # Display popup confirming data saved
            self.CAR_popup.exec_()
        except FileExistsError:
            print("File already exists.")
            self.error_popup.exec_()




################################################################
# 
# EOM_Input_Widget class
#
################################################################
class EOM_Input_Widget(QWidget):
    ################################################################
    # EOM_Input_Widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.create_EOM_data_entry_groupbox(), 0, 0, 6, 1)
        self.grid_layout.addWidget(self.create_EOM_loadout_entry_groupbox(), 0, 1, 6, 1)
        self.EOM_button = QPushButton("Save Mission Data", self)
        self.loadout_button = QPushButton("Save Loadout Data", self)
        self.grid_layout.addWidget(self.EOM_button, 6, 0, 1, 1, Qt.AlignCenter)
        self.grid_layout.addWidget(self.loadout_button, 6, 1, 1, 1, Qt.AlignCenter)
        self.view_button = QPushButton("View Data Dashboard", self)
        self.grid_layout.addWidget(self.view_button, 7, 0, 1, 2)
        self.setLayout(self.grid_layout)

        # Add functionality to "Save Mission Data" button
        self.EOM_button.clicked.connect(self.EOM_form_save)

        # Add functionality to "Save Loadout Data" button
        self.loadout_button.clicked.connect(self.loadout_form_save)

        # QMessageBoxes for Popup windows to confirm saving
        self.EOM_popup = QMessageBox()
        self.EOM_popup.setWindowTitle("EOM Form")
        self.EOM_popup.setText("End of Mission data saved successfully!")
        self.loadout_popup = QMessageBox()
        self.loadout_popup.setWindowTitle("Loadout Form")
        self.loadout_popup.setText("Loadout data save successfully!")
        self.error_popup = QMessageBox()
        self.error_popup.setWindowTitle("Save Error")
        self.error_popup.setText("Error saving data: File Already Exists!\n"
                                 + "Please ensure date and time are unique.")

    ################################################################
    # EOM_Input_Widget member function: create_EOM_data_entry_groupbox
    ################################################################
    def create_EOM_data_entry_groupbox(self):
        self.EOM_groupbox = QGroupBox(("End of Mission Stats Entry"))
        self.form_layout = QFormLayout()

        # Create Entry Boxes
        self.EOM_date = QDateEdit()
        self.EOM_endtime = QTimeEdit()
        # TODO: make above update automatically
        self.EOM_accuracy = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_shots_fired = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_shots_hit = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_deaths = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_stims_used = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_accidentals = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_samples_extracted = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_stratagems_used = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_melee_kills = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_times_reinforcing = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_friendly_fire_dmg = QSpinBox(minimum=0, maximum=1000000000)
        self.EOM_distance_traveled = QSpinBox(minimum=0, maximum=1000000000)

        # Add Entry Boxes to layout
        self.form_layout.addRow(("Date: "), self.EOM_date)
        self.form_layout.addRow(("End Time: "), self.EOM_endtime)
        self.form_layout.addRow(("Accuracy: "), self.EOM_accuracy)
        self.form_layout.addRow(("Shots Fired: "), self.EOM_shots_fired)
        self.form_layout.addRow(("Shots Hit: "), self.EOM_shots_hit)
        self.form_layout.addRow(("Deaths: "), self.EOM_deaths)
        self.form_layout.addRow(("Stims Used: "), self.EOM_stims_used)
        self.form_layout.addRow(("Accidentals: "), self.EOM_accidentals)
        self.form_layout.addRow(("Samples Extracted: "), self.EOM_samples_extracted)
        self.form_layout.addRow(("Stratagems Used: "), self.EOM_stratagems_used)
        self.form_layout.addRow(("Melee Kills: "), self.EOM_melee_kills)
        self.form_layout.addRow(("Times Reinforcing: "), self.EOM_times_reinforcing)
        self.form_layout.addRow(("Friendly Fire Damage: "), self.EOM_friendly_fire_dmg)
        self.form_layout.addRow(("Distance Traveled: "), self.EOM_distance_traveled)

        # Return groupbox to grid layout
        self.EOM_groupbox.setLayout(self.form_layout)
        return self.EOM_groupbox
    
    ################################################################
    # EOM_Input_Widget member function: create_EOM_loadout_entry_groupbox
    ################################################################
    def create_EOM_loadout_entry_groupbox(self):
        self.EOM_groupbox = QGroupBox("Mission Loadout Entry")
        self.form_layout = QFormLayout()

        # Create Entry Boxes
        self.loadout_date = QDateEdit()
        self.loadout_endtime = QTimeEdit()
        
        # Add Entry Boxes to layout
        self.form_layout.addRow(("Date: "), self.loadout_date)
        self.form_layout.addRow(("End Time: "), self.loadout_endtime)
        
        # Return groupbox to grid layout
        self.EOM_groupbox.setLayout(self.form_layout)
        return self.EOM_groupbox
    
    ################################################################
    # EOM_Input_Widget member function: EOM_form_save
    ################################################################
    def EOM_form_save(self):
        # Convert DateTimes to filename-friendly formats
        eom_day_formatted = self.EOM_date.date().toString("MMMM_d_yyyy")
        eom_time_formatted = self.EOM_endtime.time().toString("H_m")

        # Put data from form into Pandas DataFrame
        EOM_data = {"eom_day":self.EOM_date.text(),
                    "eom_time":self.EOM_endtime.text(),
                    "eom_accuracy":self.EOM_accuracy.text(),
                    "eom_shots_fired":self.EOM_shots_fired.text(),
                    "eom_shots_hit":self.EOM_shots_hit.text(),
                    "eom_deaths":self.EOM_deaths.text(),
                    "eom_stims_used":self.EOM_stims_used.text(),
                    "eom_accidentals":self.EOM_accidentals.text(),
                    "eom_samples_extracted":self.EOM_samples_extracted.text(),
                    "eom_stratagems_used":self.EOM_stratagems_used.text(),
                    "eom_melee_kills":self.EOM_melee_kills.text(),
                    "eom_times_reinforcing":self.EOM_times_reinforcing.text(),
                    "eom_friendly_fire_dmg":self.EOM_friendly_fire_dmg.text(),
                    "eom_distance_traveled":self.EOM_distance_traveled.text()
                    }
        EOM_df = pd.DataFrame(data=EOM_data, index=[0])

        # Create csv file
        file_path = "./save_files/EOM_savefile_" + eom_day_formatted + "_" + eom_time_formatted + ".csv"
        try:
            with open(file_path, "x") as file:
                file.close()
            # Write DataFrame to file
            EOM_df.to_csv(file_path, index=False)

            # Display popup confirming data saved
            self.EOM_popup.exec_()
        except FileExistsError:
            print("File already exists.")
            self.error_popup.exec_()

    ################################################################
    # EOM_Input_Widget member function: loadout_form_save
    ################################################################
    def loadout_form_save(self):
        # Convert DateTimes to filename-friendly formats
        loadout_day_formatted = self.loadout_date.date().toString("MMMM_d_yyyy")
        loadout_time_formatted = self.loadout_endtime.time().toString("H_m")

        # Put data from form into Pandas DataFrame
        loadout_data = {"loadout_day":self.loadout_date.text(),
                    "loadout_time":self.loadout_endtime.text()
                    }
        loadout_df = pd.DataFrame(data=loadout_data, index=[0])

        # Create csv file
        file_path = "./save_files/loadout_savefile_" + loadout_day_formatted + "_" + loadout_time_formatted + ".csv"
        try:
            with open(file_path, "x") as file:
                file.close()

            # Write DataFrame to file
            loadout_df.to_csv(file_path, index=False)

            # Display popup confirming data saved
            self.loadout_popup.exec_()
        except FileExistsError:
            print("File already exists.")
            self.error_popup.exec_()