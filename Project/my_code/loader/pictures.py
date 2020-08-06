import loader
import loader.modules as modules

from actuator.square_map import edgeless, traverse


class Image_data(object):
    def __init__(self, ID):
        self.ID = ID
        self.im = None
        self.rgb = None
        self.greyscale = None
        self.color = None
        self.load_file().load_rgb().load_greyscale()

    def load_file(self):
        image_path = loader.path + "\\auto_grader\\image\\" + str(self.ID) + ".png"
        self.im = modules.Image.open(image_path)
        return self

    def load_rgb(self):
        self.rgb = self.im.convert("RGB").load()
        return self

    def load_greyscale(self):
        color_counts = {
            0: sum(self.im.getdata(0)), #case 0: red
            1: sum(self.im.getdata(1)), #case 1: green
            2: sum(self.im.getdata(2))  #case 2: blue
        }
        for color in [0, 1, 2]:
            if max(color_counts.values()) == color_counts[color]:
                self.color = color
                self.greyscale = self.im.getdata(color)
                self.greyscale = list(self.greyscale)
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
    self.map[(x, y)].image_data = Image_data( Image_data.ID_counter() )
    self.map[(x, y)].color = ['R', 'G', 'B'][self.map[(x, y)].image_data.color]


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
