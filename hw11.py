import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("community_center.db")
cursor = conn.cursor()

# SQL code to create the table and insert data
sql_code = """
-- ============================================================
-- SQL Sorting & Filtering
-- Activity: Community Centre Activity Explorer
-- ============================================================

-- ---- PART 1: Build and Explore the Table ----

CREATE TABLE IF NOT EXISTS community_activity (
    activity_id     INTEGER PRIMARY KEY,
    activity_name   TEXT    NOT NULL,
    activity_type   TEXT    NOT NULL,
    day             TEXT    NOT NULL,
    participants    INTEGER NOT NULL,
    duration_mins   INTEGER NOT NULL
);

INSERT INTO community_activity VALUES (1, 'Yoga Class',        'Wellness', 'Monday',    18, 60);
INSERT INTO community_activity VALUES (2, 'Art Workshop',      'Creative', 'Tuesday',   12, 90);
INSERT INTO community_activity VALUES (3, 'Chess Club',        'Games',    'Wednesday', 16, 75);
INSERT INTO community_activity VALUES (4, 'Dance Practice',    'Wellness', 'Thursday',  20, 60);
INSERT INTO community_activity VALUES (5, 'Coding Club',       'Learning', 'Friday',    14, 90);
INSERT INTO community_activity VALUES (6, 'Book Circle',       'Learning', 'Saturday',  10, 60);
INSERT INTO community_activity VALUES (7, 'Painting Club',     'Creative', 'Saturday',  15, 75);
INSERT INTO community_activity VALUES (8, 'Football Practice', 'Sports',   'Sunday',    22, 90);
INSERT INTO community_activity VALUES (9, 'Meditation Hour',   'Wellness', 'Sunday',    13, 45);

-- ---- PART 2: ORDER BY ----

-- Sort all activities by participants, lowest first
SELECT activity_name, participants
FROM community_activity
ORDER BY participants ASC;

-- Sort all activities by participants, highest first
SELECT activity_name, participants
FROM community_activity
ORDER BY participants DESC;
"""

# Execute the SQL script
cursor.executescript(sql_code)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
