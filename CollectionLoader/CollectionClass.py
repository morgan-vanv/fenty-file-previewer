import CustomClasses
import json
import os
import csv
import pandas as pd
import requests

#   DOC:
#       ContentCollection
#           - init
#               pass directory string to create collection manager object
#           - load_collection()
#               loads files from directory, gathering file_count, storage_used, etc.
#           - print_filecollection()
#               simple print statement, outputting all file objects
#           
#

#   TODO:
#
#
#
#
#

# class to manage content collection in a given directory
class CollectionClass:
    def __init__(self, directory_name):
        self.directory_name = directory_name
        self.file_list_string = []
        self.file_list_objects = []
        self.file_dataframe_rows = []
        self.file_dataframe = []
        self.file_count = 0
        self.storage_used = 0

    # LOADS COLLECTION
    def load_collection(self):
        # In one pass through a target directory...
        # Create list of file objects
        # Gather the following information: file_count, storage_used, etc.

        for file in os.listdir(self.directory_name):
            print("      Loading File: " + str(file) + " ...")
            full_filepath = str(self.directory_name) + "/" + str(file)
            self.file_count += 1                           # Adding to scene count
            self.storage_used += (os.path.getsize(full_filepath)) / (1*(10**9)) # Adding to storage used
            self.file_list_string.append(file)             # Adding to STRING FILE list
            self.file_list_objects.append(CustomClasses.FileClass(file, self.directory_name)) #OBJECT FILE LIST
            self.file_dataframe_rows.append(CustomClasses.FileClass(file, self.directory_name).returnas_dict())
        self.file_dataframe = pd.DataFrame.from_records(self.file_dataframe_rows)
        
        print("\n")
        print("File Count: " + str(self.file_count))
        print("File List (string): " + str(self.file_list_string))
        print("Storage Used: " + str(self.storage_used)[:5] + " GB")

        print("\nDATAFRAME:")
        print(self.file_dataframe)
        pass

    #  PRINTS ALL FILES IN COLLECTION
    def print_filecollection(self):
        print("\FILE OBJECTS IN COLLECTION: \n")
        for file in self.file_list_objects:
            print(file)
            


# FILE CAN BE RAN AS SCRIPT, IF SO, DO THE FOLLOWING
if __name__ == '__main__':
    print("Ran as Script()")
    temp_directory = './CollectionLoader/testing_directory/'
    collection = CollectionClass(temp_directory)
    collection.load_collection()

