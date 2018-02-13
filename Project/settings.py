import os

# gets the directory path to this file
dir_path = os.path.dirname(os.path.realpath(__file__))

def write_settings(setting_pack):
    """writes setting to file"""
    # gets the directory path to this file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #opens file and writes setting_pack
    f = open(dir_path+"/"+"settings1.csv","w")
    f.write(str(setting_pack))
    f.close()

def read_settings():
    """reads the settings from file"""

    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path+"/"+"settings1.csv","r")
    data = f.readline()
    f.close()
    return data

