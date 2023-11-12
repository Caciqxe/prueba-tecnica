from psycopg2 import sql
from conexion import conexion

conn, cur = conexion()

query = """
    SELECT *
    FROM resumen_diario
    LIMIT 20
"""

cur.execute(query)
tablas = cur.fetchall()

for tabla in tablas:
    print(tabla)

conn.commit()
conn.close()