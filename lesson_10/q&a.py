from typing import Any

message = (
    "In software engineering, SOLID is a mnemonic acronym for five "
    "design principles intended to "
    "make object-oriented designs more understandable, "
    "flexible, and maintainable. "
)


class PaymentSystem:
    def __init__(self, provider) -> None:
        self.provider: str = provider

    def foo(self):
        return "I am foo from Payment system"

    def __getattribute__(self, name: str) -> Any:
        if name == "pasword":
            return "Access denied!"
        # if name not in self.__dict__.keys():
        #     raise AttributeError(
        # f"Your class does not have this field: {name}")
        # return super().__getattribute__(name)

    # Работа __getattribute__ под капотом
    def get_attr(self, name: str) -> Any:
        if name not in self.__dict__.keys():
            raise AttributeError(
                f"Your class does not have this field: {name}"
            )
        return self.__dict__[name]


paypal = PaymentSystem(provider="PayPal")
print(paypal.__dict__)

# print(paypal.__dict__["provider"])

# paypal.provider
# data = paypal.get_attr("provider")
print(paypal.provider)
