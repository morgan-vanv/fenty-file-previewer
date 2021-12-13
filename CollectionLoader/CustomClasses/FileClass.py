# simple datatype to store Video information
import json
import os
import cv2

class FileClass:
    def __init__(self, file_name, directory_path):
        self.file_name = file_name
        self.directory_path = directory_path
        self.full_file_name = directory_path + '/' + file_name
        self.file_extension = self.file_name[self.file_name.rfind('.'):]
        self.file_size = os.path.getsize(self.full_file_name) / (1*(10**9))
        self.tags = []
        self.rating = 0

    def __eq__(self, other):
        if isinstance(other, FileClass):
            return self.file_name == other.file_name

    def __str__(self):
        output_dict = {
            "file_name": self.file_name,
            "directory_path": self.directory_path,
            "full_file_name": self.full_file_name,
            "file_extension:": self.file_extension,
            "file_size": self.file_size,
            "tags": self.tags,
            "rating": self.rating,
        }
        return str(output_dict)

    def returnas_dict(self):
        output_dict = {
            "file_name": self.file_name,
            "directory_path": self.directory_path,
            "full_file_name": self.full_file_name,
            "file_extension:": self.file_extension,
            "file_size": self.file_size,
            "tags": self.tags,
            "rating": self.rating,
        }
        return output_dict
        
    def printandreturn_asJSON(self):
        self.set_lists_as_string()
        temp = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)
        print(temp)
        return temp
