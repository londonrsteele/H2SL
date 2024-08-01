import sys
import pandas as pd
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("Helldivers II Stats Logger")

        # Menu bar
        self.menu = self.menuBar()
        
        # File menu
        self.file_menu = self.menu.addMenu("File")
        # File > Exit QAction
        exit_action = self.file_menu.addAction("Exit", self.close)
        exit_action.setShortcut("Ctrl+Q")

        # Data menu
        self.data_menu = self.menu.addMenu("Data")
        # Data > Add Data menu
        self.data_add_data_menu = self.data_menu.addMenu("Add Data")
        # Data > Add Data > Career Data QAction
        career_data_action = self.data_add_data_menu.addAction("Career Data", self.close)
        # Data > Add Data > EOM Data QAction
        EOM_data_action = self.data_add_data_menu.addAction("EOM Data", self.close) 
        # Data > Load Data menu
        self.data_load_data_menu = self.data_menu.addMenu("Load Data")
        ################################################################
        # 
        # Add functionality here: List of Save/Load files in dropdown (10 most recent)
        #
        ################################################################
        # Data > Load Data > Demo Data QAction
        demo_data_action = self.data_load_data_menu.addAction("Demo Data", self.close)

        self.setCentralWidget(widget)