class Student():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        a1=self.m1 + other.m1
        a2=self.m2 + other.m2
        s3=Student(a1,a2)
        return s3

S1=Student(50,60)
S2=Student(60,70)

S3=S1 + S2

print(S3.m1,S3.m2)
