from database import get_db_connection


def create_tables():
    print("CREATE TABLE FUNCTION RUNNING")

    conn = get_db_connection()

    print("ABOUT TO EXECUTE SQL")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_email TEXT NOT NULL,
        category TEXT NOT NULL,
        priority TEXT NOT NULL,
        meeting_date TEXT NOT NULL,
        message TEXT NOT NULL,
        status TEXT DEFAULT 'pending'
        )
    """)

    print("SQL EXECUTED")

    conn.commit()

    print("COMMIT DONE")

    conn.close()


def add_user(name, email, password, role):

    conn = get_db_connection()

    try:

        conn.execute("""
            INSERT INTO users (name, email, password, role)
            VALUES (?, ?, ?, ?)
        """, (name, email, password, role))

        conn.commit()

        return True

    except:

        return False

    finally:
        conn.close()


def check_user(email, password):
    conn = get_db_connection()

    user = conn.execute("""
        SELECT * FROM users
        WHERE email = ?
        AND password = ?
    """, (email, password)).fetchone()

    conn.close()

    return user


def add_request(student_email, category, priority, meeting_date, message):

    conn = get_db_connection()

    conn.execute("""
        INSERT INTO requests
        (student_email, category, priority, meeting_date, message,status)

        VALUES (?, ?, ?, ?, ?, ?)
    """, (student_email, category, priority, meeting_date, message,"pending"))

    conn.commit()
    conn.close()
def get_requests():

    conn = get_db_connection()

    requests = conn.execute("""
        SELECT * FROM requests
    """).fetchall()

    conn.close()

    return requests
def update_status(request_id, new_status):

    conn = get_db_connection()

    conn.execute("""
        UPDATE requests

        SET status = ?

        WHERE id = ?
    """, (new_status, request_id))

    conn.commit()
    conn.close()
def get_student_requests(email):

    conn = get_db_connection()

    requests = conn.execute("""
        SELECT * FROM requests
        WHERE student_email = ?
    """, (email,)).fetchall()

    conn.close()

    return requests