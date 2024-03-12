#!/usr/bin/env python3
from modules.engine.local_storage import LocalStorage
from StoreMain import Products
import random

def generate_products():
    local_storage = LocalStorage()

    product_names = ["Phone", "Laptop", "Tablet", "Headphones", "Camera", "Smartwatch", "Gaming Console", "Keyboard", "PC"]
    categories = ["Electronics", "Computers", "Accessories"]
    brands = ["BrandA", "BrandB", "BrandC"]
    descriptions = ["High-quality product", "Latest technology", "Affordable price", "Limited edition"]
    abouts = ["About this product...", "Learn more about it...", "Explore the features..."]

    for _ in range(30):
        name = random.choice(product_names)
        category = random.choice(categories)
        brand = random.choice(brands)
        price = round(random.uniform(50, 1000), 2)
        stock_quantity = random.randint(0, 100)
        rating = round(random.uniform(1, 5), 2)
        discount = round(random.uniform(0, 50), 2)
        description = random.choice(descriptions)
        about = random.choice(abouts)

        img_list = [
            f"static/images/market/{name}{i}.jfif" for i in range(random.randint(1, 5))
        ]

        product = Products(
            name=name,
            category=category,
            brand=brand,
            price=price,
            stock_quantity=stock_quantity,
            rating=rating,
            discount=discount,
            description=description,
            about=about,
            img_list=img_list
        )

        product.save(save_option="local")

if __name__ == "__main__":
    generate_products()
