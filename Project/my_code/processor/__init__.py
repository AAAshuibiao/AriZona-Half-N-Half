import json

import loader
import loader.modules as modules

from . import custom_train
from . import train


cfg = json.loads(
    open( loader.path + "\\my_code\\configs.json" ).read()
)


if cfg["Use-costom-trainer"]:
    Trainer = custom_train.My_train
else:
    Trainer = modules.simple_train.simple_train_one_num


trainer = None


train.run()
