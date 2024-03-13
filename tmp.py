#!/usr/bin/env python3

from market import Products

# Replace '123456789' with the actual barcode you want to search for
barcode_to_search = '123456789'

# Query the database to find the product with the given barcode
product_instance = Products.query.filter_by(barcode=barcode_to_search).first()

if product_instance:
    # If the product is found, you can then access its attributes
    print(f"Product Name: {product_instance.name}")
    print(f"Category: {product_instance.category}")
    # ... (print other attributes as needed)
else:
    print(f"Product with barcode {barcode_to_search} not found.")