class Addition():
    def sum(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            s=a+b+c
        elif (a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s


add1=Addition()

result=add1.sum(10,40)

print(result)
