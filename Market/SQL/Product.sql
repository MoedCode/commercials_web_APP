CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    nickname VARCHAR(128),
    budget INT NOT NULL,
    image VARCHAR(150),
    id VARCHAR(40) PRIMARY KEY NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

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
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    owner VARCHAR(40),
    CONSTRAINT fk_owner FOREIGN KEY (owner) REFERENCES users(id)


);
