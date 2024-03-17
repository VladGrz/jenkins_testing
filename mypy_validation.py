"""This module provides class Person"""

class Person:
    """Class for person"""
    def __init__(self, name: str|None=None, age: int|None=None) -> None:
        """Method that sets default values or sets velues provided during object creation
        :params name: Name of the person
        :params age: Age of the person
        """
        self.name = name
        self.age = age

    def change_age(self, age: int) -> None:
        """Method to change the age of the person

        :params age: Age to set
        """
        self.age = age

    def change_name(self, name: str) -> None:
        """Method to change the name of the person

        :params name: Name to set
        """
        self.name = name

dave = Person("Dave", 15)
angel = Person()

print(dave.name)
print(angel.name)
