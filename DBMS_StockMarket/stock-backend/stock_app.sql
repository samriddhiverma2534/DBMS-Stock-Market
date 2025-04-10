USE stocks;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255)
);

 CREATE TABLE stocks (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(100),
    ->     symbol VARCHAR(20),
    ->     market_price DECIMAL(10,2),
    ->     closing_price DECIMAL(10,2)
    -> );

INSERT INTO stocks (name, symbol, market_price, closing_price) VALUES
    -> ('Bajaj Finance', 'BAJFINANCE', 8739.00, 8650.00),
    -> ('Vedanta Ltd', 'VEDL', 402.50, 420.00),
    -> ('Jindal Steel and Power Ltd', 'JINDALSTEL', 675.80, 670.00),
    -> ('Aurobindo Pharma', 'AUROPHARMA', 860.20, 850.00),
    -> ('Adani Enterprises', 'ADANIENT', 2230.45, 2210.00),
    -> ('Hindustan Unilever', 'HINDUNILVR', 2485.75, 2500.00),
    -> ('Reliance Industries', 'RELIANCE', 2745.30, 2700.00),
    -> ('Mahindra & Mahindra Ltd', 'M&M', 1480.00, 1460.00),
    -> ('ITC Ltd', 'ITC', 425.20, 430.00),
    -> ('Tata Consumers', 'TATACONSUM', 845.90, 840.00),
    -> ('HDFC Bank', 'HDFCBANK', 1816.80, 1426.80),
    -> ('Bharti Airtel', 'BHARTIARTL', 1740.50, 1747.00),
    -> ('Infosys', 'INFY', 1456.10, 1460.00),
    -> ('Larsen & Toubro', 'LT', 3259.00, 3400.00),
    -> ('Sun Pharmaceutical Industries', 'SUNPHARMA', 1705.00, 1778.85),
    -> ('HCL Technologies', 'HCLTECH', 1427.00, 1449.00),
    -> ('National Thermal Power Corporation', 'NTPC', 350.40, 358.85);

CREATE TABLE portfolio (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     user_id INT,
    ->     stock_symbol VARCHAR(20),
    ->     quantity INT,
    ->     invested_amount DECIMAL(10,2)
    -> );
INSERT INTO portfolio (user_id, stock_symbol, quantity, invested_amount) VALUES
    -> (1, 'TATACONSUM', 50, 15000.00),
    -> (1, 'RELIANCE', 20, 55000.00),
    -> (1, 'HDFCBANK', 10, 18000.00),
    -> (1, 'INFY', 25, 36000.00),
    -> (1, 'ITC', 100, 43000.00),
    -> (1, 'LT', 5, 16000.00),
    -> (1, 'M&M', 15, 22200.00),
    -> (1, 'SUNPHARMA', 10, 17050.00),
    -> (1, 'HCLTECH', 12, 17124.00),
    -> (1, 'NTPC', 80, 28000.00);

CREATE TABLE watchlist (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     user_id INT,
    ->     stock_symbol VARCHAR(20)
    -> );
INSERT INTO watchlist (user_id, stock_symbol) VALUES
    -> (1, 'VEDL'),
    -> (1, 'JINDALSTEL'),
    -> (1, 'ADANIENT'),
    -> (1, 'HINDUNILVR'),
    -> (1, 'BHARTIARTL'),
    -> (1, 'AUROPHARMA');

INSERT INTO users (name, phone, email, username, password)
VALUES ('Samriddhi', '9876543210', 'sam@gmail.com', 'sam123', 'Sam25');
CREATE table USERS (
    -> username VARCHAR(50) NOT NULL UNIQUE,
    ->  password VARCHAR(255) NOT NULL,
    -> name VARCHAR(100),
    -> email VARCHAR(100),
    -> phone_number VARCHAR(15)
    -> );
INSERT INTO USERS (username, password, name, email, phone_number) VALUES
    -> ('Samriddhi25', 'pbkdf2:sha256:260000$xyz$abc123encryptedhash1', 'Samriddhi Verma', 'samriddhi@gmail.com', '9812345678'),
    -> ('Srishti12', 'pbkdf2:sha256:260000$xyz$abc123encryptedhash2', 'Srishti Rai', 'srishti12@gmail.com', '9123456789'),
    -> ('SijonTh', 'pbkdf2:sha256:260000$xyz$abc123encryptedhash3', 'Sijon Thomas', 'sijonth@gmail.com', '987654321'),
    -> ('ak2711', 'pbkdf2:sha256:260000$xyz$abc123encryptedhash4', 'Akshat Kashyap', 'ak2711@gmail.com', '9001122334');

