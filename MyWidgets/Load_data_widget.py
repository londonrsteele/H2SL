import pandas as pd
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import (QHBoxLayout, QPushButton, QWidget,
                                QGroupBox, QDateEdit, QTimeEdit,
                                QGridLayout, QSpinBox, QMessageBox,
                                QFrame)
from assets import stylesheets
################################################################
# 
# Load_data_widget class
#
################################################################
class Load_data_widget(QWidget):
    ################################################################
    # Load_data_widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0
        

        # Make Buttons
        self.setStyleSheet(stylesheets.Big_Buttons)
        self.Load_EOM_data = QPushButton("Mission")
        self.Load_CAR_data = QPushButton("Career")

        # Set up layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.Load_EOM_data)
        self.layout.addWidget(self.Load_CAR_data)
        self.setLayout(self.layout)