import CreatePlayFolders
import SbtInstall
import os

dir_name=raw_input("Enter the directory to be created : ")
#print os.listdir(dir_name)
print os.getcwd()
app_name = []
def readPlayApps():
    playapps = open('PlayApps','r')
    for appname in playapps:
        print appname
        app_name.append(appname)
    playapps.close()

def initializeApp():
    for i in len(app_name):
        #Go to path
        readPlayApps()
        CreatePlayFolders.checkDirectory(app_name[i])
        SbtInstall.downloadSBT()
        #Back to Base

CreatePlayFolders.directoryStatus(dir_name)