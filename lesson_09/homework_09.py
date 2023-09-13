current_exchange_rate = {
    "USD": 1,
    "EUR": 1.07,
    "UAH": 0.027,
}


class Price:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def add(self, other):
        if self.currency == other.currency:
            return Price(self.amount + other.amount, "USD")
        else:
            return Price(self.convert_to_usd() + other.convert_to_usd(), "USD")

    def subtract(self, other):
        if self.currency == other.currency:
            return Price(self.amount - other.amount, "USD")
        else:
            return Price(self.convert_to_usd() - other.convert_to_usd(), "USD")

    def convert_to_usd(self):
        if self.currency == "USD":
            return self.amount
        else:
            return self.amount * current_exchange_rate[self.currency]

    def convert_from_usd(self, usd_amount, target_currency):
        if target_currency == "USD":
            return usd_amount
        else:
            return usd_amount * current_exchange_rate[target_currency]


price1 = Price(100, "UAH")
price2 = Price(1, "EUR")
result_add = price1.add(price2)
result_subtract = price1.subtract(price2)


print(f"Result of addition: {result_add.amount} {result_add.currency}")
print(
    f"Result of subtraction: {result_subtract.amount} "
    f"{result_subtract.currency}"
)
