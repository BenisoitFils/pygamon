import psycopg2

# Configura la conexión a la base de datos
conn = psycopg2.connect(
    dbname='test_db',
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432'
)

# Crea un cursor para ejecutar consultas SQL
cur = conn.cursor()

# Ejecuta una consulta
cur.execute("SELECT * FROM persona")

# Obtiene los resultados
rows = cur.fetchall()
for row in rows:
    print(row)

# Cierra el cursor y la conexión
cur.close()
conn.close()
