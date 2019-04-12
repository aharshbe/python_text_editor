#!/usr/local/bin/python3
from time import sleep
from subprocess import call

def checkType(filename):
    if ".py" in filename:
        print("Creating Python file...")
        return '# '
    if ".sh" in filename:
        print("Creating Bash file...")
        return '# '
    if ".c" in filename:
        print("Creating C file...")
        return '// '

def compileType(filename):
    if ".py" in filename:
        print("Running Python file...")
        sleep(.2)
        exec(open(filename).read())
        options = ['Y', 'y', 'n','N']
        while (1):
            choice = input("Done viewing? (y/n): ")
            if (choice in options):
                if (choice == 'y' or choice == 'Y'):
                    break
                else:
                    continue
    if ".sh" in filename:
        print("Running Bash file...")
        sleep(.2)
        s = "./{}".format(filename)
        e = "chmod u+x ./{}".format(filename)
        call(e, shell=True)
        call(s, shell=True)
        options = ['Y', 'y', 'n','N']
        while (1):
            choice = input("Done viewing? (y/n): ")
            if (choice in options):
                if (choice == 'y' or choice == 'Y'):
                    break
                else:
                    continue
    if ".c" in filename:
        print("Compiling C file...")
        sleep(.2)
        output = filename.split('.')[0]
        s = "./{}".format(output)
        e = "gcc ./{} -o {}".format(filename, output)
        call(e, shell=True)
        call(s, shell=True)
        options = ['Y', 'y', 'n','N']
        while (1):
            choice = input("Done viewing? (y/n): ")
            if (choice in options):
                if (choice == 'y' or choice == 'Y'):
                    break
                else:
                    continue
