import json

from category import Category
from product import Product


class MangaStore:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category_name):
        self.categories = [c for c in self.categories if c.name != category_name]

    def list_categories(self):
        for category in self.categories:
            print(f"Category: {category.name}")
            category.list_products()

    def find_category(self, category_name):
        for category in self.categories:
            if category.name == category_name:
                return category
        return None

    def to_dict(self):
        category_list = [category.to_dict() for category in self.categories]
        return {
            'categories': category_list
        }

    def save_to_disk(self, file_name):
        data = self.to_dict()
        with open(file_name, 'w') as file:
            json.dump(data, file)

    def load_from_disk(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
            for category_data in data.get('categories', []):
                category = Category(category_data['name'])
                for product_data in category_data['products']:
                    product = Product(product_data['name'], product_data['price'], product_data['stock'])
                    category.add_product(product)
                self.add_category(category)
        except FileNotFoundError:
            pass
