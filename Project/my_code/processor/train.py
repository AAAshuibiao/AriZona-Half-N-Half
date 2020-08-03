import loader

from processor import cfg
from processor import Trainer

def train():
    data = loader.imageList
    labels = loader.labelList

    

    trainer = Trainer(data, labels, toler, step_w, step_b)
