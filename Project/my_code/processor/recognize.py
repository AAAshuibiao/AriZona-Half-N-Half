import loader
import processor
from actuator import smap


def setup():
    loader.pictures.load_square_map_images(smap)
    smap.load_image_vectors()
    processor.train.run()



def predict():
    pass


def simple_predict():
    smap.simple_predictions = list(processor.trainer.predict(
        smap.image_vectors
    ))



#THIS IS ONLY USED FOR P3 TESTING

# def load_from_image_list():
#     ag = loader.autoGrader

#     c = 0

#     for y in range(1, 9):
#         for x in range(1, 9):
#             smap.map[(x, y)].color, smap.map[(x, y)].number = ag.image_list[c]
#             c += 1


def run():
    setup()
    #predict()


    simple_predict()
    
    #loader.autoGrader.random_image(3, 3)

    #oad_from_image_list()

    smap_debug = smap

    smap.correct_and_load_simple_predictions()

    smap._debug_print_map()
