-- Create the necessary tables and import data
-- Make sure to adjust the path to the metal_bands.sql file
-- You can execute this part only once to set up the database
CREATE TABLE IF NOT EXISTS bands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    origin VARCHAR(255),
    nb_fans INT
);

-- Load data from metal_bands.sql into the bands table
-- Make sure to adjust the path to the metal_bands.sql file
-- You can execute this part only once to import the data
SOURCE /path/to/metal_bands.sql;

-- Calculate the number of fans for each origin and rank them
SELECT origin, SUM(nb_fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;
