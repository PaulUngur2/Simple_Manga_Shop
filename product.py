class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }
