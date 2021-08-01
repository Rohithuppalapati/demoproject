def fib(num):
    if num<0:
        print('enter +ve num')
    elif num==0:
        print(0)
    elif num==1:
        print(1)
    else:
        a=0
        b=1
        for i in range(num):
            yield a
            temp=a
            a=b
            b=temp+b

for s in fib(20):
    print(s)
