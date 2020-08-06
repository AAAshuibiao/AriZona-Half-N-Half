import loader
import processor
from actuator import smap


def setup():
    loader.pictures.load_square_map_images(smap)
    smap.load_image_vectors()


def predict():
    pass


def simple_predict():
    smap.simple_predictions = processor.trainer.predict(
        smap.image_vectors
    )


def run():
    setup()
    #predict()

    simple_predict()

    for i in range(64):
        print(smap.simple_predictions[i], end = ", ")
        if not (i+1) % 8: print()

    smap.print_color()
    