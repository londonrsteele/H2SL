from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QGroupBox, QDateEdit, QTimeEdit,
                               QGridLayout, QSpinBox)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

class Input_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0
        
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.create_EOM_data_entry_groupbox(), 0, 0)
        self.grid_layout.addWidget(self.create_EOM_loadout_entry_groupbox(), 0, 1)
        self.setLayout(self.grid_layout)

    def create_EOM_data_entry_groupbox(self):
        self.EOM_groupbox = QGroupBox(("End of Mission Stats Entry"))
        self.form_layout = QFormLayout()

        # Create Entry Boxes
        self.EOM_date = QDateEdit()
        self.EOM_endtime = QTimeEdit()
        self.EOM_accuracy = QSpinBox(maximum=1000000000)
        self.EOM_shots_fired = QSpinBox(maximum=1000000000)
        self.EOM_shots_hit = QSpinBox(maximum=1000000000)
        self.EOM_deaths = QSpinBox(maximum=1000000000)
        self.EOM_stims_used = QSpinBox(maximum=1000000000)
        self.EOM_accidentals = QSpinBox(maximum=1000000000)
        self.EOM_samples_extracted = QSpinBox(maximum=1000000000)
        self.EOM_stratagems_used = QSpinBox(maximum=1000000000)
        self.EOM_melee_kills = QSpinBox(maximum=1000000000)
        self.EOM_times_reinforcing = QSpinBox(maximum=1000000000)
        self.EOM_friendly_fire_dmg = QSpinBox(maximum=1000000000)
        self.EOM_distance_traveled = QSpinBox(maximum=1000000000)

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

        # Return groupbox to grid layout
        self.EOM_groupbox.setLayout(self.form_layout)
        return self.EOM_groupbox