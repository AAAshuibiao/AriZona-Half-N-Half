import numpy as np

import loader
import processor

from processor import config as cfg
from processor import Trainer

import time
import threading
tKill = False


def print_loading_bar():
    global tKill
    print("training: starting")
    print("training: 0%")
    for i in range(1, 10):
        if tKill: break
        print("training: " + str(i) +"0%")
        time.sleep(10)
    print("training: 99%")
    return 0


def data_reshape(data):
    return np.reshape(data, (len(data), 784))

def setup():
    lower_bounds, upper_bounds = cfg["Training-data-set-portion"].split("-")

    lower_bounds = int(lower_bounds)
    upper_bounds = int(upper_bounds)

    data = loader.imageList[lower_bounds : upper_bounds]
    labels = loader.labelList[lower_bounds : upper_bounds]

    if not cfg["Use-custom-trainer"]:
        data = data_reshape( loader.imageList[lower_bounds : upper_bounds] )

    toler = cfg["tolerance"]

    step_w = cfg["step_w"]
    step_b = cfg["step_b"]

    processor.trainer = Trainer(data, labels, toler, step_w, step_b)


def learn():
    try:
        processor.trainer.run()
    except AttributeError:
        processor.trainer.train_learn()


def run():
    global tKill
    t = threading.Thread(target=print_loading_bar)
    t.start()
    setup()
    learn()
    tKill = True
