from read_picture import read_picture

train_image, train_label = read_picture.read_image_data('mnist_data\\train-images.idx3-ubyte', 'mnist_data\\train-labels.idx1-ubyte')

print(train_image[0])
print(len(train_image[0]))
print(len(train_image[0][0]))
