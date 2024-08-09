from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QWidget,
                                QLabel, QGroupBox)
from assets import stylesheets
################################################################
# 
# Log_data_widget class
#
################################################################
class Log_data_widget(QWidget):
    ################################################################
    # Log_data_widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0
        
        # Make Title
        self.Title = QLabel()
        self.Title.setStyleSheet(stylesheets.Title)
        self.Title.setText("Log Data")
        self.Title.setAlignment(Qt.AlignCenter)
        
        # Make Buttons
        self.setStyleSheet(stylesheets.Big_Buttons)
        self.Log_EOM_data = QPushButton("Mission")
        self.Log_CAR_data = QPushButton("Career")

        # Set up layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.Title)
        self.buttons_box = QGroupBox()
        self.layout.addWidget(self.buttons_box)

        # Arrange buttons
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.Log_EOM_data)
        self.buttons_layout.addWidget(self.Log_CAR_data)
        self.buttons_box.setLayout(self.buttons_layout)
        self.buttons_box.setStyleSheet(stylesheets.Big_Buttons_Box)
        self.setLayout(self.layout)