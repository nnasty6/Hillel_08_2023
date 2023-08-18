def foo():
    print("Hello, I am foo")


def bar(function):
    function.__call__()
    # print("Hello, I am bar")
    return 12


def baz():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


gen = baz()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# print(foo())
# print(baz())
