from psycopg2 import sql
from conexion import conexion

lista_tablas = [
    'users',
    'vehicles',
    'trips',
    'resumen_diario',
    'example_table'
]

conn,cur = conexion()

for tabla in lista_tablas:
    cur.execute(f"DROP TABLE IF EXISTS {tabla} CASCADE;")

conn.commit()
conn.close()
