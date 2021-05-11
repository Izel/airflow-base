import argparse
import shutil 
import os.path
import urllib

url = 'https://viaegnatia20.blob.core.windows.net/egnatia20/tst.csv'


def copyFile():
    original = '/tmp/data/tst.csv'
    target = '/tmp/data/tst1.csv'
    target2 = '/tmp/data/tst2.csv'

    exists(original)
    shutil.copy(original, target)
    shutil.copy(original, target2)



#If the required file does not exist download it, else print that it exists
def exists(path):
    if os.path.isfile(path):
        print ("File exist")
    else:
        urllib.urlretrieve(url, filename=path)



copyFile()
