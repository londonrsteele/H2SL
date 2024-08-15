import os
import subprocess
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QWidget,
                                QGroupBox, QLabel, QLineEdit)
from MyWidgets import Data_mw
from assets import stylesheets
from graphing import stat_scraper
################################################################
# 
# Load_data_widget class
#
################################################################
class Load_data_widget(QWidget):
    ################################################################
    # Load_data_widget initialization
    ################################################################
    def __init__(self):
        super().__init__()
        self.items = 0
        
        # Make Title  
        self.Title = QLabel()
        self.Title.setStyleSheet(stylesheets.Title)
        self.Title.setText("Load Data")
        self.Title.setAlignment(Qt.AlignCenter)
        
        # Create QGroupBoxes
        # Left (EOM)
        self.EOM_box = QGroupBox()
        self.EOM_box_layout = QVBoxLayout()
        self.EOM_box_title = QLabel()
        self.EOM_box_title.setText("Mission:")
        self.EOM_box_title.setStyleSheet(stylesheets.Title)
        self.EOM_box_title.setAlignment(Qt.AlignCenter)
        self.EOM_box_layout.addWidget(self.EOM_box_title)
        self.EOM_filename_box = QLineEdit()
        self.EOM_filename_box.setReadOnly(True)
        self.EOM_box_layout.addWidget(self.EOM_filename_box)
        self.EOM_buttons_box = QGroupBox()
        self.EOM_buttons_box.setStyleSheet(stylesheets.Big_Buttons_Box)
        self.EOM_buttons_layout = QHBoxLayout()
        self.EOM_MR_button = QPushButton("Most Recent")
        self.EOM_MR_button.setStyleSheet(stylesheets.Big_Buttons)
        self.EOM_OLD_button = QPushButton("Other...")
        self.EOM_OLD_button.setStyleSheet(stylesheets.Big_Buttons)
        self.EOM_buttons_layout.addWidget(self.EOM_MR_button)
        self.EOM_buttons_layout.addWidget(self.EOM_OLD_button)
        self.EOM_buttons_box.setLayout(self.EOM_buttons_layout)
        self.EOM_box_layout.addWidget(self.EOM_buttons_box)
        self.EOM_box.setLayout(self.EOM_box_layout)
        # Right (CAR)
        self.CAR_box = QGroupBox()
        self.CAR_box_layout = QVBoxLayout()
        self.CAR_box_title = QLabel()
        self.CAR_box_title.setText("Career:")
        self.CAR_box_title.setStyleSheet(stylesheets.Title)
        self.CAR_box_title.setAlignment(Qt.AlignCenter)
        self.CAR_box_layout.addWidget(self.CAR_box_title)
        self.CAR_filename_box = QLineEdit()
        self.CAR_filename_box.setReadOnly(True)
        self.CAR_box_layout.addWidget(self.CAR_filename_box)
        self.CAR_buttons_box = QGroupBox()
        self.CAR_buttons_box.setStyleSheet(stylesheets.Big_Buttons_Box)
        self.CAR_buttons_layout = QHBoxLayout()
        self.CAR_MR_button = QPushButton("Most Recent")
        self.CAR_MR_button.setStyleSheet(stylesheets.Big_Buttons)
        self.CAR_OLD_button = QPushButton("Other...")
        self.CAR_OLD_button.setStyleSheet(stylesheets.Big_Buttons)
        self.CAR_buttons_layout.addWidget(self.CAR_MR_button)
        self.CAR_buttons_layout.addWidget(self.CAR_OLD_button)
        self.CAR_buttons_box.setLayout(self.CAR_buttons_layout)
        self.CAR_box_layout.addWidget(self.CAR_buttons_box)
        self.CAR_box.setLayout(self.CAR_box_layout)

        # Connect internal buttons
        self.EOM_MR_button.clicked.connect(self.load_MR_EOM_datafile)
        self.EOM_OLD_button.clicked.connect(self.load_OLD_EOM_datafile)
        self.CAR_MR_button.clicked.connect(self.load_MR_CAR_datafile)
        self.CAR_OLD_button.clicked.connect(self.load_OLD_CAR_datafile)

        # Set up inner layout
        self.Qboxes_box = QGroupBox()
        self.Qboxes_box_layout = QHBoxLayout()
        self.Qboxes_box_layout.addWidget(self.EOM_box)
        self.Qboxes_box_layout.addWidget(self.CAR_box)
        self.Qboxes_box.setLayout(self.Qboxes_box_layout)
        
        # Make View Data button
        self.view_buttons_box = QGroupBox()
        self.view_buttons_box_layout = QHBoxLayout()
        self.view_buttons_box.setStyleSheet(stylesheets.Big_Buttons_Box)
        self.view_EOM_button = QPushButton("View Mission Data", self)
        self.view_EOM_button.setStyleSheet(stylesheets.Big_Buttons)
        self.view_CAR_button = QPushButton("View Career Data", self)
        self.view_CAR_button.setStyleSheet(stylesheets.Big_Buttons)
        self.view_BOTH_button = QPushButton("View Dashboard", self)
        self.view_BOTH_button.setStyleSheet(stylesheets.Big_Buttons)
        self.view_buttons_box_layout.addWidget(self.view_EOM_button)
        self.view_buttons_box_layout.addWidget(self.view_CAR_button)
        self.view_buttons_box_layout.addWidget(self.view_BOTH_button)
        self.view_buttons_box.setLayout(self.view_buttons_box_layout)

        # Set all buttons to disabled by default
        self.view_EOM_button.setDisabled(True)
        self.view_CAR_button.setDisabled(True)
        self.view_BOTH_button.setDisabled(True)

        # If Files loaded, make buttons available
        self.EOM_filename_box.textChanged.connect(self.restrict_buttons)
        self.CAR_filename_box.textChanged.connect(self.restrict_buttons)

        # If buttons available, connect them!
        self.view_EOM_button.clicked.connect(self.view_EOM_data)
        self.view_CAR_button.clicked.connect(self.view_CAR_data)
        self.view_BOTH_button.clicked.connect(self.view_dashboard)

        # Set up outer layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.Title)
        self.layout.addWidget(self.Qboxes_box)
        self.layout.addWidget(self.view_buttons_box)
        self.setLayout(self.layout)

    ################################################################
    # Load_data_widget member function: load_MR_EOM_data
    ################################################################
    def load_MR_EOM_datafile(self):
        # use Stat_Scraper to get most recent filename
        scraper = stat_scraper.Stat_Scraper()
        datafile = scraper.get_MR_filename("EOM")

        # check if an appropriate save file is returned
        if datafile == "Error: No File Loaded":
            self.EOM_filename_box.setText("Error: No File Loaded")
        else:
            filename = os.path.basename(datafile)
            self.EOM_filename_box.setText(str(filename))
    
    ################################################################
    # Load_data_widget member function: load_OLD_EOM_data
    ################################################################
    def load_OLD_EOM_datafile(self):
        # use Stat_Scraper to get old filename
        scraper = stat_scraper.Stat_Scraper()
        datafile = scraper.get_OLD_filename("EOM")
        self.EOM_filename_box.setText(datafile)
    
    ################################################################
    # Load_data_widget member function: load_MR_CAR_data
    ################################################################
    def load_MR_CAR_datafile(self):
        # use Stat_Scraper to get most recent filename
        scraper = stat_scraper.Stat_Scraper()
        datafile = scraper.get_MR_filename("career")

        # check if an appropriate save file is returned
        if datafile == "Error: No File Loaded":
            self.CAR_filename_box.setText("Error: No File Loaded")
        else:
            filename = os.path.basename(datafile)
            self.CAR_filename_box.setText(str(filename))
    
    ################################################################
    # Load_data_widget member function: load_OLD_CAR_data
    ################################################################
    def load_OLD_CAR_datafile(self):
        # use Stat_Scraper to get old filename
        scraper = stat_scraper.Stat_Scraper()
        datafile = scraper.get_OLD_filename("CAR")
        self.CAR_filename_box.setText(datafile)

    ################################################################
    # Load_data_widget member function: restrict_buttons
    ################################################################
    def restrict_buttons(self):
        # restrict View EOM Button pressing
        if (self.EOM_filename_box.text() == "") | (self.EOM_filename_box.text() == "Error: No File Loaded"):
            self.view_EOM_button.setDisabled(True)
        else:
            self.view_EOM_button.setEnabled(True)
        
        # restrict View CAR Button pressing
        if (self.CAR_filename_box.text() == "") | (self.CAR_filename_box.text() == "Error: No File Loaded"):
            self.view_CAR_button.setDisabled(True)
        else:
            self.view_CAR_button.setEnabled(True)
        
        # restrict View Both Button pressing
        if (self.EOM_filename_box.text() == "") | (self.EOM_filename_box.text() == "Error: No File Loaded"):
            self.view_BOTH_button.setDisabled(True)
        elif (self.CAR_filename_box.text() == "") | (self.CAR_filename_box.text() == "Error: No File Loaded"):
            self.view_BOTH_button.setDisabled(True)
        else:
            self.view_BOTH_button.setEnabled(True)

    ################################################################
    # Load_data_widget member function: view_EOM_data
    ################################################################
    def view_EOM_data(self):
        # get paths for appropriate save files
        EOM_datafile = self.EOM_filename_box.text()
        CAR_datafile = self.CAR_filename_box.text()
        
        print("Opening Data Viewer...")

        # open new data view window
        self.View_Data_mw = Data_mw.Data_mw(EOM_datafile, CAR_datafile, "EOM")
        self.View_Data_mw.setStyleSheet(stylesheets.Text)
        self.View_Data_mw.resize(800, 600)
        self.View_Data_mw.show()

        # handle "View Dashboard" button
        self.View_Data_mw.Mission_Tab.view_dashboard_button.clicked.connect(self.view_EOM_dashboard)
        self.View_Data_mw.Career_Tab.view_dashboard_button.clicked.connect(self.view_CAR_dashboard)

    ################################################################
    # Load_data_widget member function: view_EOM_data
    ################################################################
    def view_CAR_data(self):
        # get paths for appropriate save files
        EOM_datafile = self.EOM_filename_box.text()
        CAR_datafile = self.CAR_filename_box.text()

        print("Opening Data Viewer...")

        # open new data view window
        self.View_Data_mw = Data_mw.Data_mw(EOM_datafile, CAR_datafile, "CAR")
        self.View_Data_mw.setStyleSheet(stylesheets.Text)
        self.View_Data_mw.resize(800, 600)
        self.View_Data_mw.show()

        # handle "View Dashboard" button
        self.View_Data_mw.Mission_Tab.view_dashboard_button.clicked.connect(self.view_EOM_dashboard)
        self.View_Data_mw.Career_Tab.view_dashboard_button.clicked.connect(self.view_CAR_dashboard)

    ################################################################
    # Load_data_widget member function: view_EOM_dashboard
    ################################################################
    def view_EOM_dashboard(self):
        # get paths for appropriate save files
        EOM_datafile = self.EOM_filename_box.text()
        CAR_datafile = self.CAR_filename_box.text()
        
        # If empty strings, add "ERROR" to string so still pass a second argv argument
        if EOM_datafile == "":
            EOM_datafile = "ERROR"
        if CAR_datafile == "":
            CAR_datafile = "ERROR"
    
        print("Opening Misison Dashboard...")

        # open new browser window (for Dash)
        #  argv1 = EOM/CAR/BOTH, argv2 = EOM_datafile, argv3 = CAR_datafile 
        subprocess.Popen(["python", "browser_mw.py", "EOM", str(EOM_datafile), str(CAR_datafile)])

    ################################################################
    # Load_data_widget member function: view_CAR_dashboard
    ################################################################
    def view_CAR_dashboard(self):
        # get paths for appropriate save files
        EOM_datafile = self.EOM_filename_box.text()
        CAR_datafile = self.CAR_filename_box.text()
        
        # If empty strings, add "ERROR" to string so still pass a second argv argument
        if EOM_datafile == "":
            EOM_datafile = "ERROR"
        if CAR_datafile == "":
            CAR_datafile = "ERROR"
        
        print("Opening Career Dashboard...")

        # open new browser window (for Dash)
        #  argv1 = EOM/CAR/BOTH, argv2 = EOM_datafile, argv3 = CAR_datafile 
        subprocess.Popen(["python", "browser_mw.py", "CAR", str(EOM_datafile), str(CAR_datafile)])

    ################################################################
    # Load_data_widget member function: view_dashboard
    ################################################################
    def view_dashboard(self):
        # get paths for appropriate save files
        EOM_datafile = self.EOM_filename_box.text()
        CAR_datafile = self.CAR_filename_box.text()
        
        # If empty strings, add "ERROR" to string so still pass a second argv argument
        if EOM_datafile == "":
            EOM_datafile = "ERROR"
        if CAR_datafile == "":
            CAR_datafile = "ERROR"
        
        print("Opening Dashboard...")

        # open new browser window (for Dash)
        #  argv1 = EOM/CAR/BOTH, argv2 = EOM_datafile, argv3 = CAR_datafile 
        subprocess.Popen(["python", "browser_mw.py", "BOTH", str(EOM_datafile), str(CAR_datafile)])

