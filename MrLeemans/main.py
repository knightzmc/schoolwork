import sqlite3


def setup_sqlite():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER primary key autoincrement,
        surname TEXT not null,
        forename TEXT not null,
        dob DATE not null,
        address DATE not null,
        phone_number DATE not null,
        gender TEXT not null,
        tutor_group TEXT not null,
        email NVARCHAR(230) not null
    );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
        username TEXT primary key,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()


def get_connection():
    conn = sqlite3.connect('data.db')
    return conn


def username_exists(username) -> bool:
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM credentials WHERE username=?', (username,))
    user = c.fetchone()
    conn.close()
    return user is not None


def validate_password(username, password) -> bool:
    conn = get_connection()
    c = conn.cursor()

    c.execute('SELECT password FROM credentials WHERE username=?', (username,))
    db_password = c.fetchone()[0]
    return db_password == password


def login():
    username = input("Input Username:\n")
    if not username_exists(username):
        print("No such user")
        return login()

    password = input("Input Password:\n")
    valid_password = validate_password(username, password)
    if not valid_password:
        print("Invalid Password")
        return login()

    print(f"Hello, {username}")


if __name__ == '__main__':
    setup_sqlite()
    login()
