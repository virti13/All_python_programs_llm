class String:

    def __init__(self, text):
        self.__text = text   # private variable

    def reverse(self):
        return self.__text[::-1]


# Create object
s = String("Hello")

print("Original String:", "Hello")
print("Reversed String:", s.reverse())