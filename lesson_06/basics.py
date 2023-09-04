from typing import Any, Callable


def logger(func: callable) -> Callable:
    def inner(name: str):
        print(f"Running the {func.__name__}...")
        results: Any = func(name)
        if results:
            print(f"Results: {results}")
        else:
            print("There is no results...")

    return inner


@logger
def greeting(name: str) -> None:
    print(f"Hey {name}")


greeting(name="John")
