def inc_range(*args):
    num_args=len(args)
    start=0
    step=1

    if (num_args)<1:
        raise TypeError (f'expected atleast 1 argument but got {num_args}')
    elif (num_args)==1:
        stop=args[0]
    elif (num_args)==2:
        (start,stop)=args
    elif (num_args)==3:
        (start,stop,step)=args
    else:
        raise TypeError(f'expected atmost 3 args but got {num_args}')

    i=start
    while i<=stop:
        yield i
        i=i+step

for s in inc_range(40):
    print(s)
