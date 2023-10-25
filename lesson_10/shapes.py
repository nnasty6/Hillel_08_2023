from inspect import signature
from math import pi
from typing import Protocol


class CanCalculateArea(Protocol):
    def calculate_area(self) -> float:
        ...

    def foo():
        pass


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius: int = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2


class Square:
    def __init__(self, side: int) -> None:
        self.side: int = side

    def calculate_area(self) -> float:
        return self.side**2


class Diamond:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b


def calculate_area(self) -> float:
    return self.a * self.b


class Validator:
    def validate_shape(
        self, shape: CanCalculateArea, max_limit: float
    ) -> CanCalculateArea:
        if shape.calculate_area() > max_limit:
            raise ValueError("The area is too big")
        return shape


def main():
    c1 = Circle(radius=12)
    s1 = Square(side=10)
    # d1 = Diamond(a=19, b=12)

    validator = Validator()
    shape1 = validator.validate_shape(c1, 12222)
    shape2 = validator.validate_shape(s1, 133)
    # shape3 = validator.validate_shape("Hello", 1444)

    print(shape1)
    print(shape2)
    # print(shape3)
    print(signature(validator.validate_shape))
    c1.calculate_area()


def foo(a: int):
    pass


foo("dsjhfliu")

main()
