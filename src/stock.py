class Stock:
    def __init__(self):
     self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, name, amount):
        for item in self.items:
            if item.name == name:
                if amount > item.amount:
                    raise ValueError(f"Kan inte ta bort {amount} st {name}, endast {item.amount} finns")
                item.amount -= amount
                if item.amount == 0:
                    self.items.remove(item)  # ta bort posten helt om den blir tom
                return
        raise ValueError(f"{name} finns inte i lagret")
