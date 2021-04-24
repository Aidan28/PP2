import psycopg2
  

DB_NAME = "ndmsevnj"
DB_USER = "ndmsevnj"
DB_PASS = "WVw5AttKjdyH1pi9oWUVk2MexhoXAoF2"
DB_HOST = "queenie.db.elephantsql.com"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS,
                            host = DB_HOST, port = DB_PORT)
    
    print("Database connected successfully")

except:
    print("Database not connected")