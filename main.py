import sys
import pandas as pd
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

from main_window import MainWindow
from input_widget import Input_Widget
from dashboard_widget import Dashboard_Widget

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    input_widget = Input_Widget()
    dashboard_widget = Dashboard_Widget()

    # QMainWindow using QWidget as central widget
    window = MainWindow(input_widget, dashboard_widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())