from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = connect(
    dbname = "postgres",
    user = "postgres",
    host = "host.docker.internal",
    password = "postgres"
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE rwdb")
cursor.close()
conn.close()