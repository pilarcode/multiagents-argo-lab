-- Create Customers table
CREATE TABLE IF NOT EXISTS Customers(
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Email TEXT UNIQUE NOT NULL,
        Phone TEXT,
        Address TEXT
);

-- Create Products table
CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Description TEXT,
        Price REAL NOT NULL,
        StockQuantity INTEGER NOT NULL,
        Category TEXT NOT NULL
    );


-- Create Orders table
CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER NOT NULL,
        OrderDate DATE NOT NULL,
        TotalAmount REAL NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    );

-- Create OrderDetails table
CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER NOT NULL,
        ProductID INTEGER NOT NULL,
        Quantity INTEGER NOT NULL,
        Subtotal REAL NOT NULL,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    );