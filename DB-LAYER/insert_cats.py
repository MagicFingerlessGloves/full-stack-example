import os
import psycopg2

def insert_cat(name, breed, age):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "catsdb"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", 5432)
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO cats (name, breed, age) VALUES (%s, %s, %s);",
        (name, breed, age)
    )
    conn.commit()
    print(f"Inserted cat: {name}, {breed}, {age}")
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Example usage
    insert_cat("Tiger", "Tabby", 3)