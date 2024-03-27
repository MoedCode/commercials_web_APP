CREATE TABLE IF NOT EXISTS users2 (
    id VARCHAR(40) PRIMARY KEY NOT NULL UNIQUE,
    created_at VARCHAR(50) NOT NULL,
    updated_at VARCHAR(50) NOT NULL,
    email VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    nickname VARCHAR(128),
    budget INT NOT NULL,
    image VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS products2 (
    id VARCHAR(40) PRIMARY KEY NOT NULL UNIQUE,
    created_at VARCHAR(50) NOT NULL,
    updated_at VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL UNIQUE,
    category VARCHAR(255),
    brand VARCHAR(255),
    price FLOAT,
    stock_quantity INT,
    barcode VARCHAR(40) NOT NULL,
    rating FLOAT,
    discount FLOAT,
    in_stock BOOLEAN,
    Description TEXT,
    about TEXT,
    img_list TEXT,
    owner VARCHAR(40),
    CONSTRAINT fk_owner FOREIGN KEY (owner) REFERENCES users2(id)
);

