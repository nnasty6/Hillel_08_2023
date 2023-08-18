from typing import Generator
from uuid import UUID, uuid4

used_uuids_by_user: dict[str, set[UUID]] = {}

# {
#     "john": {d5c9b132-1550-4583-a81d-1011e0a48361, ...}
#     "mary": {53e841d0-5b4f-4a95-9d96-2007dd37d86d, ...}
# }


# Простая функция
def func_generate_unique_uuid(user: str) -> UUID:
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids_by_user[user]:
            used_uuids_by_user[user].add(generated_uuid)
            return generated_uuid

        # if generated_uuid in used_uuids:
        #     continue
        # used_uuids.add(generated_uuid)
        # return generated_uuid


# Генератор
def generate_unique_uuid() -> Generator[UUID, None, None]:
    # основное отличие то, что мы переносим глобальную переменную used_uuids
    # в функцию делая ее локальной и возвращаем yield
    used_uuids: set[UUID] = set()
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids:
            used_uuids.add(generated_uuid)
            yield generated_uuid


john_unique_uuid = generate_unique_uuid()
marry_unique_uuid = generate_unique_uuid()

print(next(john_unique_uuid))
print(next(john_unique_uuid))
print(next(marry_unique_uuid))
print(next(marry_unique_uuid))

# print("The ordinary func")
# print(func_generate_unique_uuid())
# print(func_generate_unique_uuid())
# print(func_generate_unique_uuid())
# print(func_generate_unique_uuid())
# print(func_generate_unique_uuid())
