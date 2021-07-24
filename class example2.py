# Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.
# 2. setAge - It should assign age to student
# 3. setMarks - It should assign marks to the student.

class Student():
    def __init__(self,name,roll_no,marks,age):
        self.name=name
        self.roll_no=roll_no
        self._marks=marks
        self._age=age

    def SetAge(self,age):
        self.age=age

    def SetMarks(self,marks):
        self.marks=marks

    def Display(self):
        print(f'name is : {self.name}')
        print(f'roll no is : {self.roll_no}')
        print(f'marks are : {self.marks}')
        print(f'age is : {self.age}')

s1=Student('rohit',10,94,16)
s2=Student('ram',20,86,14)

s1.SetAge(25)
s1.SetMarks(94)

s2.SetAge(21)
s2.SetMarks(88)

s1.Display()
print()
s2.Display()


