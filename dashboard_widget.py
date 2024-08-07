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
import webbrowser
import subprocess

################################################################
# 
# Dashboard_Widget class
#
################################################################
class Dashboard_Widget(QDialog):
    ################################################################
    # Dashboard_Widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0
        
        # Make Tab Widget
        self.tab_widget = QTabWidget()

        # Make Tabs
        self.Mission_Tab = Mission_Tab(self)
        self.Last10_Tab = Last10_Tab(self)
        self.Career_Tab = Career_Tab(self)
        self.RawData_Tab = RawData_Tab(self)

        # Add Tabs to Tab Widget
        self.tab_widget.addTab(self.Mission_Tab, "Mission Overview")
        self.tab_widget.addTab(self.Last10_Tab, "Last 10 Missions")
        self.tab_widget.addTab(self.Career_Tab, "Career Overview")
        self.tab_widget.addTab(self.RawData_Tab, "Raw Data")

        # Add Tab Widget to layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)
    
    ################################################################
    # Dashboard_Widget member function: load_EOM_data : connected to MainWindow
    ################################################################
    def load_EOM_data(self):
        EOM_df = self.Mission_Tab.load_data("EOM")
        self.Mission_Tab.display_data(EOM_df)

    ################################################################
    # Dashboard_Widget member function: load_CAR_data : connected to MainWindow
    ################################################################
    def load_CAR_data(self):
        CAR_df = self.Career_Tab.load_data("career")
        self.Career_Tab.display_data(CAR_df)

    ################################################################
    # Dashboard_Widget member function: load_demo_data : connected to MainWindow
    ################################################################
    def load_demo_data(self):
        print("Demo Data loaded successfully")

################################################################
# 
# Mission_Tab class
#
################################################################
class Mission_Tab(QWidget):
    ################################################################
    # Mission_Tab initialization
    ################################################################
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        # save savefile_dir
        self.savefile_dir = "./save_files/"

        # Set up layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # load most recent EOM data
        EOM_df = self.load_data("EOM")

        # display data
        display_label = self.display_data(EOM_df)
        self.layout.addWidget(display_label, Qt.AlignCenter)

    ################################################################
    # Mission_Tab member function: load_data
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
        
    ################################################################
    # Mission_Tab member function: display_data
    ################################################################
    def display_data(self, EOM_df):
        # see if data loaded correctly
        if EOM_df.empty:
            # data did not load
            error_label = QLabel("No Mission Save Files Loaded")
            return error_label
        else:
            # data loaded successfully
            print(EOM_df.head())
            success_label = QLabel("Yippee! Data Loaded!")    
            return success_label
    
    def display_insights(self, EOM_df):
        subprocess.Popen("python browser_mw.py")


################################################################
# 
# Last10_Tab class
#
################################################################
class Last10_Tab(QWidget):
    ################################################################
    # Last10_Tab initialization
    ################################################################
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        # save savefile_dir
        self.savefile_dir = "./save_files/"

        # Set up layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # get dictionary with 10 (or less) DataFrames
        df_dict = self.load_10_data("EOM")

        # see if any data loaded
        display_label = self.display_data(df_dict)
        self.layout.addWidget(display_label, Qt.AlignCenter)
    
    ################################################################
    # Last10_Tab member function: load_data
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

    ################################################################
    # Last10_Tab member function: load_10_data
    ################################################################
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
    
    ################################################################
    # Last10_Tab member function: display_data
    ################################################################
    def display_data(self, df_dict):
        if len(df_dict) == 0:
            # data did not load
            error_label = QLabel("No Mission Save Files Loaded")
            return error_label
        else:
            # get number of Missions returned
            print("# of Missions Loaded: " + str(len(df_dict)))
            success_label = QLabel(str(len(df_dict)) + " Missions Loaded")
            return success_label

################################################################
# 
# Career_Tab class
#
################################################################
class Career_Tab(QWidget):
    ################################################################
    # Career_Tab initialization
    ################################################################
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        # save savefile_dir
        self.savefile_dir = "./save_files/"

        # Set up layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # load most recent EOM data
        CAR_df = self.load_data("career")

        # see if data loaded correctly
        display_label = self.display_data(CAR_df)
        self.layout.addWidget(display_label, Qt.AlignCenter)

    ################################################################
    # Career_Tab member function: load_data
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

    ################################################################
    # Career_Tab member function: display_data
    ################################################################
    def display_data(self, CAR_df):
        if CAR_df.empty:
            # data did not load
            error_label = QLabel("No Career Save Files Loaded")
            return error_label
        else:
            # data loaded successfully
            print(CAR_df.head())
            success_label = QLabel("Yippee! Data Loaded!")
            return success_label

################################################################
# 
# RawData_Tab class
#
################################################################
class RawData_Tab(QWidget):
    ################################################################
    # RawData_Tab initialization
    ################################################################    
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        # save savefile_dir
        self.savefile_dir = "./save_files/"

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
