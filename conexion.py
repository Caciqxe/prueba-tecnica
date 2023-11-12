import psycopg2

def conexion():
    HOST = 'db'
    PORT = 5432
    USER = 'postgres'
    DB = 'example'
    PASS = '1234'
    
    conn = psycopg2.connect(host=HOST, port=PORT, dbname=DB, user=USER, password=PASS)
    cur = conn.cursor()

    return conn, cur