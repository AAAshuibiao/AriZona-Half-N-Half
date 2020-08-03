import loader
import loader.modules as modules

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
