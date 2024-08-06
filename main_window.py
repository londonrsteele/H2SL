from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QMainWindow, QStackedWidget, QStatusBar, QLabel)

################################################################
# 
# MainWindow class
#
################################################################
class MainWindow(QMainWindow):
    ################################################################
    # MainWindow initialization
    ################################################################
    def __init__(self, CAR_input_widget, EOM_input_widget, dashboard_widget):
        super().__init__()
        self.setWindowTitle("Helldivers II Stats Logger")
        
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
        career_data_action = self.data_add_data_menu.addAction("Career Data", self.view_CAR_input)
        # Data > Add Data > Misison Data QAction
        EOM_data_action = self.data_add_data_menu.addAction("Mission Data", self.view_EOM_input) 

        # Data > Load Data menu
        self.data_load_data_menu = self.data_menu.addMenu("Load Data")
        # Data > Load Data > Career Data QAction
        CAR_data_action = QAction("Career Data", self)
        CAR_data_action.triggered.connect(dashboard_widget.load_CAR_data)
        CAR_data_action.triggered.connect(self.view_dashboard)
        self.data_load_data_menu.addAction(CAR_data_action)

        # Data > Load Data > Mission Data QAction
        EOM_data_action = QAction("Mission Data", self)
        EOM_data_action.triggered.connect(dashboard_widget.load_EOM_data)
        EOM_data_action.triggered.connect(self.view_dashboard)
        self.data_load_data_menu.addAction(EOM_data_action)

        # Data > Load Data > Demo Data QAction
        self.data_load_data_menu.addSeparator()
        demo_data_action = QAction("Demo Data", self)
        demo_data_action.triggered.connect(dashboard_widget.load_demo_data)
        demo_data_action.triggered.connect(self.view_dashboard)
        self.data_load_data_menu.addAction(demo_data_action)
        
        # Central Widget
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(CAR_input_widget)
        self.stackedWidget.addWidget(EOM_input_widget)
        self.stackedWidget.addWidget(dashboard_widget)
        
        # default "screen" of widget is EOM data entry 
        self.stackedWidget.setCurrentWidget(EOM_input_widget)        
        self.setCentralWidget(self.stackedWidget)

        # if "View Mission Data" button is clicked, view dashboard
        EOM_input_widget.view_button.clicked.connect(self.view_dashboard)
        CAR_input_widget.view_button.clicked.connect(self.view_dashboard)

    ################################################################
    # MainWindow member function: view_CAR_input
    ################################################################
    def view_CAR_input(self):
        self.stackedWidget.setCurrentIndex(0) # Career Data Input Widget is at index 0

    ################################################################
    # MainWindow member function: view_EOM_input
    ################################################################
    def view_EOM_input(self):
        self.stackedWidget.setCurrentIndex(1) # EOM Data input widget is at index 1

    ################################################################
    # MainWindow member function: view_dashboard
    ################################################################
    def view_dashboard(self):        
        self.stackedWidget.setCurrentIndex(2) # Dashboard widget is at index 2