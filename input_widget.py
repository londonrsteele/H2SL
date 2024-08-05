import pandas as pd
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QGroupBox, QDateEdit, QTimeEdit,
                               QGridLayout, QSpinBox, QButtonGroup, QStackedWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart
from main_window import MainWindow

class Input_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.create_EOM_data_entry_groupbox(), 0, 0, 6, 1)
        self.grid_layout.addWidget(self.create_EOM_loadout_entry_groupbox(), 0, 1, 6, 1)
        self.submit_button = QPushButton("Save Mission Data", self)
        self.view_button = QPushButton("View Mission Data", self)
        self.grid_layout.addWidget(self.submit_button, 6, 0, 1, 1, Qt.AlignCenter)
        self.grid_layout.addWidget(self.view_button, 6, 1, 1, 1, Qt.AlignCenter)
        self.setLayout(self.grid_layout)

        # Add functionality to "Save Mission Data" button
        self.submit_button.clicked.connect(self.EOM_form_save)


    def create_EOM_data_entry_groupbox(self):
        self.EOM_groupbox = QGroupBox(("End of Mission Stats Entry"))
        self.form_layout = QFormLayout()

        # Create Entry Boxes
        self.EOM_date = QDateEdit()
        self.EOM_endtime = QTimeEdit()
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
    
    def create_EOM_loadout_entry_groupbox(self):
        self.EOM_groupbox = QGroupBox("Mission Loadout Entry")
        self.form_layout = QFormLayout()

        ################################################################
        # 
        # Add functionality here: loadout entry boxes
        #
        ################################################################


        # Return groupbox to grid layout
        self.EOM_groupbox.setLayout(self.form_layout)
        return self.EOM_groupbox
    
    
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
        file_path = "./" + eom_day_formatted + "_" + eom_time_formatted + "_EOM_savefile.csv"
        try:
            with open(file_path, "x") as file:
                file.close()
        except FileExistsError:
            print("File already exists.")

        # Write DataFrame to file
        EOM_df.to_csv(file_path, index=False)

        ################################################################
        # 
        # Add functionality here: send "Data saved" to status bar, popup!
        #
        ################################################################
