import psycopg2
import time

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin1234"
)

conn.autocommit = True
cursor = conn.cursor()

def send_email(account_id, message):
    # For workshop: just print
    print(f"[EMAIL SENT] Account: {account_id} | Message: {message}")

while True:
    cursor.execute("""
        SELECT notification_id, account_id, message
        FROM notification_queue
        WHERE processed = false
        ORDER BY created_at
    """)
    
    rows = cursor.fetchall()

    for notification_id, account_id, message in rows:
        send_email(account_id, message)

        cursor.execute("""
            UPDATE notification_queue
            SET processed = true
            WHERE notification_id = %s
        """, (notification_id,))

    time.sleep(5)
