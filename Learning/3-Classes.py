from abc import ABC, abstractmethod
from collections import namedtuple

# In python, we rarely use "Field" instead we use "Attribute"
# Attribute is a variable or a method that belongs to an object


class Point:
    default_color = "red"  # Class Arttribute
    __name = "Point"  # Private Class Attribute

    # notice that in Python, unlike other languages,
    # we don't have the concept of "private" or "protected" attributes
    # we just use a convention of prefixing the attribute with an underscore
    # to indicate that it is private but we can still access it from outside the class
    # like this: Point._Point__name

    def __init__(self, x, y):  # Constructor Method

        self.x = x  # Instance Attribute
        self.y = y

    @classmethod
    def zero(cls):  # Class Method
        return cls(0, 0)

    def draw(self):  # Instance Method
        print(f"Drawing point at ({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# "rszalski.github.io/magicmethods/" for more information on magic methods


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter  # if you don't write a setter, the attribute will be read only!
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


class Animal:
    def __init__(self):
        self.age = 1


class Dog(Animal):  # Inheritance
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.weight = 10

# we can also inherit from multiple classes and separate them with a comma


# we cannot instantiate an abstract class
class Stream(ABC):
    def __init__(self):
        self.opened = False

    @abstractmethod  # this method must be implemented in the child class,
    # otherrwise it will raise an error and the class will be abstract
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")
        # implementation of the read method


# namedtuple is a class that is used to create immutable objects
Point = namedtuple("Point", ["x", "y"])  # Named Tuple
p1 = Point(x=1, y=2)
