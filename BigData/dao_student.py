import sqlite3

def create_table():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            user_id TEXT,
            password TEXT
        );
    ''')
    conn.commit()
    conn.close()

def add_user(user):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (name, phone, email, user_id, password)
        VALUES (?, ?, ?, ?, ?)
    ''', (user['name'], user['phone'], user['email'], user['user_id'], user['password']))
    conn.commit()
    conn.close()

def get_user_by_id(user_id):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    if user:
        return {
            'id': user[0],
            'name': user[1],
            'phone': user[2],
            'email': user[3],
            'user_id': user[4],
            'password': user[5]
        }
    else:
        return None
