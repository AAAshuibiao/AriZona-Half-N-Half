class Square(object):
    def __init__(self, id):
        self.id = id
        self.png = None
    
    def __repr__(self):
        return str(self.id)
