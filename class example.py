class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1=Cat('linde',36)
cat2=Cat('sun',25)
cat3=Cat('kitty',14)


def oldest_cat(*args):
    return max(args)


print(f'oldet cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')
