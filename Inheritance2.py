class Vehicles:
    def __init__(self,model,cost,color):
        self.model=model
        self.cost = cost
        self.color = color

    def cars(self):
        print(self.model,self.cost,self.color)
class Toyota(Vehicles):
    pass
toyota = Toyota("Camri", "3.5million","Grey")
toyota.cars()

class Suzuki(Vehicles):
    pass
suzuki = Suzuki("Alto", "1.2million","Navy blue")
suzuki.cars()

class Mazda(Vehicles):
    pass
mazda = Mazda("CX-9","4.8million","White")
mazda.cars()







