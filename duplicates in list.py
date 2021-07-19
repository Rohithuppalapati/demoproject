array=['a','a','b','c','d','e','e']

duplicates=[]
for val in array :
    if array.count(val) > 1:
        if val not in duplicates:
            duplicates.append(val)

print(duplicates)