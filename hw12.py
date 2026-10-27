import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("marine_observations.db")
cursor = conn.cursor()

# SQL code to create the table, insert data, and perform aggregate queries
sql_code = """
-- ---- PART 1: Create Table and Insert Data ----

CREATE TABLE IF NOT EXISTS marine_observation (
    observation_id INTEGER PRIMARY KEY,
    animal_group TEXT NOT NULL,
    habitat TEXT NOT NULL,
    depth_m REAL NOT NULL,
    estimated_weight_kg REAL NOT NULL
);

INSERT INTO marine_observation VALUES (1, 'Shark', 'Open Ocean', 200, 500);
INSERT INTO marine_observation VALUES (2, 'Dolphin', 'Open Ocean', 150, 300);
INSERT INTO marine_observation VALUES (3, 'Whale', 'Deep Sea', 1000, 30000);
INSERT INTO marine_observation VALUES (4, 'Tuna', 'Open Ocean', 100, 200);
INSERT INTO marine_observation VALUES (5, 'Octopus', 'Coral Reef', 50, 20);
INSERT INTO marine_observation VALUES (6, 'Sea Turtle', 'Coral Reef', 30, 150);
INSERT INTO marine_observation VALUES (7, 'Jellyfish', 'Open Ocean', 20, 5);

-- ---- PART 3: COUNT ----

-- Total number of marine observations
SELECT COUNT(observation_id) AS total_observations
FROM marine_observation;

-- Count observations made in the Open Ocean
SELECT COUNT(observation_id) AS open_ocean_observations
FROM marine_observation
WHERE habitat = 'Open Ocean';

-- ---- PART 4: SUM and AVG ----

-- Total estimated weight of all observed animals
SELECT SUM(estimated_weight_kg) AS total_estimated_weight_kg
FROM marine_observation;

-- Average depth of all observations
SELECT AVG(depth_m) AS average_observation_depth_m
FROM marine_observation;

-- ---- PART 5: Combining Aggregate Functions ----

SELECT
    COUNT(observation_id)        AS total_observations,
    COUNT(DISTINCT animal_group) AS unique_animal_groups,
    SUM(estimated_weight_kg)     AS total_estimated_weight_kg,
    AVG(depth_m)                 AS average_observation_depth_m
FROM marine_observation;
"""

# Execute the SQL script
cursor.executescript(sql_code)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and queries executed successfully!")