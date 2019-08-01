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
    with connection.cursor() as cursor:
       list_of_names = ['jim', 'bob', 'fred']
       # Prepare a list with the same number of placeholders as in list_of_names
       # e.g. format_strings will = [%s,%s,%s]
       format_strings = ','.join(['%s']*len(list_of_names))
       cursor.execute("DELETE FROM Friends WHERE name in ({})".format(format_strings), list_of_names)
       connection.commit()
finally:
    # Close the connection regardless of whether the above was successful or not
    connection.close()