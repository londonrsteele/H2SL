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
        self.submit_button = QPushButton("Save Mission Data")
        
        ################################################################
        # 
        # Get connect functionality to work!!!
        #
        ################################################################
        self.submit_button.clicked.connect(self.change_view())

        self.grid_layout.addWidget(self.submit_button, 6, 0, 1, 2, Qt.AlignCenter)
        self.setLayout(self.grid_layout)

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
    
    @Slot()
    def change_view(self):
        print("Howdy!")