import loader

import processor

from processor import cfg
from processor import Trainer


def setup():
    lower_bounds, upper_bounds = cfg["Training-data-set-portion"].split("-")

    data = loader.imageList[lower_bounds, upper_bounds]
    labels = loader.labelList[lower_bounds, upper_bounds]

    toler = cfg["tolerance"]

    step_w = cfg["step_w"]
    step_b = cfg["step_b"]

    processor.trainer = Trainer(data, labels, toler, step_w, step_b)


def learn():
    processor.trainer.train_learn()


def run():
    setup()
    learn()
