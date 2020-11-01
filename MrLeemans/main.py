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

    c.execute('''
        CREATE TABLE IF NOT EXISTS column_aliases (
        alias TEXT primary key,
        column TEXT
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


def get_column_by_alias(alias):
    conn = get_connection()
    c = conn.cursor()

    c.execute('SELECT column FROM column_aliases WHERE alias=?', (alias,))
    val = c.fetchone()
    c.close()
    return val


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


def command_prompt():
    print('''
    Welcome. Please select a task:
    1. Find a Student
    2. Add a Student
    3. Remove a Student
    4. View all Students
    5. Change Password
    6. Logout
    7. Exit
    ''')

    task = input()
    if task == '1':
        return command_find_student()


def command_find_student():
    print('Enter a column name to search by:')
    print('Options: first_name, last_name, id')
    column = input()
    column_name = get_column_by_alias(column)
    if column_name is None:
        print(f'Could not find column {column}')
        return command_find_student()

    print('Input value to search for')
    value = input()

    conn = get_connection()
    c = conn.cursor()

    query = f"SELECT * FROM users WHERE {column_name} = ?"
    c.execute(query, (value,))
    results = c.fetchall()
    if len(results) == 0:
        print("No Results Found.")
        return command_find_student()
    print(results)


if __name__ == '__main__':
    setup_sqlite()
    login()
    command_prompt()
