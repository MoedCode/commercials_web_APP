CREATE TABLE IF NOT EXISTS products (
    id VARCHAR(40)  PRIMARY KEY NOT NULL UNIQUE ,
    name VARCHAR(255) NOT NULL UNIQUE,
    category VARCHAR(255),
    brand VARCHAR(255),
    price DECIMAL(10, 2),
    stock_quantity INT,
    barcode VARCHAR(40)   NOT NULL,
    rating FLOAT,
    discount FLOAT,
    in_stock BOOLEAN,
    Description TEXT,
    about TEXT,
    img_list TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
