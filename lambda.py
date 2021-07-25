#square
my_list=[3,9,6]

#list sorting
a=[(-1,10),(0,2),(4,3),(9,9)]

print(list(map(lambda item:item**2,my_list)))

a.sort(key=lambda x:x[1])
print(a)
a.sort(key=lambda y:y[0])
print(a)
