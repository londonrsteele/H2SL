import sys
import csv
import pandas as pd
from PySide6.QtCore import Qt, Slot, QObject
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QStackedWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

class MainWindow(QMainWindow):
    def __init__(self, input_widget, dashboard_widget):
        super().__init__()
        self.setWindowTitle("Helldivers II Stats Logger")

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(input_widget)
        self.stackedWidget.addWidget(dashboard_widget)
        # default "screen" of widget is data entry 
        self.stackedWidget.setCurrentWidget(input_widget)        
        self.setCentralWidget(self.stackedWidget)

        # if "View EOM Data" button is clicked, view dashboard
        input_widget.view_button.clicked.connect(self.view_dashboard)

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
        career_data_action = self.data_add_data_menu.addAction("Career Data", self.view_input)
        # Data > Add Data > EOM Data QAction
        EOM_data_action = self.data_add_data_menu.addAction("EOM Data", self.view_input) 
        # Data > Load Data menu
        self.data_load_data_menu = self.data_menu.addMenu("Load Data")
        ################################################################
        # 
        # Add functionality here: List of Save/Load files in dropdown (10 most recent)
        #
        ################################################################
        # Data > Load Data > Demo Data QAction
        demo_data_action = self.data_load_data_menu.addAction("Demo Data", self.load_demo_data)
    
    @Slot()
    def view_input(self):
        self.stackedWidget.setCurrentIndex(0) # input widget is at index 0
    
    @Slot()
    def view_dashboard(self):        
        self.stackedWidget.setCurrentIndex(1) # dashboard widget is at index 1

    def load_demo_data(self):
        ################################################################
        # 
        # Move below chunk to be handled in dashboard_widget!!
        #
        ################################################################
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        self.setCentralWidget(self.table_widget)

        # load into pandas dataframe for convenience
        EOM_df = pd.read_csv("./demo_EOM_data.csv")
        CAR_df = pd.read_csv("./demo_CAR_data.csv")

        # set bounds of table
        self.table_widget.setRowCount(len(EOM_df))
        self.table_widget.setColumnCount(len(EOM_df.columns))
        self.table_widget.setHorizontalHeaderLabels(list(EOM_df.columns))

        # convert to numpy array for speed (iteration)
        EOM_np = EOM_df.to_numpy()
        CAR_np = EOM_df.to_numpy()

        # fill table with data
        for row in range(len(EOM_np)):
            for col in range(len(EOM_np[row])):
                self.table_widget.setItem(row, col, QTableWidgetItem(str(EOM_np[row][col])))


