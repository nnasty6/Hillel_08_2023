class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def get_name(self):
        print(f"Name is {self.name}")

    def __str__(self) -> str:
        return f"this is {self.name}. He is {self.age}"

    def __repr__(self) -> str:
        return f"name={self.name}, age={self.age}"


team = [
    {"name": "John", "age": 12},
    {"name": "Marry", "age": 22},
]
# print(team[0]["name"])

# if not team[1].get("name"):
#     print(f"No name in {team[1]}")
# else:
#     print(team[1]["name"])

# john = Person(name="John", age=12)
john = Person(name="John", age=12)
print(john.__dict__)
# john.name = "John"
# john.age = 12
marry = Person(name="Marry", age=22)

john.get_name()
marry.get_name()
print(john)
# print(john.name)
