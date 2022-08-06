# class
class Dog():
    """Represent a dog."""

    def __init__(self, name):
        """Inittialize dog object"""
        self.name = name

    def sit(self):
        print(self.name + ' is sitting')

# my_dog = Dog('Peso')
# print(my_dog.name)
# my_dog.sit()


class SARdog(Dog):
    def __init__(self, name):
        super().__init__(name)

    def search(self):
        print(self.name + ' is searching')


my_dog = SARdog('willie')
my_dog.sit()
my_dog.search()
