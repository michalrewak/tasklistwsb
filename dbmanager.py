import bcrypt
import psycopg2

# Gets connection to the Postgre DB
def getConnection():
    conn = None
    with open('pass.txt', 'r') as f:
        passw = f.readline()

    try:
        conn = psycopg2.connect(
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
    except(Exception, psycopg2.DatabaseError) as error:
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
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return userExists

# Checks if user exists and if not, creates new one and hashes its password using bcrypt
def createUser(username, password):
    if(userExists(username) == True):
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
    updated_count=0
    try:
        cur = conn.cursor()
        cur.execute(sql, (username, hash.decode("utf-8")))
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
    if(userExists(username) == False):
        return 

    conn = getConnection()
    sql = """
    select id, password from tasks.assignee where email = %s
    """
    loginSuccess = False
    try:
        cur = conn.cursor()
        cur.execute(sql, (username,))
        if(cur.rowcount == 0):
            loginSuccess == False
            return
        passw = cur.fetchone()[1]
        print(passw)
        utf8Password = password.encode("utf-8")
        loginSuccess == bcrypt.checkpw(utf8Password, passw.encode("utf-8"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insertTask():
    print("insert task")

def modifyTask():
    print("modify task")

def getTasks():
    print("get tasks")



# test 
# getConnection()

createUser("test3@tesdsst.com", "testPassword123")
loginUser("test3@tesdsst.com", "testPassword123")