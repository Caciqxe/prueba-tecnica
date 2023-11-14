from psycopg2 import sql
from conexion import conexion

conn, cur = conexion()

query = """
    SELECT *
    FROM information_schema.tables
    WHERE table_schema = 'public';
"""

cur.execute(query)
tablas = cur.fetchall()

print("Tablas creadas:")
for tabla in tablas:
    print(tabla[2])

conn.commit()
conn.close()