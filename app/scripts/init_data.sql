INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES
('Juan', 'Pérez', 'juan.perez@email.com', '555-1234', 'Calle de la Rosa 12, Sevilla'),
('Ana', 'López', 'ana.lopez@email.com', '555-5678', 'Av. Libertad 3, Valencia'),
('Carlos', 'González', 'carlos.gonzalez@email.com', '555-8765', 'Calle del Sol 7, Madrid'),
('Laura', 'Martínez', 'laura.martinez@email.com', '555-3456', 'Carrer de la Marina 5, Barcelona'),
('Eva', 'Sánchez', 'pedro.sanchez@email.com', '555-6543', 'Av. Paseo de Marques 9, Alicante');


INSERT INTO Products (Name, Description, Price, StockQuantity, Category)
VALUES
('Perfume Chanel No. 5', 'Perfume floral y aldehídico, uno de los más emblemáticos', 120.99, 50, 'Women'),
('Perfume Dolce & Gabbana Light Blue', 'Fragancia fresca y floral, ideal para el verano', 75.99, 40,'Women'),
('Perfume Gucci Bloom', 'Perfume floral para mujeres con notas de jazmín y nardo', 110.00, 30,'Women'),
('Perfume Yves Saint Laurent Black Opium', 'Fragancia oriental floral, notas de café y vainilla', 115.00, 55,'Women'),
('Perfume Jo Malone London English Pear & Freesia', 'Perfume afrutado floral, con notas de pera y fresia', 145.00, 35,'Women'),
('Perfume Chanel Coco Mademoiselle', 'Perfume floral amaderado para mujeres, notas de naranja y rosa', 130.00, 50,'Women'),
('Perfume Viktor & Rolf Flowerbomb', 'Fragancia floral con notas de jazmín, naranja y patchouli', 120.00, 45,'Women'),
('Perfume Lancôme La Vie Est Belle', 'Perfume dulce y floral, con notas de iris y pachulí', 110.00, 55,'Women'),
('Perfume Paco Rabanne 1 Million', 'Perfume amaderado especiado con notas de cuero y ámbar', 95.00, 65,'Men'),
('Perfume Giorgio Armani Acqua di Gio', 'Perfume fresco acuático, con notas de cítricos y jazmín', 99.99, 60,'Men'),
('Perfume Jean Paul Gaultier Le Male', 'Perfume oriental especiado, con notas de menta, lavanda y vainilla', 90.00, 80,'Men'),
('Perfume Tom Ford Black Orchid', 'Perfume floral y especiado, con notas de orquídea negra y especias', 140.00, 40,'Men'),
('Perfume Creed Aventus', 'Perfume amaderado y afrutado, ideal para hombres con estilo', 320.00, 25,'Men'),
('Perfume Versace Eros', 'Fragancia amaderada y oriental, inspirada en la mitología griega', 85.00, 70,'Men'),
('Perfume Dior Sauvage', 'Perfume amaderado especiado, ideal para hombres', 95.49, 60, 'Men');



INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
VALUES
(1, '2025-02-10', 120.99),
(2, '2025-02-12', 95.49),
(3, '2025-02-13', 110.00),
(4, '2025-02-14', 185.99),
(5, '2025-02-15', 85.00);


INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Subtotal)
VALUES
(1, 1, 1, 120.99),
(2, 2, 1, 95.49),
(3, 4, 1, 110.00),
(4, 2, 1, 95.49),
(4, 3, 1, 75.99),
(5, 5, 1, 85.00);
