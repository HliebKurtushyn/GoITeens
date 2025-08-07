import psycopg2

conn = psycopg2.connect(
    dbname='tests',
    user='postgres',
    password='300911',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

# Наскільки пам'ятаю, то в цьому коді має змінитись створення id (SERIAL) і тут не треба йому тип (типу INTEGER) давати, і автозбільшення саме
# Ну ще наче безпечний інсерт трохи по іншому а не (?). Якщо спрацює - добре

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
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
    cursor.executemany("INSERT INTO users (username) VALUES (%s)", users)
    
    events = [("Concert",), ("Festival",), ("Performance",)]
    cursor.executemany("INSERT INTO events (event_name) VALUES (%s)", events)
    
    tickets = [(1, 2, 500), (2, 1, 300), (3, 3, 1900), (1, 3, 2000), (2, 3, 199), (3, 3, 555), (1, 3, 122)]
    cursor.executemany("INSERT INTO tickets (user_id, event_id, price) VALUES (%s, %s, %s)", tickets)
    
conn.commit()

cursor.execute(''' 
SELECT tickets.id, users.username, events.event_name, tickets.price
FROM tickets
JOIN users ON tickets.user_id = users.id
JOIN events ON tickets.event_id = events.id
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
