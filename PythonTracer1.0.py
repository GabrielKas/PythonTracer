'''
Sure! Here's a simple Python program that generates traces and makes simple calls to a SQLite database:



This program connects to a SQLite database (example.db), creates a table named records if it doesn't exist already,
generates traces consisting of a timestamp and some random data, and then inserts these traces into the database.
The program runs indefinitely until interrupted by the user (usually by pressing Ctrl+C).




'''





import sqlite3
import random
import time

# Connect to SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS records
             (id INTEGER PRIMARY KEY, timestamp INTEGER, data TEXT)''')

# Function to generate a trace
def generate_trace():
    timestamp = int(time.time())
    data = f"Data-{random.randint(1, 100)}"
    return timestamp, data

# Function to insert trace into database
def insert_trace(timestamp, data):
    c.execute("INSERT INTO records (timestamp, data) VALUES (?, ?)", (timestamp, data))
    conn.commit()

# Main function
def main():
    try:
        while True:
            timestamp, data = generate_trace()
            insert_trace(timestamp, data)
            print(f"Inserted trace: {timestamp}, {data}")
            time.sleep(1)  # Wait for 1 second
    except KeyboardInterrupt:
        conn.close()
        print("\nProgram stopped.")

if __name__ == "__main__":
    main()
