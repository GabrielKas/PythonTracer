# PythonTracer
**PythonTracer for tests in Database, Monitoring, Webservers and Cloud**


This Program was inspired by ChatGPT Input:
- "Let's Work, looking for a simple python program that can generate traces and simple calls to database"
- "i want to access the program by a web address"


With the First Setup:
This program connects to a SQLite database (example.db), creates a table named records if it doesn't exist already, generates traces consisting of a timestamp and some random data, and then inserts these traces into the database. The program runs indefinitely until interrupted by the user (usually by pressing Ctrl+C).


With the second setup:
you can run the program, and it will expose an endpoint /traces which returns all traces stored in the database in JSON format. You can access this endpoint by navigating to http://127.0.0.1:5000/traces in your web browser or by making a GET request to that URL programmatically.
