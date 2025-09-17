import sqlite3

# Створення або підключення до бази даних
connection = sqlite3.connect("playlist.db")
cursor = connection.cursor()

# Створення таблиці для збереження пісень
cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name TEXT NOT NULL,
    artist TEXT NOT NULL,
    genre TEXT,
    release_year INTEGER
)
''')

print("Таблиця 'songs' створена успішно!")
connection.commit()
connection.close()