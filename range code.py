class Mygen():
    current=0
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def __iter__(self):
        return self

    def __next__(self):
        if Mygen.current<self.last:
            num=Mygen.current
            Mygen.current = Mygen.current + 1
            return num
        raise StopIteration

value=Mygen(0,100)
for i in value:
    print(i)


