import loader
import loader.modules as modules

from actuator.square_map import edgeless, traverse


class Image_data(object):
    def __init__(self, ID):
        self.ID = ID
        self.file = None
        self.rgb = None
        self.greyscale = None
        self.load_file().load_rgb().load_greyscale().get_color()
        self.color = None

    def load_file(self):
        image_path = loader.path + "\\auto_grader\\image\\" + str(self.ID) + ".png"
        self.file = modules.Image.open(image_path)
        return self

    def load_rgb(self):
        self.rgb = self.file.convert("RGB").load()
        return self

    def load_greyscale(self):
        self.greyscale = self.file.convert("L").load()
        return self

    def get_color(self):
        self.color = "R"
        return self

    @classmethod
    def ID_counter(self):
        try:
            self.count += 1
        except AttributeError:
            self.count = 0
        return self.count


@edgeless
@traverse
def load_square_map_images(self, x = None, y = None):
    self.map[(x, y)].image = Image_data( Image_data.ID_counter() )


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
