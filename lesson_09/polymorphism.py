from functools import singledispatch


@singledispatch
def custom_add(a, b):
    raise NotImplementedError("Unsupported type")


@custom_add.register(int)
def _(a, b):
    return a + b


@custom_add.register(str)
def _(a, b):
    return f"Concat {a}{b}"


print(custom_add(1, 1))
print(custom_add("1", "1"))
print(custom_add(12.2, "1"))
