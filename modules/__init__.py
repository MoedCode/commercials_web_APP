storage_t = "DB"

if storage_t == "LOCAL":
    from modules.engine.local_storage import LocalStorage

    local_storage = LocalStorage()
    local_storage.reload()
product_data = {
    "name": "nokia 10 pureView",
    "category": "Electronics - smart phones ",
    "brand": "Nokia",
    "price": 99.99,
    "stock_quantity": 50,
    "rating": 4.5,
    "discount": 10.0,
    "In_Stock": True,

    "description": "Summary Nokia 10 PureView ram 8 GB camera 16 MP + 8 MP + 12 MP +12 MP display 6.1 inches (15.49 cm) performance Qualcomm Snapdragon 875 storage 128 GB battery 4000 mAh",
    "about": "More information about the sample product.",
    "img_list": [
        "/static/images/market/nokia_10_pureview.jfif",
        "/static/images/market/nokia_10_pureview.jfif",
]
    }