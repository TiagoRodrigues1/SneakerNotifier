class SneakerInfo:
    def __str__(self):
        return 'Sneaker -> ' + self.name + " with price -> " + self.price + " will be launched " + str(self.releaseDate)
 
    def __init__(self, name, img, price, releaseDate):
        self.name = name
        self.img = img
        self.price = price
        self.releaseDate = releaseDate