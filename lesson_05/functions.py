def foo():
    return 1, 2, 3, 4, 5


# data1, data2, data3, data4, data5 = foo()
data = foo()

# print(data)
# print(data1, data2, data3, data4, data5)

contact_info = ("John", "Doe", "Kyiv", "33111", "+380887655656", "man", 40)
# name, surname, city, postal_code, phone_number, sex, age = contact_info
name, surname, *meta, age = contact_info

# print(name, surname, age)
# print(meta)


# def create_user(name, surname, city, postal_code, phone_number, sex, age):
def create_user(*args, **kwargs):
    print("User is crested")
    print(args)
    print(kwargs)
    # print(f"The name is {name}")
    # print(f"The surname is {surname}")


create_user(
    name="John",
    surname="Doe",
    city="Kyiv",
    postal_code="33111",
    phone_number="+380887655656",
    sex="man",
    age=40,
)
