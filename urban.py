import sqlite3
contact = sqlite3.connect('dt.db')
cursor = contact.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL,
    description TEXT, 
    price INT NOT NULL
    )
    ''')


initiate_db()
'''for i in range(1, 5):
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                   (f'Продукт{i}', f"Описание{i}", f"{i * 100}"))
'''

s=[]
def get_all_products():
    cursor.execute('SELECT * FROM Products')
    a = cursor.fetchall()
    s=[]
    for i in a:
        s.append(list(i))
    return s
