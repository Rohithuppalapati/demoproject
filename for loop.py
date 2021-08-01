def for_code(iterable):
    iterator=iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

for_code([1,2,3])
