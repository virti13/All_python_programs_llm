# Parent class
class Bird:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


# Child class
class Penguin(Bird):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def show_info(self):
        super().show()
        print("Color:", self.color)


# Create object
p = Penguin("Pingu", "Black and White")

p.show_info()