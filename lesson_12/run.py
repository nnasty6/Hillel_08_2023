from pprint import pprint as print

from services import Dish, DishSize, Kitchen

# from typing import TYPE_CHECKING


# sys.path.append("/Users/ger.anastasia.a/Documents/Projects/test140823_2")


# Is not recomended
# if TYPE_CHECKING is True:
#     from services import Kitchen

# import importlib
# kitchen = importlib.import_module("kitchen")
# kitchen.Kitchen


def main(kitchen: "Kitchen"):
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
    print(dishes)


if __name__ == "main":
    pass
    # main()

# regular execution
# for dish in dishes:
#     Kitchen.cook(dish)

# concurrent execution
# threads = [
#     Thread(
#         # this is callback - the object of the func
#         # to be called
#         target=Kitchen.cook,
#         args=(dish,),
#     )
#     for dish in dishes
# ]

# for thread in threads:
#     thread.start()


# for thread in threads:
#     thread.join()

# processes
# tasks = [
#     Process(
#         # this is callback - the object of the func
#         # to be called
#         target=Kitchen.cook,
#         # args=(dish,),
#         args=[dish],
#     )
#     for dish in dishes
# ]

# for task in tasks:
#     task.run()
# # start() also doesn't work

# for task in tasks:
#     task.join()

print("All threads are finished")
