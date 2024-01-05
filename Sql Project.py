sql_command = """
SELECT Customer.Id, ContactName, Address, Phone, Country, OrderDate, ShippedDate
FROM Customer, [Order]
WHERE Customer.Id = [Order].CustomerId
"""
print((sql_command))

sql_command = """ 
SELECT ContactName, Address, Phone, Country
FROM Customer 
LEFT JOIN [Order] ON Customer.Id = [Order] .CustomerId
WHERE [Order].Id IS NULL
"""
print((sql_command))

sql_command = """
SELECT OrderDetail.OrderId, OrderDetail.Quantity, Product.ProductName, Product.QuantityPerUnit, Product.UnitsOnOrder, Product.UnitPrice
FROM OrderDetail
JOIN Product ON OrderDetail.ProductId = Product.Id
ORDER BY Product.UnitPrice DESC
"""
print((sql_command))

sql_command = """
SELECT Id, ProductName, QuantityPerUnit, UnitPrice
FROM Product
WHERE UnitPrice BETWEEN 20 AND 25 AND Discontinued = 0
ORDER BY UnitPrice ASC;
"""
print((sql_command))
