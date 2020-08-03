import os
import sys


path = ".."


def askForCorrectPath():
    global path
    print( "please input the correct path for Project folder(\"官方营算法\" folder):" )
    path = input()


try:
    assert os.getcwd().split('\\')[-1] == "my_code"
    sys.path.append(path)
except AssertionError:
    print( "cwd not under \"my_code\", as cwd = " + os.getcwd() )
    askForCorrectPath()
    sys.path.append(path)


from read_picture.read_picture import read_image_data
