import os, fnmatch
from pathlib import Path
import pandas as pd
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QDialog, QWidget, QTabWidget,
                               QLabel)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

class Dashboard_Widget(QDialog):
    ################################################################
    # 
    # Dashboard_Widget initialization
    #
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0

        # save files directory
        self.savefile_dir = "./save_files/"
        
        # Make Tab Widget
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(Mission_Tab(self), "Mission Overview")
        self.tab_widget.addTab(Last10_Tab(self), "Last 10 Missions")
        self.tab_widget.addTab(Career_Tab(self), "Career Overview")
        self.tab_widget.addTab(RawData_Tab(self), "Raw Data")

        # Add Tab Widget to layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

        ################################################################
        # 
        # After input, show a Tab Dialog with tabs:
        #   Mission Overview
        #   Last 10 Missions
        #   Career Overview
        #   Raw Data
        #
        ################################################################

    def load_data(self, data_class):
        # sort data_class files in directory by modified time
        filepaths = sorted(Path(self.savefile_dir).iterdir(), key=os.path.getmtime)
        
        most_recent_file_path = ""
        # find most recent data_class (EOM, CAR, loadout) file (closest to index 0)
        for filepath in filepaths:
            if filepath.name.startswith(data_class):
                most_recent_file_path = filepath
                break
        
        # if most_recent_file_path is empty, no save file exists for that data_class
        if most_recent_file_path == "":
            print("No save file exists!")
            # return empty df
            return pd.DataFrame()
        else:
            # load data from most recent file into dataframe
            df = pd.read_csv(most_recent_file_path)
            return df

    def load_10_data(self, data_class):
        # sort files in directory by modified time
        filepaths = sorted(Path(self.savefile_dir).iterdir(), key=os.path.getmtime)
        
        # get top 10 data_class files and load into dataframes
        dict_of_dfs = {}
        df_count = 0
        for filepath in filepaths:
            if filepath.name.startswith(data_class):
                dict_of_dfs[df_count] = pd.read_csv(self.savefile_dir+filepath.name)
                df_count +=1
                if df_count == 10:
                    break
        
        # return dictionary of dataframes
        return dict_of_dfs

class Mission_Tab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        # Set up layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # load most recent EOM data
        EOM_df = parent.load_data("EOM")
        # see if data loaded correctly
        if EOM_df.empty:
            # data did not load
            error_label = QLabel("No Mission Save Files Loaded")
            layout.addWidget(error_label, Qt.AlignCenter)
        else:
            # data loaded successfully
            print(EOM_df.head())
            success_label = QLabel("Yippee! Data Loaded!")
            layout.addWidget(success_label, Qt.AlignCenter)


class Last10_Tab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # Set up layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # get dictionary with 10 (or less) DataFrames
        df_dict = parent.load_10_data("EOM")

        # see if any data loaded
        if len(df_dict) == 0:
            # data did not load
            error_label = QLabel("No Mission Save Files Loaded")
            layout.addWidget(error_label, Qt.AlignCenter)
        else:
            # get number of Missions returned
            print("# of Missions Loaded: " + str(len(df_dict)))
            success_label = QLabel(str(len(df_dict)) + " Missions Loaded")
            layout.addWidget(success_label, Qt.AlignCenter)


class Career_Tab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        # Set up layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # load most recent EOM data
        CAR_df = parent.load_data("career")
        # see if data loaded correctly
        if CAR_df.empty:
            # data did not load
            error_label = QLabel("No Career Save Files Loaded")
            layout.addWidget(error_label, Qt.AlignCenter)
        else:
            # data loaded successfully
            print(CAR_df.head())
            success_label = QLabel("Yippee! Data Loaded!")
            layout.addWidget(success_label, Qt.AlignCenter)


class RawData_Tab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)


    # def load_demo_data(self):
    #     layout = QVBoxLayout()
    #     self.setLayout(layout)
    #     self.table_widget = QTableWidget()
    #     layout.addWidget(self.table_widget)
    #     self.setCentralWidget(self.table_widget)

    #     # load into pandas dataframe for convenience
    #     EOM_df = pd.read_csv("./demo_EOM_data.csv")
    #     CAR_df = pd.read_csv("./demo_CAR_data.csv")

    #     # set bounds of table
    #     self.table_widget.setRowCount(len(EOM_df))
    #     self.table_widget.setColumnCount(len(EOM_df.columns))
    #     self.table_widget.setHorizontalHeaderLabels(list(EOM_df.columns))

    #     # convert to numpy array for speed (iteration)
    #     EOM_np = EOM_df.to_numpy()
    #     CAR_np = EOM_df.to_numpy()

    #     # fill table with data
    #     for row in range(len(EOM_np)):
    #         for col in range(len(EOM_np[row])):
    #             self.table_widget.setItem(row, col, QTableWidgetItem(str(EOM_np[row][col])))

    ################################################################
    # 
    # Dashboard_Widget member functions
    #
    ################################################################
    def load_CAR_data(self):
        print("Career Data loaded successfully")

    def load_EOM_data(self):
        print("End of Mission Data loaded successfully")

    def load_demo_data(self):
        print("Demo Data loaded successfully")