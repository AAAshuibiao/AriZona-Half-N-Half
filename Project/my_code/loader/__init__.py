path = ".."

import sys

from . import modules
from . import pictures


stdout = sys.stdout

print("loading: auto_grader", file = stdout)
autoGrader = modules.auto_grader()

print("loading: mnist images and lables", file = stdout)
imageList, labelList = pictures.load_mnist()
