CREATE DATABASE nav_electric_vehicles;
GO
USE nav_electric_vehicles;
-- Create the ev_cars table
CREATE TABLE ev_cars (
    ev_car_id INT IDENTITY(1,1) PRIMARY KEY,
    brand NVARCHAR(50) CHECK (brand IN ('Tesla', 'Tata', 'Mahindra', 'Vel', 'Ford', 'Amigo')) NOT NULL,
    color NVARCHAR(50) CHECK (color IN ('Red', 'Blue', 'Black', 'White', 'Green')) NOT NULL,
    model NVARCHAR(2) CHECK (model IN ('base', 'mid-range', 'classic', 'customized', 'customized_premium')) NOT NULL,
    price INT CHECK (price BETWEEN 100000 AND 5000000),
    stock_quantity INT NOT NULL,
    CONSTRAINT brand_color_model UNIQUE (brand, color, model)
);

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT IDENTITY(1,1) PRIMARY KEY,
    ev_car_id INT FOREIGN KEY REFERENCES ev_cars(ev_car_id) NOT NULL,
    percentage_discount DECIMAL(5,2) CHECK (percentage_discount BETWEEN 0 AND 100)
);

-- Create a stored procedure to populate the ev_cars table
GO  -- Separate batches
CREATE PROCEDURE PopulateEVCars
AS
BEGIN
    DECLARE @counter INT = 0;
    DECLARE @max_records INT = 100;
    DECLARE @brand NVARCHAR(50);
    DECLARE @color NVARCHAR(50);
    DECLARE @model NVARCHAR(2);
    DECLARE @price INT;
    DECLARE @stock INT;

    -- Seed the random number generator
    SET @counter = 0;
    SET @max_records = 100;
    SET @brand = '';
    SET @color = '';
    SET @model = '';
    SET @price = 0;
    SET @stock = 0;

    WHILE @counter < @max_records
    BEGIN
        -- Generate random values
        SET @brand = (SELECT TOP 1 brand FROM (VALUES ('Tesla'), ('Tata'), ('Mahindra'), ('Vel'), ('Ford'), ('Amigo')) AS Brands(brand) ORDER BY NEWID());
        SET @color = (SELECT TOP 1 color FROM (VALUES ('Red'), ('Blue'), ('Black'), ('White'), ('Green')) AS Colors(color) ORDER BY NEWID());
        SET @model = (SELECT TOP 1 model FROM (VALUES ('base'), ('mid-range'), ('classic'), ('customized'), ('customized_premium')) AS Models(model) ORDER BY NEWID());
        SET @price = CAST(10 + RAND() * 41 AS INT);
        SET @stock = CAST(10 + RAND() * 91 AS INT);

        -- Attempt to insert a new record
        -- Duplicate brand, color, model combinations will be ignored due to the unique constraint
        BEGIN TRY
            INSERT INTO ev_cars (brand, color, model, price, stock_quantity)
            VALUES (@brand, @color, @model, @price, @stock);
            SET @counter = @counter + 1;
        END TRY
        BEGIN CATCH
            -- Handle duplicate key error
        END CATCH;
    END;
END;
GO  -- Separate batches

-- Call the stored procedure to populate the ev_cars table
EXEC PopulateEVCars;

-- Insert at least 10 records into the discounts table
INSERT INTO discounts (ev_car_id, percentage_discount)
VALUES
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00),
(6, 10.00),
(7, 30.00),
(8, 35.00),
(9, 40.00),
(10, 45.00);