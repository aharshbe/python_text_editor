#!/usr/local/bin/python3
from time import sleep
from subprocess import call

def checkType(filename):
    if ".py" in filename:
        print("Creating Python file...")
        return '# '
    elif ".sh" in filename:
        print("Creating Bash file...")
        return '# '
    elif ".c" in filename:
        print("Creating C file...")
        return '// '
    elif ".gitignore" in filename:
        return '# '
    else:
        return ''

def compileType(filename):
    if ".py" in filename:
        print("Running Python file...")
        sleep(.2)
        exec(open(filename).read())
        print("<< END OF FILE >>")
        options = ['Y', 'y', 'n','N']
        while (1):
            choice = input("Done viewing? (y/n): ")
            if (choice in options):
                if (choice == 'y' or choice == 'Y'):
                    break
                else:
                    continue
    elif ".sh" in filename:
        print("Running Bash file...")
        sleep(.2)
        s = "./{}".format(filename)
        e = "chmod u+x ./{}".format(filename)
        call(e, shell=True)
        call(s, shell=True)
        print("<< END OF FILE >>")
        options = ['Y', 'y', 'n','N']
        while (1):
            choice = input("Done viewing? (y/n): ")
            if (choice in options):
                if (choice == 'y' or choice == 'Y'):
                    break
                else:
                    continue
    elif ".c" in filename:
        print("Compiling C file...")
        sleep(.2)
        output = filename.split('.')[0]
        s = "./{}".format(output)
        e = "gcc ./{} -o {}".format(filename, output)
        call(e, shell=True)
        call(s, shell=True)
        print("<< END OF FILE >>")
        options = ['Y', 'y', 'n','N']
        while (1):
            choice = input("Done viewing? (y/n): ")
            if (choice in options):
                if (choice == 'y' or choice == 'Y'):
                    break
                else:
                    continue
    else:
        print("Not sure of this file extension and so can't run it.")
