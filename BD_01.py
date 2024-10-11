import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#for i in range(1, 11):
    #cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    #(f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))
#for i in range(1, 11, 2):
    #cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))
#for i in range(1, 11, 3):
    #cursor.execute('DELETE FROM Users WHERE id = ?', (i,))
#cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
#users = cursor.fetchall()
#my_table = ['Имя: ', ' | Почта: ', ' | Возраст: ', ' | Баланс: ']
#for user in users:
    #for i in range(len(user)):
        #print(my_table[i], end='')
        #print(user[i], end='')
    #print()

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(total_users)

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances)

cursor.execute('SELECT COUNT(*) FROM Users')
print(all_balances / total_users)

cursor.execute('SELECT AVG(balance) FROM Users')# Упрощает код, не нужен SELECT SUM, и SELECT COUNT
avg_balance = cursor.fetchone()[0]
print(avg_balance)


connection.commit()
connection.close()