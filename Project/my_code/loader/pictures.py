import loader
import loader.modules as modules

import actuator


class Image(object):
    def __init__(self, ID):
        self.ID = ID
        self.file = None
        self.rgb = None
        self.greyscale = None
        self.load_file().load_rgb().load_greyscale().get_color()
        self.color = None
        self.number = None

    def load_file(self):
        image_path = loader.path + "\\auto_grader\\images\\" + str(self.ID) + ".png"
        self.file = modules.Image.open(image_path)
        return self

    def load_rgb(self):
        self.rgb = self.file.convert("RGB").load()

    def load_greyscale(self):
        self.greyscale = self.file.convert("L").load()

    def get_color(self):
        self.color = "R"


def load_square_map():
    smap = actuator.smap
    for i in range( smap.size[0] * smap.size[1] ):
        print(i)


def load_mnist():
    while True:
        try:
            train_image, train_label = modules.read_image_data(
                loader.path + '\\mnist_data\\train-images.idx3-ubyte',
                loader.path + '\\mnist_data\\train-labels.idx1-ubyte'
            )
            break
        except FileNotFoundError as pathError:
            print(pathError)
            modules.askForCorrectPath()
    
    return train_image, train_label
