#!/usr/bin/env python3

from modules.products import Products
import os

if __name__ == "__main__":
    # List of product data for each image
    products_list = [
        {
        "name": name,
        "category": category,
        "brand": "Your Brand",
        "price": 0.0,  # Set the price accordingly
        "stock_quantity": 0,  # Set the stock quantity accordingly
        "rating": 0.0,  # Set the rating accordingly
        "discount": 0.0,  # Set the discount accordingly
        "in_stock": True,  # Set the in_stock flag accordingly
        "description": f"Description for {name} product.",
        "about": "More information about the sample product.",
        "img_list": [f"/static/images/market/{image_name}"]
    },
        {
            "name": "Apple Watch Series 8",
            "category": "Electronics",
            "brand": "Apple",
            "price": 599.99,
            "stock_quantity": 100,
            "rating": 4.8,
            "discount": 10.0,
            "in_stock": True,
            "description": "Description for Apple Watch Series 8.",
            "about": "More information about the Apple Watch Series 8.",
            "img_list": [
                "/static/images/market/0-Apple-Watch-Series8.jfif",
                "/static/images/market/1-Apple-Watch-Series8.jfif",
                "/static/images/market/2-Apple-Watch-Series8.jfif"
            ]
        },
        {
            "name": "VOLKMI Reno 8 Pro Smartphone",
            "category": "Electronics",
            "brand": "VOLKMI",
            "price": 699.99,
            "stock_quantity": 50,
            "rating": 4.5,
            "discount": 5.0,
            "in_stock": True,
            "description": "Description for VOLKMI Reno 8 Pro Smartphone.",
            "about": "More information about the VOLKMI Reno 8 Pro Smartphone.",
            "img_list": [
                "/static/images/market/0-VOLKMI-Reno8pro-Smartphone.jfif",
                "/static/images/market/1-VOLKMI-Reno8pro-Smartphone.jfif",
                "/static/images/market/2-VOLKMI-Reno8pro-Smartphone.jfif"
            ]
        },
        # Add more products with their respective image paths
        {
            "name": "Earbuds",
            "category": "Electronics",
            "brand": "Brand X",
            "price": 149.99,
            "stock_quantity": 30,
            "rating": 4.2,
            "discount": 0.0,
            "in_stock": True,
            "description": "Description for Earbuds.",
            "about": "More information about Earbuds.",
            "img_list": [
                "/static/images/market/earpods0.jfif",
                "/static/images/market/earpods1.jfif",
                "/static/images/market/earpods2.jfif"
            ]
        },
        {
            "name": "Smartwatch",
            "category": "Electronics",
            "brand": "Brand Y",
            "price": 249.99,
            "stock_quantity": 20,
            "rating": 4.5,
            "discount": 15.0,
            "in_stock": True,
            "description": "Description for Smartwatch.",
            "about": "More information about Smartwatch.",
            "img_list": [
                "/static/images/market/Smartwatch0.jfif",
                "/static/images/market/Smartwatch1.jfif",
                "/static/images/market/Smartwatch2.jfif"
            ]
        },
        {
            "name": "Camera",
            "category": "Electronics",
            "brand": "Brand Z",
            "price": 799.99,
            "stock_quantity": 15,
            "rating": 4.7,
            "discount": 20.0,
            "in_stock": True,
            "description": "Description for Camera.",
            "about": "More information about Camera.",
            "img_list": [
                "/static/images/market/Camera0.jfif",
                "/static/images/market/Camera1.jfif",
                "/static/images/market/Camera2.jfif"
            ]
        },
        # Add more products as needed
    ]

    # List to store product objects
    product_objects = []

    # Iterate over product data and create product objects
    for product_data in products_list:
        img_list = product_data.pop("img_list")  # Remove img_list from product_data
        for img_path in img_list:
            product_data_copy = product_data.copy()  # Create a copy of product_data
            product_name = product_data_copy["name"] + "_" + os.path.basename(img_path)  # Add image name to product name
            product_data_copy["name"] = product_name  # Update product name
            product_data_copy["img_list"] = [img_path]  # Assign img_path to img_list
            product_instance = Products(**product_data_copy)  # Create Products object
            product_objects.append(product_instance)  # Append product object to list

    # Save products
    for product_instance in product_objects:
        product_instance.save(save_option="DB")
        print(f"Product saved: {product_instance.name}")
