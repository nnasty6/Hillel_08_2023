import sys

from pympler.asizeof import asizeof

users: list[str] = ["john", "marry", "jack", "john", "marry", "mark"]

# users_gen = (user for user in users) - генераторное выражение
# user_gen = _user_gen
# def _user_gen(): генераторная функция
#     for user in users:
#         yield user

# users_seen = set()
# for user in users:
#     if user in users_seen:
#         continue
#     users_seen.add(user)
#     print(user)


def dedup(collection):
    items = set()
    for item in collection:
        if item in items:
            continue
        yield item
        items.add(item)


for user in dedup(users):
    print(user)

print(sys.getsizeof(users))
print(asizeof(users))
