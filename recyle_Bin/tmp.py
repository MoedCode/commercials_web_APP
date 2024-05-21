#!/usr/bin/env python3

from market import app, db, Products

# Make sure the app context is pushed
app.app_context().push()

# Create the database tables if not created yet
db.create_all()

# Define product data
product_data = {
    "name": "smart watch",
    "category": "Electronic--ssmart-watch-sport/Electronic--ssmart-watch-sport",
    "brand": "Sample Brand",
    "price": 99.99,
    "stock_quantity": 50,
    "rating": 4.5,
    "discount": 10.0,
    "In_Stock": True,
    "description": "This is aElectronic--smart-watch-sport/Electronic--ssmart-watch-sport description.",
    "about": "More information about the sample product.",
    "img_list": [
        "/static/images/market/Smartwatch0.jfif",
        "/static/images/market/Smartwatch1.jfif",
        "/static/images/market/Smartwatch2.jfif"]
}

# Create a new product instance
product_instance = Products(**product_data)

# Save the product to the database
product_instance.save("DB")

# Retrieve the product using its barcode
barcode_to_search = '123456789'
queried_product = Products.query.filter_by(barcode=barcode_to_search).first()

# Check if the product is found
if queried_product:
    # Print product information
    print(f"Product Name: {queried_product.name}")
    print(f"Category: {queried_product.category}")
    # ... (print other attributes as needed)
else:
    print(f"Product with barcode {barcode_to_search} not found.")
