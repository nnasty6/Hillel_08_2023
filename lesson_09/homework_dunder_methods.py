currency_dict: dict = {"USD": 1, "EUR": 0.93, "GBP": 0.80, "UAH": 37}


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def exchange(self, other: "Price"):
        return int(self.amount / currency_dict[other.currency])

    def __add__(self, other: "Price"):
        if self.currency == other.currency:
            return f"{self.amount + other.amount} {self.currency}"
        else:
            # print(self.exchange(self))
            # print(self.exchange(other))
            return f"{self.exchange(self) + self.exchange(other)} USD"

    def __sub__(self, other: "Price"):
        if self.currency == other.currency:
            return f"{self.amount - other.amount} {self.currency}"
        else:
            return f"{self.exchange(self) - self.exchange(other)} USD"


price1 = Price(1000, "EUR")
price2 = Price(1000, "USD")

sum_p: Price = price1 + price2
sub_p: Price = price1 - price2

print(f"Sum of prices = {sum_p}, subtraction of prices =  {sub_p}")
