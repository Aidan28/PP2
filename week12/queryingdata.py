import psycopg2
  

DB_NAME = "ndmsevnj"
DB_USER = "ndmsevnj"
DB_PASS = "WVw5AttKjdyH1pi9oWUVk2MexhoXAoF2"
DB_HOST = "queenie.db.elephantsql.com"
DB_PORT = "5432"


conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS,
                            host = DB_HOST, port = DB_PORT)
    
print("Database connected successfully")

cur = conn.cursor()

cur.execute("SELECT ID, NAME, EMAIL FROM employe")

rows = cur.fetchall()

for data in rows:
    print("ID : " + str(data[0]))
    print("Name : " + data[1])
    print("Email : " + data[2])

print("Data selected successfully")
conn.close()