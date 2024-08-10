import os, fnmatch
from pathlib import Path
import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QGridLayout, QPushButton,
                               QVBoxLayout, QDialog, QWidget, QTabWidget,
                               QLabel, QMessageBox, QFileDialog)
import subprocess
from assets import stylesheets

################################################################
# 
# Mission_Tab class
#
################################################################
class Mission_Tab(QWidget):
    ################################################################
    # Mission_Tab initialization
    ################################################################
    def __init__(self, parent: QWidget, datafile):
        super().__init__(parent)
        # set up layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # validate datafile
        if (datafile == "") | (datafile == "Error: No File Loaded"):
            # Create warning label
            Warning_Label = QLabel("Warning: No Misison file loaded")
            self.layout.addWidget(Warning_Label)
            print("Warning: No Mission file loaded")
        else:
            # load data
            self.data = pd.read_csv("./save_files/"+datafile)
            print(self.data)

            # Create data labels
            Accuracy = QLabel("Accuracy: " + str(self.data["eom_accuracy"][0]) + "%")

            # Add data labels
            self.layout.addWidget(Accuracy)


################################################################
# 
# Career_Tab class
#
################################################################
class Career_Tab(QWidget):
    ################################################################
    # Career_Tab initialization
    ################################################################
    def __init__(self, parent: QWidget, datafile):
        super().__init__(parent)
        # set up layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # validate datafile
        if (datafile == "") | (datafile == "Error: No File Loaded"):
            # Create warning label
            Warning_Label = QLabel("Warning: No Career file loaded")
            self.layout.addWidget(Warning_Label)
            print("Warning: No Career file loaded")
        else:
            # load data
            self.data = pd.read_csv("./save_files/"+datafile)
            print(self.data)

            # Create data labels
            Accuracy = QLabel("Enemy kills")

            # Add data labels
            self.layout.addWidget(Accuracy)