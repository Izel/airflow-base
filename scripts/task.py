import argparse
import shutil 

def copyFile():
    original = '/usr/local/airflow/tst.csv'
    target = '/tmp/tst.csv'
    target2 = '/tmp/tst2.csv'

    shutil.copy(original, target)
    shutil.copy(original, target2)




copyFile()
#moveFile()
