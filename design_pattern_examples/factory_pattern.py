__author__ = 'MAK'


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("vough")


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("meau")


def get_pet(name, pet='dog'):

    pets = dict(dog=Dog(name=name),
                cat=Cat(name=name))

    return pets[pet]


if __name__ == '__main__':
    get_pet(name='Milo').speak()
    get_pet(name='Tom', pet='cat').speak()


