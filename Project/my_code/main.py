#Runs on windows 10, Python 3.8.5

def main():
    import os
    import sys

    sys.path.append(".")
    sys.path.append("..")

    from read_picture import read_picture

    try:
        train_image, train_label = read_picture.read_image_data('mnist_data\\train-images.idx3-ubyte', 'mnist_data\\train-labels.idx1-ubyte')
    except FileNotFoundError:
        try:
            train_image, train_label = read_picture.read_image_data('..\\mnist_data\\train-images.idx3-ubyte', '..\\mnist_data\\train-labels.idx1-ubyte')
        except FileNotFoundError as fe:
            print(fe)
            os.system("pause")
