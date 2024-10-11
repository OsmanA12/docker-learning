# app.py

from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Connect to the Redis database
    db = MySQLdb.connect(
        host="mydb1",    # Hostname of the MySQL redis container
        user="root",    # Username to connect to MySQL redis
        passwd="my-secret-pw",  # Password for the MySQL redis user
        db="MySQLredis"      # Name of the database to connect to
    )
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Welcome Ladies and Gentlemen! MySQL rdedis version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)