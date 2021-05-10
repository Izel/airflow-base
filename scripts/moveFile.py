import argparse
import shutil 

def moveFile():
    ap = argparse.ArgumentParser()
	

    ap.add_argument("-o", "--output",
					default='',
					help="path to output file")
    ap.add_argument("-i", "--input",
					default='',
					help="path to output file")
    args = vars(ap.parse_args())
    input = [args["input"]]
    output = [args["output"]]
    print(input[0])
    shutil.copy(str(input[0]), str(output[0]))

moveFile()