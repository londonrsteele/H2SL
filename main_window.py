from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QMainWindow, QStackedWidget)
from MyWidgets import (Welcome_widget, Log_data_widget, EOM_input_widget,
                       CAR_input_widget, Load_data_widget)

################################################################
# 
# MainWindow class
#
################################################################
class MainWindow(QMainWindow):
    ################################################################
    # MainWindow initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Helldivers II Stats Logger")
        
        # Menu bar
        self.menu = self.menuBar()

        # File menu
        self.file_menu = self.menu.addMenu("File")
        # File > Home QAction    
        home_action = self.file_menu.addAction("Home", self.view_Welcome)
        # File > Exit QAction
        exit_action = self.file_menu.addAction("Exit", self.close)
        exit_action.setShortcut("Ctrl+Q")

        # Back button
        back_action = self.menu.addAction("Back", self.go_back_action)
        back_icon = QIcon("./assets/left.png")
        back_action.setIcon(back_icon)

        # Create widgets
        Welcome = Welcome_widget.Welcome_widget()
        Log_data = Log_data_widget.Log_data_widget()
        EOM_input = EOM_input_widget.EOM_input_widget()
        CAR_input = CAR_input_widget.CAR_input_widget()
        Load_data = Load_data_widget.Load_data_widget()

        # Central Widget
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Welcome)   # index 0
        self.stackedWidget.addWidget(Log_data)  # index 1
        self.stackedWidget.addWidget(EOM_input) # index 2
        self.stackedWidget.addWidget(CAR_input) # index 3
        self.stackedWidget.addWidget(Load_data) # index 4
        
        # opening "screen"/widget is Welcome 
        self.stackedWidget.setCurrentWidget(Welcome)        
        self.setCentralWidget(self.stackedWidget)

        # Set up button functionality
        # Welcome buttons
        Welcome.Log_data_button.clicked.connect(self.view_Log_data)
        Welcome.View_data_button.clicked.connect(self.view_View_data)
        # Log_data buttons
        Log_data.Log_EOM_data.clicked.connect(self.view_EOM_input)
        Log_data.Log_CAR_data.clicked.connect(self.view_CAR_input)
        # EOM_input buttons
        EOM_input.view_button.clicked.connect(self.view_Load_data)
        # CAR_input buttons
        CAR_input.view_button.clicked.connect(self.view_Load_data)
        # Load_data buttons

    ################################################################
    # MainWindow member function: view_Welcome
    ################################################################    
    def view_Welcome(self):
        self.setWindowTitle("Helldivers 2 Stats Logger: Welcome")
        self.stackedWidget.setCurrentIndex(0)

    ################################################################
    # MainWindow member function: view_Log_data
    ################################################################    
    def view_Log_data(self):
        self.setWindowTitle("Helldivers 2 Stats Logger: Log Data")
        self.stackedWidget.setCurrentIndex(1)

    ################################################################
    # MainWindow member function: view_EOM_input
    ################################################################    
    def view_EOM_input(self):
        self.setWindowTitle("Helldivers 2 Stats Logger: Log Mission Data")
        self.stackedWidget.setCurrentIndex(2)

    ################################################################
    # MainWindow member function: view_CAR_input
    ################################################################    
    def view_CAR_input(self):
        self.setWindowTitle("Helldivers 2 Stats Logger: Log Career Data")
        self.stackedWidget.setCurrentIndex(3)

    ################################################################
    # MainWindow member function: view_Load_data
    ################################################################    
    def view_Load_data(self):
        self.setWindowTitle("Helldivers 2 Stats Logger: Load Data")
        self.stackedWidget.setCurrentIndex(4)

    ################################################################
    # MainWindow member function: view_View_data
    ################################################################    
    def view_View_data(self):
        self.setWindowTitle("Helldivers 2 Stats Logger: View Data")
        self.stackedWidget.setCurrentIndex(4)

    def go_back_action(self):
        if self.stackedWidget.currentIndex() != 0:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)