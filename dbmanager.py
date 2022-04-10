import bcrypt
import psycopg2

def getConnection():
    conn = None
    try:
        conn = psycopg2.connect(
            host = "tasklistwsb.postgres.database.azure.com",
            database = "postgres", 
            user = "taskadmin", 
            password = "2A6shEiVvtB9psWcRCoE",
            port = 5432)
        #print("Postgre Version: ")
        #cur = conn.cursor()
        #cur.execute("select version()")
        #db_version = cur.fetchone()
        #print(db_version)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error) #log error
    return conn

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

def createUser(username, password):
    if(userExists(username) == True):
        # info ze user istnieje
        return

    bytePwd = password.encode('utf-8')
    hash = bcrypt.hashpw(bytePwd, bcrypt.gensalt())
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
        cur.execute(sql, (username, hash))
        updated_count = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(f"Updated count: {updated_count}")

def loginUser(username, password):
    loginSuccess = False
    conn = getConnection()
    

def insertTask():
    print("insert task")

def modifyTask():
    print("modify task")



# test 
# getConnection()

createUser("test@tesdsst.com", "testPassword123")