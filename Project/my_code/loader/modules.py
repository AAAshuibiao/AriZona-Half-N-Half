import os
import sys

import loader



def askForCorrectPath():
    print( "please input the correct path for Project folder(\"官方营算法\" folder):" )
    loader.path = input()


try:
    assert os.getcwd().split('\\')[-1] == "my_code"
    sys.path.append(loader.path)
    sys.path.append(loader.path + "\\auto_grader")

except AssertionError:
    print( "cwd not under \"my_code\", as cwd = " + os.getcwd() )
    askForCorrectPath()
    sys.path.append(loader.path)


from auto_grader import auto_grader
from read_picture import read_image_data
from simple_train import simple_train
