from dataclasses import dataclass


class PaymentSystem:
    def __init__(self, name) -> None:
        self.name = name

    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using {self.name}")


# class Product:
#     def __init__(self, id, name, price) -> None:
#         self.id: str = id
#         self.name: str = name
#         self.price: float = price
# =


@dataclass
class Product:
    id: str
    name: str
    price: float


def buy(self, products: dict[Product,], payment_system: PaymentSystem):
    total = self.price  # * quantity
    payment_system.pay(total)

    return total


phone = Product("Phone", 1000)
paypal = PaymentSystem("PayPal")

phone.buy(2, paypal)
