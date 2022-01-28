class Parent():
    def __init__(self,house):
        self.house=house

    def parentasseet(self):
        print('Parent Assets are ',self.house)

class Son(Parent):

    def __init__(self,house,car):
        self.car=car
        super().__init__(house)

    def sonasseet(self):
        print(f'Son Assets are {self.house} and {self.car} ')

class Grandson(Son):
    def __init__(self,bike,house,car):
        self.bike=bike
        super().__init__(house,car)

    def grandsonasset(self):
        print(f'Grandson assets are \n House: {self.house}\n Bike: {self.bike}\n Car: {self.car}\n')


s1=Grandson('Ducati','3floors','Hyundai')

s1.grandsonasset()


