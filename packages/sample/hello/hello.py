import psycopg2
from urllib.parse import urlparse, parse_qs

def main(args):
    name = args.get('name', 'stranger')
    conn_str = "postgresql://doadmin:AVNS_VSGbT6K2T6WSOZQvp_0@db-postgresql-sgp1-03058-do-user-16324282-0.h.db.ondigitalocean.com:25060/defaultdb?sslmode=require"

    # Parse connection string
    result = urlparse(conn_str)
    conn_params = {
        'dbname': result.path[1:],  # skip leading '/'
        'user': result.username,
        'password': result.password,
        'host': result.hostname,
        'port': result.port,
        'sslmode': parse_qs(result.query).get('sslmode', ['require'])[0]
    }

    try:
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        server_time = cur.fetchone()[0]

        cur.close()
        conn.close()

        return { "body": f"Hello {name}! The time is {server_time}." }
    except Exception as e:
        return { "statusCode": 500, "body": f"Database connection failed: {e}" }
