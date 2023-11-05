from dataclasses import dataclass
from enum import StrEnum, auto
from multiprocessing import Process
from threading import Thread
from time import sleep


# Enum Используется для того, чтобы
# задать какие-то контстанты
# для определенной группы
class DishSize(StrEnum):
    S = auto()
    M = auto()
    L = auto()


# Равнозначны
# DishSize = {
#     "S": "S",
#     "M": "M",
#     "L": "L",
# }
# DishSize["S"]

# DishSize.S


@dataclass
class Dish:
    name: str
    size: DishSize
    ingredients: list[str]


# food = Dish("food", DishSize.M)


class Kitchen:
    @staticmethod
    def heat(dish: Dish):
        """Tis function is IO-bound task.
        We should wait until meal is warm.
        """
        # IO-bound task - это когда мы чего-то ждем
        print(f"\n⏰ Started hitting {dish.name}")
        # NOTE: IO-bound task
        sleep(3)
        # sleep эмулирует ожидание - это единственная
        # конструкция которая является IO-bound task
        # дугих вариаций IO-bound task нет
        print(f"✅ The {dish} is warm")

    @staticmethod
    def cook(dish: Dish):
        """This function is CPU-bound task.
        We should cook the meal...
        """
        # CPU-bound task - код, который выполняется
        # последовательно - строка за строкой
        # это цикл
        print(f"\n⏰ started cooking {dish}")
        # NOTE: CPU-bound task
        _ = [i for i in range(150_000_000)]
        # _ - this means that we don't care about this var
        print(f"✅ The {dish} is ready")


pizza = Dish(
    name="Peperony",
    size=DishSize.M,
    ingredients=["tomato", "cheese", "peperoni", "dough"],
)

salad = Dish(
    name="Ceasar",
    size=DishSize.S,
    ingredients=["tomato", "cheese", "chiken", "dough"],
)

dishes = [pizza, salad]

# regular execution
# for dish in dishes:
#     Kitchen.cook(dish)

# concurrent execution
threads = [
    Thread(
        # this is callback - the object of the func
        # to be called
        target=Kitchen.cook,
        args=(dish,),
    )
    for dish in dishes
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# processes
tasks = [
    Process(
        # this is callback - the object of the func
        # to be called
        target=Kitchen.cook,
        # args=(dish,),
        args=[dish],
    )
    for dish in dishes
]

for task in tasks:
    task.run()
# start() also doesn't work

# for task in tasks:
#     task.join()

print("All threads are finished")
