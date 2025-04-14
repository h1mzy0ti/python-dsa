class car:
    def __init__(self,model,year,manufacturer):
        self.year = year
        self.__model = model
        self.manufacturer = manufacturer

    def getmodel(self):
        return self.__model

class suv(car):
    def specification(self):
        self.specs = "20"
        return self.specs


car = car("BD",2025,"BYD")


print(car.getmodel())

car2 = suv(2023,"BH","Hammar")

print(car2.specification())