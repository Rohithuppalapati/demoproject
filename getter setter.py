class Student():
    def __int__(self,name,age):
        self.__name=name
        self.__age=age

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def display(self):
        print('name is ',self.getName())
        print('age is ',self.getAge())


obj1=Student()

obj1.setName('Rohith')
obj1.setAge(24)

obj1.display()

obj2=Student()

obj2.setName('Sanjay')
obj2.setAge(34)

obj2.display()