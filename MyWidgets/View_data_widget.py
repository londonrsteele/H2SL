import pandas as pd
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import (QFormLayout, QPushButton, QWidget,
                                QGroupBox, QDateEdit, QTimeEdit,
                                QGridLayout, QSpinBox, QMessageBox,
                                QFrame)
from assets import stylesheets
################################################################
# 
# View_data_widget class
#
################################################################
class View_data_widget(QWidget):
    ################################################################
    # View_data_widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0
        