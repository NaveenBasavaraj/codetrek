CREATE TABLE products (
    name TEXT NOT NULL default 'Unknown',
    price INT NOT NULL,
    quantity INT default 0
);




-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
