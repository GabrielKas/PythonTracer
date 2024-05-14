'''
If you want to access the program through a web address, you can use a web framework like Flask to create a simple web interface.
Here's an updated version of the program that integrates Flask to expose an endpoint for accessing the traces:

With this setup, you can run the program, and it will expose an endpoint /traces which
returns all traces stored in the database in JSON format.
You can access this endpoint by navigating to http://127.0.0.1:5000/traces in your
web browser or by making a GET request to that URL programmatically.

'''







from flask import Flask, jsonify
import sqlite3
import random
import time

app = Flask(__name__)

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

# Function to get all traces from the database
def get_traces():
    c.execute("SELECT * FROM records")
    return c.fetchall()

# API endpoint to get all traces
@app.route('/traces', methods=['GET'])
def get_traces_api():
    traces = get_traces()
    return jsonify(traces)

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
