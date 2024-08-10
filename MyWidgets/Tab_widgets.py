import os, fnmatch
from pathlib import Path
import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QHBoxLayout, QPushButton,
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