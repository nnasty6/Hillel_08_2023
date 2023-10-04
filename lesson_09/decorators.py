# def staticmethod(func):
#     def inner(*args, **kwargs):
#         if "self" in args:
#             del from args
#         return func(*args, **kwargs)
#     return inner


class Shop:
    USERS_MAX_SIZE = 300

    def register(self, username, password1, password2, email):
        pass

    def login(self, username, password):
        pass

    @classmethod
    def build_new(cls, domin: str):
        # Host the application on {domain}
        # ...
        cls.USERS_MAX_SIZE
        # cls.login()
        # cls = Shop
        # Shop.login()

    @staticmethod
    def get_current_users_amount(user_card_info):
        # numbers = SELECT COUNT(id) FROM users;
        return 12

    def buy(self, product: dict):
        pass


zara = Shop()
bershka = Shop()

zara.build_new("zara.com")
Shop.build_new("bershka.com")

zara.buy(
    {
        "pants L": 1222,
    },
)

# Shop.buy(
#     zara,
#     {
#         "pants L": 1222,
#     },
# )

# With staticmethod
# Shop.buy(
#     {
#         "pants L": 1222,
#     },
# )
