class Product:
    def __init__(self, name: str, category: str, price: float, stock: int):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def change_price(self, new_price: float) -> None:
        self.price = new_price

    def change_stock(self, new_stock: int) -> None:
        self.stock = new_stock

    def __str__(self) -> str:
        return f"{self.name} | {self.category} | {self.price} грн | {self.stock} шт"


class Order:
    def __init__(self):
        self.products: dict[Product, int] = {}
        self.total = 0

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= product.stock:
            self.products[product] = quantity
            product.change_stock(product.stock - quantity)
            self.calculate_total()
        else:
            print(f"Недостатньо товару: {product.name}")

    def calculate_total(self) -> float:
        self.total = 0

        for product, quantity in self.products.items():
            self.total += product.price * quantity

        return self.total

    def __str__(self) -> str:
        result = "Деталі замовлення:\n"

        for product, quantity in self.products.items():
            result += f"{product.name}: {quantity} шт. x {product.price} грн\n"

        result += f"Сума: {self.calculate_total()} грн"
        return result


class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.orders: list[Order] = []

    def add_order(self, order: Order) -> None:
        self.orders.append(order)

    def __str__(self) -> str:
        return f"{self.name} | {self.email}"


def load_shop(filename: str) -> tuple[list[Product], list[Customer]]:
    products = []
    customers = []
    section = ""

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "PRODUCTS":
                    section = "products"
                    continue

                if line == "CUSTOMERS":
                    section = "customers"
                    continue

                if not line:
                    continue

                data = line.split(";")

                if section == "products":
                    product = Product(
                        data[0],
                        data[1],
                        float(data[2]),
                        int(data[3])
                    )
                    products.append(product)

                elif section == "customers":
                    customer = Customer(data[0], data[1])
                    customers.append(customer)

    except FileNotFoundError:
        print("Файл не знайдено")

    return products, customers


products, customers = load_shop("shop.txt")

print("Товари")
for product in products:
    print(product)

print("\nКлієнти")
for customer in customers:
    print(customer)

order = Order()

order.add_product(products[0], 2)
order.add_product(products[2], 1)

customers[0].add_order(order)

print("\nЗамовлення")
print(order)

print("\nСклад після замовлення")
for product in products:
    print(product)