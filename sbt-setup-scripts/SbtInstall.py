#This module download the SBT
import wget

def downloadSBT():
    url = 'https://dl.bintray.com/sbt/native-packages/sbt/0.13.13/sbt-0.13.13.tgz'
    try:
        print("downloading sbt")
        wget.download(url)
        print "File Download Complete"
    except:
        print "Unable to download SBT"