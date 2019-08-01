import os

import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv("C9_USER")

# Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'Chinook')
                            
try:
    # Run a query
    # Once you have a Connection (see connection above), you can create a Cursor object and call 
    # its execute() method to perform SQL commands.
    # This will display the data in tuples by row
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection regardless of whether the above was successful or not
    connection.close()