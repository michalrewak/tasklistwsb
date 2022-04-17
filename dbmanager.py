import bcrypt
import psycopg2


# Gets connection to the Postgre DB
def getConnection():
    conn = None
    with open('pass.txt', 'r') as f:
        passw = f.readline()
    try:
        conn = psycopg2.connect(
            host="tasklistwsb.postgres.database.azure.com",
            database="postgres",
            user="taskadmin",
            password=passw,
            port=5432)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)  # log error
    return conn


# Check if user exists in DB
def userExists(username):
    sql = """select id from tasks.assignee where email = %s"""
    conn = getConnection()
    user_exists = False
    try:
        cur = conn.cursor()
        cur.execute(sql, (username,))
        user_exists = cur.rowcount != 0
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return user_exists


# Checks if user is admin based on id
def userIsAdmin(user_id):
    sql = """select isadmin from tasks.assignee where id = %s"""
    conn = getConnection()
    user_is_admin = False
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        user_is_admin = cur.fetchone()[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return user_is_admin


# Gets user email
def userEmail(user_id):
    sql = """select email from tasks.assignee where id = %s"""
    conn = getConnection()
    user_email = ""
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        user_email = cur.fetchone()[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return user_email


# Checks if user exists and if not, creates new one and hashes its password using bcrypt
def createUser(username, password):
    if userExists(username):
        # info ze user istnieje
        return

    bcrypt_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
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
        cur.execute(sql, (username, bcrypt_hash.decode("utf-8")))
        updated_count = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Updated count: {updated_count}")


# Check if user exists, then checks if password is correct
def loginUser(username, password):
    if not userExists(username):
        return

    conn = getConnection()
    sql = """
    select id, password from tasks.assignee where email = %s
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (username,))
        if cur.rowcount == 0:
            return -1
        row = cur.fetchone()
        passw = row[1]
        id = row[0]
        print(passw)
        utf8_password = password.encode("utf-8")
        if bcrypt.checkpw(utf8_password, passw.encode("utf-8")):
            return id
        else:
            return -1
    except (Exception, psycopg2.DatabaseError) as error:
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
    updated_count = 0
    try:
        cur = conn.cursor()
        cur.execute(sql, (title, priority, assigne_id, desc, status))
        updated_count = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Updated count: {updated_count}")


# modifies task and does not care what have been modified by user, updates everything
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
    updated_count = 0
    try:
        cur = conn.cursor()
        cur.execute(sql, (title, priority, desc, status, taskid))
        updated_count = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Updated count: {updated_count}")


def delete_task(task_id):
    conn = getConnection()
    sql = """
        DELETE FROM tasks.task
	    WHERE id = %s
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (task_id,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# Gets user tasks if specified or all tasks
def getTasks(user_id):
    conn = getConnection()
    sql = "select t.id, title, priority, email, a.id, description from tasks.task t inner join tasks.assignee a on a.id=t.assigneid"
    items = []
    row_count = 0
    is_admin = userIsAdmin(user_id)
    if not is_admin:
        sql += " where assigneid = %s"
    try:
        cur = conn.cursor()
        if not is_admin:
            cur.execute(sql, (user_id,))
        else:
            cur.execute(sql)

        row_count = cur.rowcount
        row = cur.fetchone()
        while row:
            items.append({"id": row[0], "title": row[1], "priority": row[2], "assignee": row[3], "assignee_id": row[4], "description": row[5]})
            row = cur.fetchone()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Returned count: {row_count}")
    return items

# test
# getConnection()
# createUser("test3@tesdsst.com", "testPassword123")
# loginUser("test3@tesdsst.com", "testPassword123")
# getTasks(3) 
# insertTask(
#     "Testowy tytul zadania", 
#     1, 
#     2, 
#     """Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
#     Vivamus gravida tellus iaculis leo semper, eget volutpat mi dictum. """,
#     "W trakcie")
# modifyTask(4, "Testowy tytul zadania", 2, "Vivamus gravida tellus iaculis leo semper, eget volutpat mi dictum. Cras fermentum purus vitae diam sodales viverra.", "W trakcie")
