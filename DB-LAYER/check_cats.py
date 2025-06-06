import os
import psycopg2

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "catsdb"),
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD", "postgres"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=os.getenv("POSTGRES_PORT", 5432)
)

cur = conn.cursor()
cur.execute("SELECT id, name, breed, age FROM cats;")
rows = cur.fetchall()

print("Cats in database:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Breed: {row[2]}, Age: {row[3]}")

cur.close()
conn.close()