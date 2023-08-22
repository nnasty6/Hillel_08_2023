from itertools import zip_longest
from pprint import pprint as print


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __rerp__(self):
        return f"{self.name} representation"

    def __str__(self) -> str:
        return f"The string representation of {self.name}"

    def another(self):
        return "from another"


john = Person(name="John")

# print("John")
# print(repr("John "))
# print(john.__str__())
# print(john)
# print(str("asdasd"))

# john_has_name, john_has_surname, john_has_age, john_has_city = ()
john_contact_info_existence = (
    True,
    True,
    False,
    False,
)

# print(john_contact_info_existence)

# if not all(john_contact_info_existence):
#     print("Some fields do not exist")

# if any(john_contact_info_existence):
#     print("At least one field does exist")

# for item in john_contact_info_existence:
#     if item is False:
#         print("Some fields do not exist")
#         break

# team = ["John", "Marry", "Jach", "Rosa", "Mark"]
# print(sorted(team))
# print(sorted(team, reverse=True))
# print(ord("J"))
# print(ord("j"))
# print(chr(74))

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 30, "number": 3},
    {"name": "Cavin", "age": 12, "number": 18},
]
# def by_age(item: dict):
#     return item["age"]

# print(sorted(team, key=lambda item: item["age"]))
# print(id(team))


class Animal:
    pass


class Dog(Animal):
    pass


spike = Dog()

# print(isinstance(spike, Animal)) #проверяет полное дерево подклассов
# print(type(spike) == Animal)

john = "Jphn"
marry = "Marry"

# print(john is marry)
# print(id(john) == id(marry))
# print(isinstance(marry, str))
# print(type(marry) == str)
# print(hash("name"))
# print(hash("name"))
# print(hash("name"))


def foo():
    """Some documentation"""
    pass


# print(help(foo))

names = ["John", "Marry", "Jack"]
ages = [20, 30, 40, 60]

# for index, name in enumerate(names):
#     print(f"{name=}, age={ages[index]}")

for name, age in zip(names, ages):
    print(f"{name=}, {age=}")

for name, age in zip_longest(names, ages):
    print(f"{name=}, {age=}")
