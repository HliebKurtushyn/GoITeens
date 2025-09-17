import psycopg2

# Підключення до БД
conn = psycopg2.connect(
    dbname="my_database",
    user="postgres",
    password="300911",
    host="127.0.0.1",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        age INT
    );
""")
conn.commit()  # Збереження змін


# Виконання SQL-запиту
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

# Вивід отриманих даних
for row in rows:
    print(row)

# Закриття з'єднання
conn.close()