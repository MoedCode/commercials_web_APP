#!/usr/bin/env python3

class ProductConsole:
    def __init__(self):
        self.products = []

    def display_menu(self):
        print("=== Product Management Console ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Exit")

    def run_console(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_products()
            elif choice == "3":
                print("Exiting the Product Management Console. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def add_product(self):
        product_data = {}
        product_data['name'] = input("Enter the product name: ")
        product_data['category'] = input("Enter the product category: ")
        product_data['description'] = input("Enter the product description: ")
        product_data['price'] = float(input("Enter the product price: "))
        product_data['discount'] = float(input("Enter the product discount: "))
        product_data['stock_quantity'] = int(input("Enter the stock quantity: "))
        product_data['brand'] = input("Enter the product brand: ")
        product_data['rating'] = float(input("Enter the product rating: "))
        product_data['in_stock'] = input("Is the product in stock? (True/False): ").lower() == 'true'
        product_data['img_list'] = input("Enter a comma-separated list of image URLs: ").split(',')

        product_instance = Product(**product_data)
        self.products.append(product_instance)
        print("Product added successfully!")

    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            for idx, product in enumerate(self.products, start=1):
                print(f"Product {idx}: {product.name}, Price: ${product.price}, Stock: {product.stock_quantity}")

if __name__ == "__main__":
    product_console = ProductConsole()
    product_console.run_console()
