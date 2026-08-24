# create class
class Dog:

    # class attribute
    species = "animal"

    # instance attributes
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# instantiate the Dog class
tommy = Dog("Tommy", "Labrador")
bruno = Dog("Bruno", "German Shepherd")


# access the class attribute
print("Tommy is an {}".format(tommy.species))
print("Bruno is also an {}".format(bruno.species))


# access the instance attributes
print("{} is a {}".format(tommy.name, tommy.breed))
print("{} is a {}".format(bruno.name, bruno.breed))