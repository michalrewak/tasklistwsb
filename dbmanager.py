import bcrypt
import psycopg


# Gets connection to the Postgre DB
def getConnection():
    conn = None
    with open('pass.txt', 'r') as f:
        passw = f.readline()

    try:
        conn = psycopg.connect(
            host = "tasklistwsb.postgres.database.azure.com",
            database = "postgres", 
            user = "taskadmin", 
            password = passw,
            port = 5432)
        #print("Postgre Version: ")
        #cur = conn.cursor()
        #cur.execute("select version()")
        #db_version = cur.fetchone()
        #print(db_version)
    except(Exception, psycopg.DatabaseError) as error:
        print(error) #log error
    return conn


# Check if user exists in DB
def userExists(username):
    sql = """select id from tasks.assignee where email = %s"""
    conn = getConnection()
    userExists = False
    try:
        cur = conn.cursor()
        cur.execute(sql, (username,))
        userExists = cur.rowcount != 0
        cur.close()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return userExists


# Checks if user exists and if not, creates new one and hashes its password using bcrypt
def createUser(username, password):
    if (userExists(username) == True):
        # info ze user istnieje
        return

    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    sql = """
        INSERT INTO tasks.assignee (email, password, isadmin)
    VALUES 
    (
        %s,
        %s,
        false
    )"""
    conn = getConnection()
    updated_count = 0
    try:
        cur = conn.cursor()
        cur.execute(sql, (username, hash.decode("utf-8")))
        updated_count = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Updated count: {updated_count}")


# Check if user exists, then checks if password is correct
def loginUser(username, password):
    if (userExists(username) == False):
        return

    conn = getConnection()
    sql = """
    select id, password from tasks.assignee where email = %s
    """
    loginSuccess = False
    try:
        cur = conn.cursor()
        cur.execute(sql, (username,))
        if (cur.rowcount == 0):
            loginSuccess == False
            return
        passw = cur.fetchone()[1]
        print(passw)
        utf8Password = password.encode("utf-8")
        loginSuccess == bcrypt.checkpw(utf8Password, passw.encode("utf-8"))
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# inserts entire task into database 
def insertTask(title, priority, assigne_id, desc, status):
    conn = getConnection()
    sql = """
    INSERT INTO tasks.task (title, priority, assigneid, description, status)
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (title, priority, assigne_id, desc, status))
        updated_count = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Updated count: {updated_count}")

def modifyTask(taskid, title, priority, desc, status):
    conn = getConnection()
    sql = """
        UPDATE tasks.task
        SET
            title = %s,
            priority = %s,
            description = %s,
            status = %s
        WHERE
            id = %s
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (title, priority, desc, status, taskid))
        updated_count = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Updated count: {updated_count}")

def getTasks(user_id = None):
    print("get tasks")

def getTasks(user_id = None):
    if user_id is None:
        items = [
            {"id": "1", "title": "task1", "priority": "niski", "assignee": "Michał", "assignee_id" : "1"},
            {"id": "2", "title": "task2", "priority": "średni", "assignee": "Andrzej", "assignee_id" : "2"},
            {"id": "3", "title": "task3", "priority": "średni", "assignee": "Enrico", "assignee_id" : "3"},
            {"id": "4", "title": "task4", "priority": "średni", "assignee": "Leonid", "assignee_id" : "4"}
            ]
        return items

    items = [
        {"id": "1", "title": "task1", "priority": "niski", "assignee": "Michał", "assignee_id": "1"},
        {"id": "2", "title": "task2", "priority": "średni", "assignee": "Andrzej", "assignee_id": "2"},
        {"id": "3", "title": "task3", "priority": "średni", "assignee": "Enrico", "assignee_id": "3"},
        {"id": "4", "title": "task4", "priority": "średni", "assignee": "Leonid", "assignee_id": "4"}
    ]

    return [task for task in items if task['assignee_id'] == user_id]

# test
# getConnection()
#
# createUser("test3@tesdsst.com", "testPassword123")
# loginUser("test3@tesdsst.com", "testPassword123")
