import functools


def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)


class Animal:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def breath(self):
        print("Breathing")


class Dog(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)


dog = Dog(name="Buddy", color="Brown")
print(dog.name)
print(dog.color)
print(dog.breath())
