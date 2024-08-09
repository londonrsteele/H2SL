from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QWidget,
                                QLabel, QGroupBox)
from assets import stylesheets
################################################################
# 
# Welcome_widget class
#
################################################################
class Welcome_widget(QWidget):
    ################################################################
    # Welcome_widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0

        # Make Title
        self.Title = QLabel()
        self.Title.setStyleSheet(stylesheets.Title)
        self.Title.setText("Welcome!")
        self.Title.setAlignment(Qt.AlignCenter)
        
        # Make Buttons
        self.setStyleSheet(stylesheets.Big_Buttons)
        self.Log_data_button = QPushButton("Log Data")
        self.View_data_button = QPushButton("View Data")

        # Set up layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.Title)
        self.buttons_box = QGroupBox()
        self.layout.addWidget(self.buttons_box)

        # Arrange buttons
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.Log_data_button)
        self.buttons_layout.addWidget(self.View_data_button)
        self.buttons_box.setLayout(self.buttons_layout)
        self.buttons_box.setStyleSheet(stylesheets.Big_Buttons_Box)
        self.setLayout(self.layout)