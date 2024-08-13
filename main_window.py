from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QMainWindow, QStackedWidget, QFileDialog)
from MyWidgets import (Welcome_widget, Log_data_widget, EOM_input_widget,
                       CAR_input_widget, Load_data_widget)
from assets import SAVE_PATH
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
        # File > Change Save File Directory
        savefile_action = self.file_menu.addAction("Change Save File Directory", self.change_save_dir)
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

    ################################################################
    # MainWindow member function: go_back_action
    ################################################################
    def go_back_action(self):
        if self.stackedWidget.currentIndex() != 0:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)

    ################################################################
    # MainWindow member function: change_save_dir
    ################################################################
    def change_save_dir(self):
        directories = []
        # open a file explorer window and show only directories
        file_explorer = QFileDialog(parent=None, caption="Choose a Save File Directory", directory=SAVE_PATH.save_path)
        file_explorer.setFileMode(QFileDialog.Directory)
        if file_explorer.exec_():
            # get selected directory
            directories = file_explorer.selectedFiles()
        # check if old_filenames is empty
        if directories:
            print("directory = " + str(directories[0]))
            # not empty, load the first filename(directory) only
            SAVE_PATH.save_path = directories[0]
            with open("./assets/SAVE_PATH.py", "w") as savefile:
                savefile.write("save_path = \""+directories[0] + "\"")
        else:
            # note: do not raise an exception here, value gets handled elsewhere
            return str("Error: No File Loaded")