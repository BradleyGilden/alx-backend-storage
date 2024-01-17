-- a trigger that decreases the quantity of an item after adding a new order
-- creating the trigger
CREATE TRIGGER decrease
AFTER INSERT ON holberton.orders
FOR EACH ROW
BEGIN
    UPDATE holberton.items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
