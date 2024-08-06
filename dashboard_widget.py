from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
from PySide6.QtCharts import QChartView, QPieSeries, QChart

class Dashboard_Widget(QWidget):
    ################################################################
    # 
    # Dashboard_Widget initialization
    #
    ################################################################
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