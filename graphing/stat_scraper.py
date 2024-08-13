import os
from pathlib import Path
import pandas as pd
from PySide6.QtWidgets import QFileDialog
from assets import SAVE_PATH
################################################################
#
# Stat_Scraper class
#
################################################################
class Stat_Scraper():
    ################################################################
    # Stat_Scraper initialization
    ################################################################
    def __init__(self):
       self.filenames = sorted(Path(SAVE_PATH.save_path+"/").iterdir(), key=os.path.basename, reverse=True)
       print(self.filenames)

    ################################################################
    # Stat_Scraper member function: get_files_of_type
    ################################################################
    def get_files_of_type(self, type):
        type_filenames = []
        # handle discrepancies on how "career" is passed through different functions
        if type == "CAR":
            type = "career"
        # go through all filenames in ./save_files/ (dir)
        for filename in self.filenames:
            # if is of type == type, append to type_filenames
            # note, because iterating through a sorted list,
            # first append is most recent, then second most, etc.
            if filename.name.startswith(type):
                type_filenames.append(os.path.basename(filename))
        return type_filenames

    ################################################################
    # Stat_Scraper member function: get_MR_filename
    ################################################################
    def get_MR_filename(self, type):
        # get files of type
        type_filenames = self.get_files_of_type(type)
        # if type_filenames is empty, no save type file exists
        if not type_filenames:
            raise RuntimeError("Error: No " + str(type) + " save file exists")
        else:
            # index 0 is most recent file of type
            return type_filenames[0]

    ################################################################
    # Stat_Scraper member function: get_OLD_filename
    ################################################################
    def get_OLD_filename(self, type):
        old_filenames = []
        if type == "EOM":
            # open a file explorer window and show only EOM files
            file_explorer = QFileDialog(parent=None, caption="Choose a Mission Data File", directory="./save_files/", filter="EOM_savefile_*.csv")
            file_explorer.setFileMode(QFileDialog.ExistingFile)
            if file_explorer.exec_():
                # get selected filename(s)
                old_filenames = file_explorer.selectedFiles()
        elif type == "CAR":
            # open a file explorer window and show only CAR files
            file_explorer = QFileDialog(parent=None, caption="Choose a Career Data File", directory="./save_files/", filter="career_savefile_*.csv")
            file_explorer.setFileMode(QFileDialog.ExistingFile)
            if file_explorer.exec_():
                # get selected filename(s)
                old_filenames = file_explorer.selectedFiles()
        elif type == "loadout":
        # open a file explorer window and show only loadout files
            file_explorer = QFileDialog(parent=None, caption="Choose a Loadout Data File", directory="./save_files/", filter="loadout_savefile_*.csv")
            file_explorer.setFileMode(QFileDialog.ExistingFile)
            if file_explorer.exec_():
                # get selected filename(s)
                old_filenames = file_explorer.selectedFiles()
        # check if old_filenames is empty
        if old_filenames:
            #load the first filename only
            filename = os.path.basename(old_filenames[0])
            return filename
        else:
            # note: do not raise an exception here, value gets handled elsewhere
            return str("Error: No File Loaded")

    ################################################################
    # Stat_Scraper member function: load_last10_filenames
    ################################################################
    def get_last10_filenames(self, type, passed_file):
        # get the files of type
        files_of_type_in_filenames = self.get_files_of_type(type)
        # get the index of the passed file in the files of type to see how many older files exist
        index_of_filename_in_files_of_type = files_of_type_in_filenames.index(passed_file)
        # compare that index to the number of files of type
        num_of_files_of_type = len(files_of_type_in_filenames)

        # make list of last 10 files, including passed file (index 0)
        older_files = []
        older_files.append(passed_file)

        # if index+1 (to account for 0-based indexing vs 1-based counting) == number of files
        if (index_of_filename_in_files_of_type +1) == num_of_files_of_type:
            # is the oldest file. return list of len 1
            return older_files
        # else if there aren't 9 older files
        elif (num_of_files_of_type-(index_of_filename_in_files_of_type+1)) < 9:
            # return every file older than passed file
            for i in range(index_of_filename_in_files_of_type+1, num_of_files_of_type):
                older_files.append(os.path.basename(files_of_type_in_filenames[i]))
            return older_files
        # else there exists more than 9 older files, only append the 9 most recent
        else:
            # index_of_filename_in_files_of_type+1 to get next oldest file
            # index_of_filename_in_files_of_type+10, range is noninclusive (appends 9 filenames)
            for i in range(index_of_filename_in_files_of_type+1, index_of_filename_in_files_of_type+10):
                older_files.append(os.path.basename(files_of_type_in_filenames[i]))
            return older_files

    ################################################################
    # Stat_Scraper member function: load_file
    ################################################################
    def load_file(self, filename):
        # if filename is not an error value
        if (filename != "Error: No File Loaded") & (filename != "ERROR"):
            return pd.read_csv(SAVE_PATH.save_path+"/"+filename)
        else:
            # filename is an error value, return an empty df (handled elsewhere)
            return pd.DataFrame()

    ################################################################
    # Stat_Scraper member function: load_files
    ################################################################
    def load_files(self, list_of_older_filenames):
        list_of_dfs = []
        # load the files and then append their dfs
        for filename in list_of_older_filenames:
            list_of_dfs.append(pd.DataFrame(self.load_file(str(filename))))
        return list_of_dfs
    
    ################################################################
    # Stat_Scraper member function: get_max_stats_last10
    ################################################################
    def get_min_and_max_stats_last10(self, dfs, type):
        # dfs is list of dfs to iterate through to find max stats
        # skip past the non-numeric data entries at beginning of save files
        if type == "EOM":
            start_index = 4
        if type == "career":
            start_index = 2
        if type == "loadout":
            start_index = 2

        # create min_df and max_df
        min_df = pd.DataFrame.copy(dfs[0])
        max_df = pd.DataFrame.copy(dfs[0])

        # iterate through each df
        for df in dfs:
            # iterate through each stat
            for i in range(start_index, len(df.columns)):
                # if value in df[column][0] < min_df[column][0]
                if df[df.columns[i]][0] < min_df[df.columns[i]][0]:
                    # set new max_stat to max_df
                    min_df[df.columns[i]] = df[df.columns[i]][0]
                # elif value in df[column][0] > max_df[column][0]
                elif df[df.columns[i]][0] > max_df[df.columns[i]][0]:
                    # set new max_stat to max_df
                    max_df[df.columns[i]] = df[df.columns[i]][0]
        
        return min_df, max_df
    
    ################################################################
    # Stat_Scraper member function: get_minmax_stats_alltime
    ################################################################
    def get_min_and_max_stats_alltime(self, type):
        # get all filenames of file type
        files_of_type = self.get_files_of_type(type)
        # load all files into dfs
        dfs = self.load_files(files_of_type)

        # skip past the non-numeric data entries at beginning of save files
        if type == "EOM":
            start_index = 4
        if type == "career":
            start_index = 2
        if type == "loadout":
            start_index = 2

        # create min_df and max_df
        min_df = pd.DataFrame.copy(dfs[0])
        max_df = pd.DataFrame.copy(dfs[0])

        # iterate through each df
        for df in dfs:
            # iterate through each stat
            for i in range(start_index, len(df.columns)):
                # if value in df[column][0] < min_df[column][0]
                if df[df.columns[i]][0] < min_df[df.columns[i]][0]:
                    # set new max_stat to max_df
                    min_df[df.columns[i]] = df[df.columns[i]][0]
                # elif value in df[column][0] > max_df[column][0]
                elif df[df.columns[i]][0] > max_df[df.columns[i]][0]:
                    # set new max_stat to max_df
                    max_df[df.columns[i]] = df[df.columns[i]][0]
        
        return min_df, max_df

    ################################################################
    # Stat_Scraper member function: minmax (normalization)
    ################################################################
    def minmax_normalize(self, min_df, max_df, x_df, type):
        # skip past the non-numeric data entries at beginning of save files
        if type == "EOM":
            start_index = 4
        if type == "career":
            start_index = 2
        if type == "loadout":
            start_index = 2

        # Create a minmax list to update
        minmax_list = []

        # iterate through each stat, note: min_df and max_df are same structure
        for i in range(start_index, len(min_df.columns)):
            # calculate minmax
            # minmax = (x - min) / (max - min)
            min = min_df.iloc[0,i]
            max = max_df.iloc[0,i]
            x = x_df.iloc[0,i]
            minmax = (x-min)/(max-min)
            # update minmax_df
            minmax_list.append(minmax)

        return minmax_list