import loader.modules as modules

def load_pictures():
    while True:
        try:
            train_image, train_label = modules.read_image_data(
                    modules.path + '\\mnist_data\\train-images.idx3-ubyte', modules.path + '\\mnist_data\\train-labels.idx1-ubyte'
                )
            break
        except FileNotFoundError as pathError:
            print(pathError)
            modules.askForCorrectPath()
    
    return train_image, train_label