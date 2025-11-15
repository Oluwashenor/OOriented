# Object Oriented Programming


class Dog:
    def __init__(self, name):
        self.name = name
        print(name)

    def get_name(self):
        return self.name

    def bark(self):
        print("Bark")

# d = Dog("Sample")
# print(d.name)
