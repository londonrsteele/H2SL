from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

class Input_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0
