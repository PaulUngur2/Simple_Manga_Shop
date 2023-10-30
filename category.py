class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def list_products(self):
        for product in self.products:
            print(f"{product.name} - Price: {product.price} - In Stock: {product.stock}")

    def to_dict(self):
        product_list = [product.to_dict() for product in self.products]
        return {
            'name': self.name,
            'products': product_list
        }
