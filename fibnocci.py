def fib(number):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(number):
        c=a+b
        print(c)
        a=b
        b=c
    return 'done'
c=fib(10)
print(c)



