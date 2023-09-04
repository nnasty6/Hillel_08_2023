class MyCotext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, *args, **kwargs):
        print("Exiting")

    def foo(self):
        print("I am foo")


with MyCotext() as context:
    context.foo()
