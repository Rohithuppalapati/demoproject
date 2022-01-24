class Students():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.school=self.School()

    def details(self):
        print('Name is ',self.name)
        print('rollno is ',self.roll)
        self.school.show()

    class School():
        def __init__(self):
            self.schname='Nalanda'
            self.schcity='VIZ'

        def show(self):
            print('school name is ',self.schname)
            print('schcity is ',self.schcity)


S1=Students('Ramesh',47)
S2=Students('Hardik',29)

S1.details()
print('************')
S2.details()


