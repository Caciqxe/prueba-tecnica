from psycopg2 import sql
from conexion import conexion

conn, cur = conexion()

command = """
CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    name_user VARCHAR(255) NOT NULL,
    rut_user INT NOT NULL
);

CREATE TABLE IF NOT EXISTS vehicles(
    vehicle_id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS trips(
    trip_id VARCHAR(255) PRIMARY KEY,
    user_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    membership_id INT NOT NULL,
    booking_time TIMESTAMP NOT NULL,
    status_id INT NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    start_lat VARCHAR(255),
    start_lon VARCHAR(255),
    end_lat VARCHAR(255),
    end_lon VARCHAR(255),
    travel_dist NUMERIC,
    price_amount NUMERIC,
    price_tax NUMERIC,
    price_total NUMERIC,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

CREATE TABLE IF NOT EXISTS resumen_diario(
    resumen_id VARCHAR(255) PRIMARY KEY,
    dia TIMESTAMP NOT NULL,
    conteo_usuarios INT NOT NULL,
    precio_total NUMERIC NOT NULL,
    precio_promedio NUMERIC NOT NULL,
    metros_total NUMERIC NOT NULL
)
"""

cur.execute(command)
conn.commit()

conn.close()