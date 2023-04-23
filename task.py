import sqlite3
# Завдання 1. 
# - Створи об‘єкт conn, що відповідає за створення та підключення до БД bank.db 
# - Створи об‘єкт cur, завдяки якому буде можливість робити SQL-запити до БД
# - Створи таблицю clients у БД, що має наступні поля: id, name, money_balance

conn = sqlite3.connect("bank.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY,
    name TEXT,
    money_balance INT)""")




# Завдання 2. 
# - Створи SQL-запити, кожен з яких буде додавати нового клієнта у БД: ('Bill', 1000), ('Bob', 500), ('Anna', 2000).

#! list_client = [('Bill', 1000), ('Bob', 500), ('Anna', 2000)]
#! cur.executemany("""INSERT INTO clients(name, money_balance) VALUES(?, ?)""", list_client)

# Завдання 3.
# - Створи запит, що отримає клієнта з id 1

#! cur.execute("SELECT * FROM clients WHERE id = 1")
#! print(cur.fetchone())
# - Створи запит, що отримає усіх клієнтів
#! cur.execute("SELECT * FROM clients")
#! print(cur.fetchall())
# - Створи запит, що отримає уісх клієнтів, баланс яких більше або дорівнює 700

cur.execute("SELECT * FROM clients WHERE money_balance >= 700")
print(cur.fetchall())


# Завдання 4.
# - Створи запит, що змінить ім‘я клієнта з id 1 на Billy

# Завдання 5.
# - створи запит, ща видалить усіх усіх клієнтів, баланс яких менше або дорівнює 1000
conn.commit()