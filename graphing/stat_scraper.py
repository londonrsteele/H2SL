import os
from pathlib import Path
import pandas as pd
from PySide6.QtWidgets import QFileDialog

class Stat_Scraper():
    def __init__(self):
       self.filenames = sorted(Path("./save_files/").iterdir(), key=os.path.getmtime, reverse=True)

    def get_MR_filename(self, type):
        if type == "CAR":
            type = "career"
        for filename in self.filenames:
            if filename.name.startswith(type):
                datafile = filename
                break
        # if datafile is empty, no save EOM file exists
        if datafile == "":
            return str("Error: No File Loaded")
        else:
            return filename
    
    def get_OLD_filename(self, type):
        filenames = []
        if type == "EOM":
            # open a file explorer window
            file_explorer = QFileDialog(self, "Choose a Mission Data File", "./save_files/")
            file_explorer.setFileMode(QFileDialog.ExistingFile)
            # show only EOM files
            file_explorer.setNameFilter("EOM_savefile_*.csv")
            if file_explorer.exec_():
                # get selected filename(s)
                filenames = file_explorer.selectedFiles()
        elif type == "CAR":
            # open a file explorer window
            file_explorer = QFileDialog(self, "Choose a Career Data File", "./save_files/")
            file_explorer.setFileMode(QFileDialog.ExistingFile)
            # show only EOM files
            file_explorer.setNameFilter("career_savefile_*.csv")
            if file_explorer.exec_():
                # get selected filename(s)
                filenames = file_explorer.selectedFiles()
        elif type == "loadout":
            # open a file explorer window
            file_explorer = QFileDialog(self, "Choose a Loadout Data File", "./save_files/")
            file_explorer.setFileMode(QFileDialog.ExistingFile)
            # show only EOM files
            file_explorer.setNameFilter("loadout_savefile_*.csv")
            if file_explorer.exec_():
                # get selected filename(s)
                filenames = file_explorer.selectedFiles()
        # check if filenames is empty
        if filenames:
            #load the first filename only
            filename = os.path.basename(filenames[0])
            return filename
        else:
            return str("Error: No File Loaded")

    def load_file(self, filename):
        if (filename != "Error: No File Loaded") & (filename != "ERROR"):
            return pd.read_csv("./save_files/"+filename)
        else:
            return pd.DataFrame()
        
    