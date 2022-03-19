class Dog():
    species = "mammal"
    def __init__(self,breed,name,spots):
        #Attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = "lab", name = "sammy", spots = False)

print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)





