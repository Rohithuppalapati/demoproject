def highest_even(values):
    for i in values:
        if(int(i) % 2 == 0):
            print('even')
        else:
            print('odd')

print(highest_even([1,2,3,4,5]))