def swap(func):

    def wrapper(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrapper

@swap
def div(a,b):
    return a/b
@swap
def sub(a,b):
    return a-b

result=div(5,2)
result1=sub(1,3)

print(result,result1)
