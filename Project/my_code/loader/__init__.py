from . import modules
from . import pictures

autoGrader = modules.auto_grader()

imageList, labelList = pictures.load_mnist()
