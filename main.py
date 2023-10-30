from category import Category
from manga_store import MangaStore
from product import Product

if __name__ == "__main__":
    store = MangaStore()
    store.load_from_disk('manga_store.json')

    def list_categories():
        store.list_categories()

    def add_category():
        category_name = input("Enter category name: ")
        category = Category(category_name)
        store.add_category(category)

    def update_category():
        old_category_name = input("Enter the old category name: ")
        new_category_name = input("Enter the new category name: ")
        category = store.find_category(old_category_name)
        if category:
            category.name = new_category_name
        else:
            print("Category not found.")

    def remove_category():
        category_name = input("Enter category name to remove: ")
        store.remove_category(category_name)

    def list_products():
        category_name = input("Enter category name: ")
        category = store.find_category(category_name)
        if category:
            category.list_products()
        else:
            print("Category not found.")

    def add_product():
        category_name = input("Enter category name: ")
        category = store.find_category(category_name)
        if category:
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product price: "))
            product_stock = int(input("Enter product stock: "))
            product = Product(product_name, product_price, product_stock)
            category.add_product(product)
        else:
            print("Category not found.")

    def update_product():
        category_name = input("Enter category name: ")
        category = store.find_category(category_name)
        if category:
            product_name = input("Enter product name to update: ")
            new_product_name = input("Enter new product name: ")
            new_product_price = float(input("Enter new product price: "))
            new_product_stock = int(input("Enter new product stock: "))
            for product in category.products:
                if product.name == product_name:
                    product.name = new_product_name
                    product.price = new_product_price
                    product.stock = new_product_stock
                    break
            else:
                print("Product not found.")
        else:
            print("Category not found.")

    def remove_product():
        category_name = input("Enter category name: ")
        category = store.find_category(category_name)
        if category:
            product_name = input("Enter product name to remove: ")
            category.remove_product(product_name)
        else:
            print("Category not found.")

    def save_to_disk():
        store.save_to_disk('manga_store.json')
        print("Store data saved to disk.")

    menu = {
        '1': list_categories,
        '2': add_category,
        '3': update_category,
        '4': remove_category,
        '5': list_products,
        '6': add_product,
        '7': update_product,
        '8': remove_product,
        '9': save_to_disk,
        '10': lambda: exit("Exiting the store."),
    }

    while True:
        print("\nOptions:")
        print("1. List Categories")
        print("2. Add Category")
        print("3. Update Category Name")
        print("4. Remove Category")
        print("5. List Products in a Category")
        print("6. Add Product to a Category")
        print("7. Update Product")
        print("8. Remove Product from a Category")
        print("9. Save Store to Disk")
        print("10. Exit")

        choice = input("Enter your choice: ")
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")
