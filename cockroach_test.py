import logging
import os
import psycopg2

def print_hello(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT message FROM messages")
        logging.debug("print_hello(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        for row in rows:
            print(row[0])

def main():
    conn_string = input('Enter a connection string:\n')

    conn = psycopg2.connect(os.path.expandvars(conn_string))
    print_hello(conn)

    conn.close()

if __name__ == "__main__":
    main()
