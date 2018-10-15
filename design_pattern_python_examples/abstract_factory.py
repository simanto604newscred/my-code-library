__author__ = 'MAK'


class Dog:

    def __init__(self, name=None):
        self.name = name

    def speak(self):
        return "vough"

    def __str__(self):
        return "Dog"


class Cat:

    def __init__(self, name=None):
        self.name = name

    def speak(self):
        return "meau"

    def __str__(self):
        return "Cat"


class DogFactory:
    """ Concrete Factory """

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns Dog Food object"""
        return "Dog food"


class CatFactory:
    """ Concrete Factory """

    def get_pet(self):
        """Returns a Cat object"""
        return Cat()

    def get_food(self):
        """Returns Cat Food object"""
        return "Cat food"


class PetStore:

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory """

        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the DogFactory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Our pet says '{}'!".format(pet.speak()))
        print("Our pet food is '{}'!".format(pet_food))


if __name__ == '__main__':

    # create a concreate Factory
    factory = DogFactory()

    # create a pet store housing our Abstract Factory
    shop = PetStore(pet_factory=factory)

    # invoke the utility mehtod to show the details of our pet
    shop.show_pet()
