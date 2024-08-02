from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

class Dashboard_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0

        
        ################################################################
        # 
        # After input, show a Tab Dialog with tabs:
        #   Mission Overview
        #   Last 10 Missions
        #   Career Overview
        #   Raw Data
        #
        ################################################################