-- Create database
CREATE DATABASE ProMarket_DB;

-- Create user
CREATE USER 'ProMarket'@'localhost' IDENTIFIED BY 'ProMarket_PWD';

-- Grant privileges
GRANT ALL PRIVILEGES ON ProMarket_DB.* TO 'ProMarket'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
