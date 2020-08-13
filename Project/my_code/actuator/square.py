from PIL import Image

class Square(object):
    def __init__(self, ID):
        self.ID = ID
        self.poz = "this is not implemented yet"
        
        self.number = None
        self.color = None
        self.is_edge = True

        #self.image = Image()

        self.image_data = None

        self.moves = None

        self.psargs = {"moves" : None, "is_known" : False}
