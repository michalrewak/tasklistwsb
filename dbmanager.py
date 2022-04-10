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

def createUser():
    print("create user")

def loginUser():
    conn = getConnection()
    cur = conn.cursor()

def insertTask():
    print("insert task")

def modifyTask():
    print("modify task")



# test 
getConnection()