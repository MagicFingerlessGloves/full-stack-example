CREATE TABLE IF NOT EXISTS cats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    breed VARCHAR(50),
    age INT
);

INSERT INTO cats (name, breed, age) VALUES
('Milo', 'Siamese', 2),
('Luna', 'Maine Coon', 3),
('Oliver', 'Bengal', 1),
('Leo', 'Persian', 4),
('Bella', 'Sphynx', 2),
('Charlie', 'Ragdoll', 5),
('Simba', 'British Shorthair', 3),
('Chloe', 'Abyssinian', 2),
('Max', 'Scottish Fold', 1),
('Nala', 'Russian Blue', 4),
('Cleo', 'Savannah', 2);