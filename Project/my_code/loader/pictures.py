import loader.modules as modules

def load_pictures():
    path = ".\\"
    while True:
        try:
            train_image, train_label = modules.read_picture.read_image_data(path + 'mnist_data\\train-images.idx3-ubyte', path + 'mnist_data\\train-labels.idx1-ubyte')
            break
        except FileNotFoundError as pathError:
            print(pathError)
            print("please input the correct path:")
            path = input()
    
    return train_image, train_label
