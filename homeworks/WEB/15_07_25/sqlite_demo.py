import sqlite3

conn = sqlite3.connect('events.db')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    price INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(event_id) REFERENCES events(id)
);
''')

conn.commit()

cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    users = [("Gleb",), ("Sasha",), ("Denis",)]
    cursor.executemany("INSERT INTO users (username) VALUES (?)", users)
    
    events = [("Concert",), ("Festival",), ("Performance",)]
    cursor.executemany("INSERT INTO events (event_name) VALUES (?)", events)
    
    tickets = [(1, 2, 500), (2, 1, 300), (3, 3, 1900), (1, 3, 2000), (2, 3, 199), (3, 3, 555), (1, 3, 122)]
    cursor.executemany("INSERT INTO tickets (user_id, event_id, price) VALUES (?, ?, ?)", tickets)
    
conn.commit()

cursor.execute(''' 
SELECT tickets.id, users.username, events.event_name, tickets.price
FROM tickets
JOIN users ON tickets.user_id = users.id
JOIN events on tickets.event_id = events.id
            ''')
print("All tickets:")
for row in cursor.fetchall():
    print(row)
    
cursor.execute('''
SELECT events.event_name, COUNT(tickets.id) AS ticket_count
FROM tickets
JOIN events ON tickets.event_id = events.id
GROUP BY events.id
HAVING COUNT(tickets.id) > 5
''')
print("\nEvents with more than 5 tickets:")
for row in cursor.fetchall():
    print(row)

cursor.execute('''
SELECT DISTINCT users.username
FROM tickets
JOIN users ON tickets.user_id = users.id
WHERE tickets.price > 500
''')
print("\nUsers which bought tickets which price more than 500:")
for row in cursor.fetchall():
    print(row)

conn.close()
