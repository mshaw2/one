#This module creates directory Structure
import os
def directoryStatus(dir_name):
    try:
        os.path.dirname(dir_name)
        print "Directory Already Exists"
    except:
        print "Creating New Directory"
        os.mkdir(dir_name)

