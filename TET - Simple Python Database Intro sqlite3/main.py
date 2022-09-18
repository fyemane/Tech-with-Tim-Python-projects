# https://www.youtube.com/watch?v=IL300fe71cU
# To use the module, you must first create a Connection object that represents the database.
# # the data will be stored in the demo.db file:
import sqlite3

# connect to databse
con = sqlite3.connect('demo.db')

# create cursor object, sending info to database
cur = con.cursor()

# Create table
# call its execute() method to perform SQL commands:
# cur.execute("CREATE TABLE contacts (name text, phone text, city text)")

# Insert a row of data
# cur.execute("INSERT INTO contacts VALUES ('Jenny', '867-5309', 'Los Angeles')")

# update values
cur.execute("UPDATE contacts SET city='Dallas' WHERE name='Jenny'")

# retrieve values
cur.execute("SELECT * FROM contacts WHERE name='Jenny'")

# pool all different results from cursor object
results = cur.fetchall()
print(results)

# it is tuple inside list
# print(results[0][0], results[0][1], results[0][2])

# Save (commit) the changes to databse
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
