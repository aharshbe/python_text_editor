#!/usr/local/bin/python3
from time import sleep

def checkType(filename):
    if ".py" in filename:
        print("Creating Python file...")
        sleep(.4)
        return '# '
    if ".sh" in filename:
        print("Creating Bash file...")
        sleep(.4)
        print("bash")
        return '# '
    if ".c" in filename:
        print("Creating C file...")
        sleep(.4)
        return '// '
