class fruits:
    def __init__(self, type, color, price, shape):
        self.fruittype = type
        self.fruitcolor = color
        self.fruitprice = price
        self.fruitshape = shape

    def display(self):
      print(self.fruittype, self.fruitcolor, self.fruitprice, self.fruitshape)


myobj = fruits("Banana", "Green", 20, "Rectangle")
myobj.display()
myobj2 = fruits("Mango", "Yellow", 40 , "Oval")
myobj2.display()
myobj3 =fruits("Avocado", "Grey", 30, "Circle")
myobj3.display()