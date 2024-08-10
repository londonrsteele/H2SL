from PySide6.QtWidgets import (QMainWindow, QTabWidget, QVBoxLayout)
from MyWidgets import (Tab_widgets)
################################################################
# 
# Data_mw class
#
################################################################
class Data_mw(QMainWindow):
    ################################################################
    # Data_mw initialization
    ################################################################
    def __init__(self, EOM_datafile, CAR_datafile):
        super().__init__()
        self.setWindowTitle("Helldivers II Stats Logger: Data Viewer")
        
        # Make Tab Widget
        self.Tab_Widget = QTabWidget()

        # Make Tabs
        self.Mission_Tab = Tab_widgets.Mission_Tab(self, EOM_datafile)
        self.Career_Tab = Tab_widgets.Career_Tab(self, CAR_datafile)

        # Add Tabs to Tab Widget
        self.Tab_Widget.addTab(self.Mission_Tab, "Mission")
        self.Tab_Widget.addTab(self.Career_Tab, "Career")

        # Add Tab Widget to main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.Tab_Widget)
        self.setLayout(self.layout)
        
        # Set Tab Widget as Central Widget 
        self.setCentralWidget(self.Tab_Widget)

        # TODO: view dashboard
