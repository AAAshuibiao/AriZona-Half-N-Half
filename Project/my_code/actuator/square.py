from PIL import Image

class Square(object):
    def __init__(self, ID):
        self.ID = ID
        self.is_edge = True

        self.image_data = None
        
        self.simple_prediction = None

        self.color = None
