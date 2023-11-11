import psycopg2
print('start')
# Connect to the database
conn = psycopg2.connect(host='db', port=5432, dbname='example', user='postgres', password='1234')

# Create a cursor
cur = conn.cursor()

# Create the table
cur.execute('CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(255) NOT NULL)')

# Commit the changes
conn.commit()
print('ok')
# Close the connection
conn.close()