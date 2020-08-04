import json

import loader
import loader.modules as modules

from loader import stdout

from . import custom_train


print("loading: trainer", file = stdout)
cfg = config = json.loads(
    open( loader.path + "\\my_code\\configs.json" ).read()
)

if cfg["Use-custom-trainer"]:
    Trainer = custom_train.My_train
else:
    Trainer = modules.simple_train.simple_train_one_num

trainer = None


print("running: training", file = stdout)
from . import train
train.run()


print("running: recognizing", file = stdout)
from . import recognize
recognize.run()
