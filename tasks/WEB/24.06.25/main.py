import sqlite3

connection = sqlite3.connect("restaurants.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT,
    michelin_stars INTEGER,
    rating INTEGER,
    cuisine TEXT
)
""")

restaurants_data = [
    ("Street 1", 2, 4.7, "українська"),
    ("Street 2", 3, 4.9, "італійська"),
    ("Street 3", 1, 4.5, "азіатська"),
    ("Street 4", 0, 3.8, "німецька"),
    ("Street 5", 2, 4.3, "британська")
]

# З цим моментом трохи допоміг Chatgpt
cursor.executemany("""
INSERT INTO restaurants (address, michelin_stars, rating, cuisine)
VALUES (?, ?, ?, ?)
""", restaurants_data)

connection.commit()
connection.close()

print("Success")
