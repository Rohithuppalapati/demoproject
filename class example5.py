class pythoncoaching():

    # class method or static method

    @staticmethod
    def boardread():
        print('All please look at the board')

    # class variable

    Board = 'Black Board'

    # instance menthods

    def writing(self, name):
        print('i am writing : ',name)

    def listen(self, name):
        print('i am listening : ',name)

    def understand(self, percentage):
        print('i am able to understand : ',percentage)


# creating objects to invoke instance methods

a = pythoncoaching()
b = pythoncoaching()

# instance variables

a.pen = 'parker'
b.pen = 'bitco'
a.book = 'classmate'
b.book = 'ITC'

# invoking instance methods

a.writing(a.pen)
a.listen('rohith')
a.understand('80%')

print()

b.writing(b.pen)
b.listen('ramu')
b.understand('50%')

# invoking class method

print()
pythoncoaching.boardread()

# invoking class variable

print(pythoncoaching.Board)




