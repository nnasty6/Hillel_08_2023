currency_dict: dict = {"USD": 1, "EUR": 0.93, "GBP": 0.80, "UAH": 37}


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def exchange_other(self, other: "Price"):
        return int(other.amount / currency_dict[other.currency])

    def exchange_self(self):
        return int(self.amount / currency_dict[self.currency])

    def __add__(self, other: "Price"):
        print(self.exchange_self())
        print(self.exchange_other(other))

        if self.currency == other.currency:
            return f"{self.amount + other.amount} {self.currency}"
        elif self.currency == "USD" and other.currency != "USD":
            return f"{self.amount + self.exchange_other(other)} USD"
        elif self.currency != "USD" and other.currency == "USD":
            return f"{self.exchange_self() + other.amount} USD"
        else:
            return f"{self.exchange_self() + self.exchange_other(other)} USD"

    def __sub__(self, other: "Price"):
        if self.currency == other.currency:
            return f"{self.amount - other.amount} {self.currency}"
        elif self.currency == "USD" and other.currency != "USD":
            return f"{self.amount - self.exchange_other(other)} USD"
        elif self.currency != "USD" and other.currency == "USD":
            return f"{self.exchange_self() - other.amount} USD"
        else:
            return f"{self.exchange_self() - self.exchange_other(other)} USD"


price1 = Price(1000, "GBP")
price2 = Price(1000, "EUR")

sum_p: Price = price1 + price2
sub_p: Price = price1 - price2

print(f"Sum of prices = {sum_p}, subtraction of prices =  {sub_p}")
